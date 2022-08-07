import struct
import pickle

from datastructures import *

DEFAULT_LEVEL_LOC = "./resources/LaserTank.lvl"

DEFAULT_LPB_LOC = "./resources/LaserTank_0001.lpb"

CONVEYORS_DIRECTIONS = {
    c.CONVEYOR_UP: UP,
    c.CONVEYOR_RIGHT: RIGHT,
    c.CONVEYOR_DOWN: DOWN,
    c.CONVEYOR_LEFT: LEFT,
}


class Game:
    def __init__(self):
        self.state: GameState = GameState()

        self.moves_history = []
        self.moves_buffer = []  # RecBuffer
        self.undo_state = []
        self.sounds_buffer = []

        # Static Info
        self.level_info = LevelInfo(1, "", "", "", "", "")

        # Control flags
        self.running = True

        # Dynamic flags
        self.tank_moving_on_conveyor = False

        self.microtick = 0

    def is_objects_sliding(self):
        """Is anything sliding? Originally named SlideO_s"""
        return len(self.state.sliding_items) > 0

    def is_inputs_queued(self):
        """Are there player moves waiting in the buffer to be played?"""
        return len(self.moves_buffer) > 0

    def is_tank_on_terrain(self):
        """If the tank up on an object from a trick-shot then the tank is not on the terrain"""
        return self.state.items[self.state.tank.sq] == c.EMPTY

    def is_ice(self, sq: Square):
        return self.state.terrain[sq] == c.ICE or self.state.terrain[sq] == c.THINICE

    def load_level(self, level_number, filename=DEFAULT_LEVEL_LOC):
        self.state.sliding_items = {}
        self.moves_history = []
        self.moves_buffer = []
        self.state.score_shots = 0
        self.state.score_moves = 0
        self.undo_state = []
        self.sounds_buffer = []

        if level_number < 1:
            level_number = 1
        struct_format = "<256s31s256s31sH"  # tLevel C structure
        chunk_size = struct.calcsize(struct_format)  # 576
        byte_offset = chunk_size * (level_number - 1)
        with open(filename, "rb") as f:
            f.seek(byte_offset, 0)  # Seek to byte offset relative to start of file
            chunk = f.read(chunk_size)
            if not chunk:
                return None
        playfield_ints, title, hint, author, difficulty_int = struct.unpack(
            struct_format, chunk
        )

        def convert_null_terminated_bytes_to_str_helper(in_bytes):
            """Convert null terminated string from bytes to python string"""
            return in_bytes.split(b"\x00")[0].decode("mbcs")

        title = convert_null_terminated_bytes_to_str_helper(title)
        hint = convert_null_terminated_bytes_to_str_helper(hint)
        author = convert_null_terminated_bytes_to_str_helper(author)
        difficulty = c.DIFFICULTY_TEXTS.get(difficulty_int, c.DIFFICULTY_TEXTS[1])
        self.level_info = LevelInfo(level_number, title, hint, author, difficulty, filename)

        for sq in SQUARES:
            # Note that lvl files are saved in columns and playfield is in [x][y]
            i = int(playfield_ints[sq.y + sq.x * c.PLAYFIELD_SIZE])
            terrain, item = c.DECODE_TABLE.get(i, (c.GRASS, c.EMPTY))
            # Tank is not placed in the items array
            if item == c.TANK:
                self.state.tank = TankRec(sq, direction=UP)
                self.state.items[sq] = c.EMPTY
            else:
                self.state.items[sq] = item
            self.state.terrain[sq] = terrain

    def queue_new_inputs(self, new_inputs):
        self.moves_buffer.extend(new_inputs)

    def tick(self):
        # Main game loop (see C-3043)
        if c.K_UNDO in self.moves_buffer:
            self.moves_buffer = []
            self.undo()
        elif c.K_RESET in self.moves_buffer:
            self.load_level(self.level_info.number, self.level_info.filename)
        elif c.K_LVL_PRE in self.moves_buffer:
            self.load_level(self.level_info.number - 1, self.level_info.filename)
        elif c.K_LVL_NXT in self.moves_buffer:
            self.load_level(self.level_info.number + 1, self.level_info.filename)

        if self.microtick == 0:
            self.tick_laser_turn()
        elif self.microtick == 1:
            self.tick_tank_turn()
        elif self.microtick == 2:
            self.tick_resolve_object_momenta()
        elif self.microtick == 3:
            self.tick_resolve_tank_momenta()
        elif self.microtick == 4:
            self.tick_tank_destination()

        self.microtick += 1
        if self.microtick > 4:
            self.microtick = 0

    def tick_laser_turn(self):
        if self.state.laser_live:
            self.MoveLaser()

    def tick_tank_turn(self):
        # Process keyboard buffer
        if self.moves_buffer and not (
                self.state.laser_live
                or self.tank_moving_on_conveyor
                or self.is_objects_sliding()
                or self.state.tank.is_sliding
        ):
            move = self.moves_buffer.pop(0)
            if move == c.K_SHOOT:
                self.UpdateUndo()
                self.state.score_shots += 1
                self.FireLaser(self.state.tank.sq, self.state.tank.direction, True)
                self.MoveLaser()
            elif move in [c.K_UP, c.K_RIGHT, c.K_DOWN, c.K_LEFT]:
                K_TO_DIRECTION = {c.K_UP: UP, c.K_RIGHT: RIGHT, c.K_DOWN: DOWN, c.K_LEFT: LEFT}
                dr = K_TO_DIRECTION.get(move)
                # MoveTank
                if self.state.tank.direction != dr:
                    # Tank is turning
                    self.state.tank.direction = dr
                    self.SoundPlay(c.S_Turn)
                else:
                    destination = self.state.tank.sq.relative(dr)
                    if self.is_on_board_and_empty(destination):
                        self.SoundPlay(c.S_Move)
                        self.UpdateUndo()
                        self.state.score_moves += 1
                        self.state.tank.sq = self.state.tank.sq.relative(dr)
                        self.check_tunnel_tank()
                        if self.is_ice(destination):
                            self.state.tank.is_sliding = True
                            # self.tank.sliding_sq = self.tank.sq
                            self.state.tank.sliding_dr = dr
                    else:
                        self.SoundPlay(c.S_Head)  # Bumping into something
            self.AntiTank()

    def tick_resolve_object_momenta(self):
        # Resolve Momenta
        if self.is_objects_sliding():
            # self.IceMoveO()  # NOTE: IceMoveO includes additional AntiTank() moves
            # Move an item on the ice
            for sliding_item_sq, sliding_item_dr in reversed(list(self.state.sliding_items.items())):
                if self.state.terrain[sliding_item_sq] == c.THINICE:
                    # Sliding off thin ice so melt the ice into water
                    self.state.terrain[sliding_item_sq] = c.WATER

                # if destination is empty (not item and not tank)
                # note: CheckLoc also sets wasIce to True is destination is Ice or ThinIce
                destination = sliding_item_sq.relative(sliding_item_dr)
                if self.is_on_board_and_empty(destination) and not destination == self.state.tank.sq:
                    self.MoveObj(sliding_item_sq, sliding_item_dr)
                    self.AntiTank()
                    if not self.is_ice(destination):
                        del self.state.sliding_items[sliding_item_sq]
                    else:
                        # Update position of tracked sliding object
                        # Insert destination item at the position of the original
                        new_list = {}
                        for s, d in self.state.sliding_items.items():
                            if s == sliding_item_sq:
                                new_list[destination] = d
                            else:
                                new_list[s] = d
                        new_list[destination] = sliding_item_dr
                        self.state.sliding_items = new_list
                else:
                    if self.state.terrain[sliding_item_sq] == c.WATER:
                        # Drop into water if ice melted and item couldn't move
                        self.sink_item_in_water(sliding_item_sq)
                    del self.state.sliding_items[sliding_item_sq]
                    self.AntiTank()

    def tick_resolve_tank_momenta(self):
        if self.state.tank.is_sliding:
            # self.IceMoveT()
            #  Move the tank on the Ice
            if self.state.terrain[self.state.tank.sq] == c.THINICE:
                self.state.terrain[self.state.tank.sq] = c.WATER

            destination = self.state.tank.sq.relative(self.state.tank.sliding_dr)
            if self.is_on_board_and_empty(destination):
                # self.ConvMoveTank(self.tank.sliding_dr)
                self.state.tank.sq = self.state.tank.sq.relative(self.state.tank.sliding_dr)
                # self.tank_moving_on_conveyor = True
                self.check_tunnel_tank()
                self.AntiTank()
                # Move tank an additional square
                # self.tank.sq = self.tank.sq.relative(self.tank.sliding_dr)
                if not self.is_ice(destination):
                    self.state.tank.is_sliding = False
            else:
                self.state.tank.is_sliding = False
        self.tank_moving_on_conveyor = False  # used to disable Laser on the conveyor

    def tick_tank_destination(self):
        if self.is_tank_on_terrain():
            # Check where the tank ended up
            tank_terrain = self.state.terrain[self.state.tank.sq]
            if tank_terrain == c.FLAG:
                self.game_over(victorious=True)
            elif tank_terrain == c.WATER:
                self.game_over(victorious=False)
            elif tank_terrain in CONVEYORS_DIRECTIONS:
                direction = CONVEYORS_DIRECTIONS.get(tank_terrain)
                if self.is_on_board_and_empty(self.state.tank.sq.relative(direction)):
                    # self.ConvMoveTank(direction)
                    self.state.tank.sq = self.state.tank.sq.relative(direction)
                    self.tank_moving_on_conveyor = True
                    self.check_tunnel_tank()
                    if self.is_ice(self.state.tank.sq):
                        self.state.tank.is_sliding = True
                        self.state.tank.sliding_dr = direction
                    self.AntiTank()

    def game_over(self, victorious):
        self.running = False
        # Skipping sound, playback, save recording
        if victorious:
            # self.CheckHighScore()
            self.state.reached_flag = True
        else:
            self.state.player_dead = True
        print(f"Game over! {'Win!' if victorious else 'Dead!'}")

    # def change_tank_sq(self, destination):
    #     self.tank.sq = destination
    #
    # def change_item(self, sq, new_item):
    #     self.items[sq] = new_item
    #
    # def change_terrain(self, sq, new_terrain):
    #     self.terrain[sq] = new_terrain

    # def ConvMoveTank(self, direction):
    #     # Move tank in the direction of the conveyor
    #     self.state.tank.sq = self.state.tank.sq.relative(direction)
    #     self.tank_moving_on_conveyor = True

    def check_tunnel_tank(self):
        self.state.tank.on_waiting_tunnel = False
        # Check if tank ended up on a tunnel
        if self.is_tunnel(self.state.tank.sq):
            tunnel_exit = self.find_tunnel_exit(self.state.tank.sq)
            if tunnel_exit is None:
                # Tank fell in a black hole
                self.game_over(victorious=False)
            elif tunnel_exit == self.state.tank.sq:
                # Blocked exit found
                self.state.tank.on_waiting_tunnel = True
            else:
                self.state.tank.sq = tunnel_exit

    # def check_ice_tank(self, direction):
    #     if self.is_ice(self.state.tank.sq):
    #         # self.tank.sliding_sq = self.tank.sq
    #         self.state.tank.is_sliding = True
    #         self.state.tank.sliding_dr = direction

    def is_on_board_and_empty(self, sq):
        """ Return True if a sq is on the board and is EMPTY """
        return False if sq is None else self.state.items[sq] == c.EMPTY

    def check_loc_move_start_sliding(self, sq, dr):
        """ For when some objects are hit by a laser (Block, Mirrors, Antitanks)
        Move object in dr, return True if was able """
        # Stop it sliding if already
        self.state.sliding_items.pop(sq, None)
        destination = sq.relative(dr)
        if destination is None or self.state.items[destination] != c.EMPTY:
            # Hitting edge of board or occupied square
            self.SoundPlay(c.S_LaserHit)
        else:
            self.MoveObj(sq, dr)
            if self.is_ice(destination):
                self.state.sliding_items[destination] = dr

    def AntiTank(self):
        # Look for antitanks on same row/col as tank and let them fire (only if laser not already existing)
        # Order: Right, left, down, above from Tank

        # Only one laser on board so returns if laser exists
        if self.state.laser_live:
            return

        # Tank on an item is hidden from AntiTanks
        if not self.is_tank_on_terrain():
            return

        for scan_dir, antitank, shoot_dir in [
            (RIGHT, c.ANTITANK_LEFT, LEFT),
            (LEFT, c.ANTITANK_RIGHT, RIGHT),
            (DOWN, c.ANTITANK_UP, UP),
            (UP, c.ANTITANK_DOWN, DOWN),
        ]:
            sq = self.state.tank.sq
            while self.is_on_board_and_empty(sq := sq.relative(scan_dir)):
                pass
            if sq is not None and (self.state.items[sq] == antitank):
                self.FireLaser(sq, shoot_dir, False)
                self.MoveLaser()
                break

    def FireLaser(self, sq, dr, is_player_tank):

        self.state.laser_live = True

        self.state.laser.dir_front = dr
        self.state.laser.dir_back = dr
        self.state.laser.sq = sq

        if is_player_tank:
            self.state.laser.colour = c.LaserColorG
            self.SoundPlay(c.S_Fire)
        else:
            self.state.laser.colour = c.LaserColorR
            self.SoundPlay(c.S_Anti2)
        # self.MoveLaser()

    def UpdateUndo(self):
        # Should be done whenever player moves or shoots
        self.undo_state.append(pickle.dumps(self.state))

    def PopUndo(self):
        # Remove an undo when tank moving through a tunnel
        if len(self.undo_state) > 0:
            return pickle.loads(self.undo_state.pop())
        else:
            return None

    def undo(self):
        old_state = self.PopUndo()
        if old_state is not None:
            self.state = old_state

    def MoveLaser(self):

        if not self.running:
            return

        LaserBounceOnIce = True
        while LaserBounceOnIce:
            LaserBounceOnIce = False
            dr = self.state.laser.dir_front
            sq = self.state.laser.sq.relative(dr)

            self.state.laser.dir_back = self.state.laser.dir_front

            if sq is None:
                # Laser out of board
                self.state.laser_live = False
            elif sq == self.state.tank.sq:
                # Hit tank
                self.game_over(victorious=False)
            else:
                item_loc = self.state.items[sq]

                # Laser interact with item
                if item_loc == c.EMPTY:
                    pass

                elif item_loc == c.GLASS:
                    # In original, this is where glass is set to a glowing sprite
                    pass

                elif item_loc == c.SOLID:
                    self.state.laser_live = False
                    self.SoundPlay(c.S_LaserHit)

                elif item_loc == c.BLOCK:
                    self.state.laser_live = False
                    # Can block be moved in direction of laser? Is square free
                    self.check_loc_move_start_sliding(sq, dr)

                elif item_loc == c.WALL:
                    self.state.laser_live = False
                    self.state.items[sq] = c.EMPTY  # Destroy wall with laser
                    self.SoundPlay(c.S_Bricks)

                elif item_loc in c.DEADANTITANK_ALL:  # Include dead tanks as solid items
                    self.state.laser_live = False
                    self.SoundPlay(c.S_LaserHit)
                    self.state.sliding_items.pop(sq, None)

                elif item_loc in c.ANTITANKS_ALL:
                    ANTITANK_HIT_DIRECTION = {
                        c.ANTITANK_UP: (DOWN, c.DEADANTITANK_UP),
                        c.ANTITANK_RIGHT: (LEFT, c.DEADANTITANK_RIGHT),
                        c.ANTITANK_DOWN: (UP, c.DEADANTITANK_DOWN),
                        c.ANTITANK_LEFT: (RIGHT, c.DEADANTITANK_LEFT),
                    }
                    hit_direction, deadantitank = ANTITANK_HIT_DIRECTION.get(item_loc)
                    self.state.laser_live = False
                    if dr == hit_direction:  # Laser hit front of antitank
                        # Kill Antitank
                        self.state.items[sq] = deadantitank
                        self.SoundPlay(c.S_Anti1)
                    else:
                        self.check_loc_move_start_sliding(sq, dr)

                elif item_loc in [c.MIRROR_LEFT_UP, c.MIRROR_UP_RIGHT, c.MIRROR_RIGHT_DOWN, c.MIRROR_DOWN_LEFT, ]:
                    MIRROR_REFLECTION_DIRECTION = {
                        c.MIRROR_LEFT_UP: {UP: None, RIGHT: UP, DOWN: LEFT, LEFT: None},
                        c.MIRROR_UP_RIGHT: {UP: None, RIGHT: None, DOWN: RIGHT, LEFT: UP},
                        c.MIRROR_RIGHT_DOWN: {UP: RIGHT, RIGHT: None, DOWN: None, LEFT: DOWN},
                        c.MIRROR_DOWN_LEFT: {UP: LEFT, RIGHT: DOWN, DOWN: None, LEFT: None},
                    }
                    reflection_direction = MIRROR_REFLECTION_DIRECTION.get(item_loc).get(dr)
                    if reflection_direction is not None:
                        self.state.laser.dir_front = reflection_direction
                        self.SoundPlay(c.S_Deflb)
                        if sq in self.state.sliding_items:
                            LaserBounceOnIce = True
                    else:
                        self.state.laser_live = False
                        self.check_loc_move_start_sliding(sq, dr)

                elif item_loc in [c.ROTMIRROR_LEFT_UP, c.ROTMIRROR_UP_RIGHT, c.ROTMIRROR_RIGHT_DOWN,
                                  c.ROTMIRROR_DOWN_LEFT, ]:
                    ROTMIRROR_REFLECTION_DIRECTION = {
                        c.ROTMIRROR_LEFT_UP: {
                            UP: c.ROTMIRROR_UP_RIGHT,
                            RIGHT: UP,
                            DOWN: LEFT,
                            LEFT: c.ROTMIRROR_UP_RIGHT
                        },
                        c.ROTMIRROR_UP_RIGHT: {
                            UP: c.ROTMIRROR_RIGHT_DOWN,
                            RIGHT: c.ROTMIRROR_RIGHT_DOWN,
                            DOWN: RIGHT,
                            LEFT: UP
                        },
                        c.ROTMIRROR_RIGHT_DOWN: {
                            UP: RIGHT,
                            RIGHT: c.ROTMIRROR_DOWN_LEFT,
                            DOWN: c.ROTMIRROR_DOWN_LEFT,
                            LEFT: DOWN
                        },
                        c.ROTMIRROR_DOWN_LEFT: {
                            UP: LEFT,
                            RIGHT: DOWN,
                            DOWN: c.ROTMIRROR_LEFT_UP,
                            LEFT: c.ROTMIRROR_LEFT_UP
                        },
                    }
                    reflection_action = ROTMIRROR_REFLECTION_DIRECTION.get(item_loc).get(dr)
                    if type(reflection_action) is Direction:
                        self.state.laser.dir_front = reflection_action
                        self.SoundPlay(c.S_Deflb)
                    else:
                        self.state.laser_live = False
                        self.state.items[sq] = reflection_action
                        self.SoundPlay(c.S_Rotate)

            # Check destination square and start objects there moving if needed
            if self.state.laser_live:
                # Laser is still on the board
                # Move laser
                self.state.laser.sq = self.state.laser.sq.relative(dr)
            else:
                # Laser is off the board / hit something solid
                # Antitank Turn
                self.AntiTank()

                # TestIfConvCanMoveTank: Used to handle the speed bug
                terrain_tank_on = self.state.terrain[self.state.tank.sq]
                if self.is_tank_on_terrain() and (
                        (
                                terrain_tank_on == c.CONVEYOR_UP
                                and self.is_on_board_and_empty(self.state.tank.sq.relative(UP))
                        )
                        or (
                                terrain_tank_on == c.CONVEYOR_RIGHT
                                and self.is_on_board_and_empty(self.state.tank.sq.relative(RIGHT))
                        )
                        or (
                                terrain_tank_on == c.CONVEYOR_DOWN
                                and self.is_on_board_and_empty(self.state.tank.sq.relative(DOWN))
                        )
                        or (
                                terrain_tank_on == c.CONVEYOR_LEFT
                                and self.is_on_board_and_empty(self.state.tank.sq.relative(LEFT))
                        )
                ):
                    self.tank_moving_on_conveyor = True
        # loops here if LaserBounceOnIce was set in the loop

    def is_tunnel(self, sq):
        return self.state.terrain[sq] in c.TUNNEL_ALL

    def SoundPlay(self, sound_id):
        self.sounds_buffer.append(sound_id)

    def find_tunnel_exit(self, sq) -> [None, Square]:
        """
        Look for other tunnels that match the one on this square
        Return:
            Square() != sq if empty exit found
            sq if blocked exit(s) found
            None if black hole (no exits on map)
        """

        tunnel_id = self.state.terrain[sq]

        found_blocked_exit = False

        # Find an empty destination tunnel
        for sqx in SQUARES:
            if self.state.terrain[sqx] == tunnel_id and not sqx == sq:
                # Found an exit tunnel (and not the same as entry)
                if self.state.items[sqx] != c.EMPTY:
                    # Exit is blocked
                    found_blocked_exit = True
                else:
                    return sqx

        if found_blocked_exit:
            return sq
        else:
            # No exit found, so Tunnel is a Black Hole
            return None

    def MoveObj(self, sq: Square, dr: Direction):
        # Try to move object on square x,y that was pushed in dir dx,dy then play sound sf
        # Update terrain under object's initial position (x,y)
        # Also unblock tunnel if Obj blocking tunnel and let other end activate (cx,cy)
        # used by CheckLLoc and IceMoveO
        item = self.state.items[sq]  # Get object type

        # Trigger waiting tunnel if vacating a tunnel
        if self.is_tunnel(sq):
            # Unblock tunnel
            self.move_item_off_tunnel(sq)
        else:
            self.state.items[sq] = c.EMPTY

        # Now update destination
        dest = sq.relative(dr)
        self.move_item_to_destination(dest, item)

    def move_item_off_tunnel(self, sq: Square):
        # Search for a blocked tunnel with the same ID
        tunnel_waiting_id = c.Tunnel_Set_Waiting[self.state.terrain[sq]]
        tunnel_id = c.Tunnel_Set_Not_Waiting[tunnel_waiting_id]

        for sqx in SQUARES:
            if (
                    self.state.terrain[sqx] == tunnel_waiting_id
                    and self.state.items[sqx] != c.EMPTY
                    and not (sqx == sq)
            ):
                # We are moving an object through a tunnel
                # Other end of blocked tunnel had an object so move it through now
                # Move object through a tunnel (from xy to cx, cy)
                # Transfer blocked object
                self.state.items[sq] = self.state.items[sqx]
                self.state.items[sqx] = c.EMPTY
                self.state.terrain[sqx] = tunnel_id
                break
        else:
            # Did not find another end of this tunnel with an object on
            # Not Blocked Anymore
            self.state.items[sq] = c.EMPTY
            self.state.terrain[sq] = c.Tunnel_Set_Not_Waiting[self.state.terrain[sq]]

            # We didn't find a match so maybe the tank is it
            if self.state.tank.on_waiting_tunnel and self.state.terrain[self.state.tank.sq] == tunnel_id:
                self.check_tunnel_tank()

    def move_item_to_destination(self, dest: Square, item):
        # If destination is a tunnel then set dest to tunnel's exit
        if self.is_tunnel(dest):
            tunnel_exit = self.find_tunnel_exit(dest)
            if tunnel_exit is None:
                return  # The tunnel was a black hole
            elif tunnel_exit == dest:
                self.state.terrain[dest] = c.Tunnel_Set_Waiting[self.state.terrain[dest]]
            else:
                dest = tunnel_exit

        self.state.items[dest] = item
        if self.state.terrain[dest] == c.WATER:
            # Destination square is water
            self.sink_item_in_water(dest)
        else:
            # Move object to destination square
            self.SoundPlay(c.S_Push2)

    def sink_item_in_water(self, sq: Square):
        item = self.state.items[sq]
        self.state.items[sq] = c.EMPTY
        if item == c.BLOCK:
            self.state.terrain[sq] = c.BRIDGE
        self.SoundPlay(c.S_Sink)
