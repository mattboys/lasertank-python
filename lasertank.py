import struct
import pickle

import pygame
import pygame.locals

import constants as c

DEFAULT_LEVEL_LOC = "./resources/LaserTank.lvl"
DEFAULT_SPRITESHEET_LOC = "./resources/spritesheet.png"
DEFAULT_LPB_LOC = "./resources/LaserTank_0001.lpb"

Direction = tuple
UP: Direction = (0, -1)
DOWN: Direction = (0, 1)
LEFT: Direction = (-1, 0)
RIGHT: Direction = (1, 0)
STATIONARY: Direction = (0, 0)

CONVEYORS_DIRECTIONS = {
    c.CONVEYOR_UP: UP,
    c.CONVEYOR_RIGHT: RIGHT,
    c.CONVEYOR_DOWN: DOWN,
    c.CONVEYOR_LEFT: LEFT,
}


class Square(int):
    def __new__(cls, x, y=None):
        if y is None:
            value = x
        else:
            if not Square.on_board(x, y):
                raise ValueError(f"Square ({x},{y}) is not on the board.")
            value = x + (y * c.PLAYFIELD_SIZE)
        return int.__new__(cls, value)

    @staticmethod
    def on_board(x, y):
        return 0 <= x < c.PLAYFIELD_SIZE and 0 <= y < c.PLAYFIELD_SIZE

    @property
    def coords(self):
        return self.x, self.y

    @property
    def x(self) -> int:
        return self % c.PLAYFIELD_SIZE

    @property
    def y(self) -> int:
        return int(self / c.PLAYFIELD_SIZE)

    def relative(self, direction: Direction):
        """ Return the square one space in the specified direction if on the board, None otherwise """
        x, y = self.coords
        dx, dy = direction
        xp = x + dx
        yp = y + dy
        if not Square.on_board(xp, yp):
            return None
        else:
            return Square(xp, yp)

    def __repr__(self):
        return f"Square({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x},{self.y})"


SQUARES = [Square(x, y) for y in range(c.PLAYFIELD_SIZE) for x in range(c.PLAYFIELD_SIZE)]


class TankRec:
    def __init__(
            self,
            sq: Square,
            direction: Direction,
            on_waiting_tunnel=False,
            is_sliding=False,
            sliding_dr=STATIONARY
    ):
        self.sq: Square = sq
        self.direction: Direction = direction
        self.on_waiting_tunnel = on_waiting_tunnel  # Indicates that tank is on a waiting tunnel
        self.is_sliding = is_sliding
        self.sliding_dr: Direction = sliding_dr

    def __repr__(self):
        return f"TankRec({self.sq}, {self.direction}, {self.on_waiting_tunnel}, {self.is_sliding}, {self.sliding_dr})"


class LaserRec:
    def __init__(
            self,
            sq=Square(5, 10),
            dir_front=UP,
            dir_back=LEFT,
            colour=c.LaserColorR,
    ):
        self.sq: Square = sq
        self.dir_front: Direction = dir_front
        self.dir_back: Direction = dir_back
        self.colour = colour


class LevelInfo:
    def __init__(
            self,
            number: int,
            title: str,
            hint: str,
            author: str,
            difficulty: str,
            filename: str,
    ):
        self.number: int = number
        self.title: str = title
        self.hint: str = hint
        self.author: str = author
        self.difficulty: str = difficulty
        self.filename: str = filename


# class SlidingData:  # Sliding Struct
#     def __init__(
#             self,
#             sq: Square,
#             dr: Direction,
#     ):
#         self.sq: Square = sq  # Last XY position of object to move
#         self.dr: Direction = dr  # Direction to move in Delta Cords


class GameState:
    def __init__(self):
        self.terrain = [c.GRASS for _ in range(c.PLAYFIELD_SIZE ** 2)]
        self.items = [c.EMPTY for _ in range(c.PLAYFIELD_SIZE ** 2)]
        self.tank = TankRec(Square(x=7, y=15), direction=UP)
        self.laser = LaserRec()
        self.laser_live = False
        self.sliding_items: dict[Square, Direction] = {}
        self.score_shots = 0
        self.score_moves = 0
        self.reached_flag = False
        self.player_dead = False


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
        # Was named SlideO_s
        # Is anything sliding?
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
                    self.check_ice_tank(direction)
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

    def ConvMoveTank(self, direction):
        # Move tank in the direction of the conveyor
        self.state.tank.sq = self.state.tank.sq.relative(direction)
        self.tank_moving_on_conveyor = True

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

    def check_ice_tank(self, direction):
        if self.is_ice(self.state.tank.sq):
            # self.tank.sliding_sq = self.tank.sq
            self.state.tank.is_sliding = True
            self.state.tank.sliding_dr = direction

    def is_on_board_and_empty(self, sq):
        return False if sq is None else self.state.items[sq] == c.EMPTY

    def check_loc_move_start_sliding(self, sq, dr):

        # Stop it sliding if already
        self.state.sliding_items.pop(sq, None)

        destination = sq.relative(dr)
        if destination is None or self.state.items[destination] != c.EMPTY:
            # Hitting edge of board or occupied square
            return False

        item = self.state.items[sq]  # Get object type

        self.MoveObj(sq, dr)

        # MoveObj2(sq, dr, c.S_Push1)
        if self.is_ice(destination):
            self.state.sliding_items[destination] = dr

        return True

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
                    if not self.check_loc_move_start_sliding(sq, dr):
                        self.SoundPlay(c.S_LaserHit)

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
                    elif not self.check_loc_move_start_sliding(sq, dr):
                        self.SoundPlay(c.S_LaserHit)

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
                        if not self.check_loc_move_start_sliding(sq, dr):
                            self.SoundPlay(c.S_LaserHit)

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
                        (terrain_tank_on == c.CONVEYOR_UP and self.is_on_board_and_empty(
                            self.state.tank.sq.relative(UP)))
                        or (terrain_tank_on == c.CONVEYOR_RIGHT and self.is_on_board_and_empty(
                    self.state.tank.sq.relative(RIGHT)))
                        or (terrain_tank_on == c.CONVEYOR_DOWN and self.is_on_board_and_empty(
                    self.state.tank.sq.relative(DOWN)))
                        or (terrain_tank_on == c.CONVEYOR_LEFT and self.is_on_board_and_empty(
                    self.state.tank.sq.relative(LEFT)))
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


class Graphics:
    MENUBAR_SIZE = 19
    SPRITE_SIZE = 32  # SpBm_Width, SpBm_Height
    SPRITE_SHEET_ROWS = 6
    SPRITE_SHEET_COLUMNS = 10
    SIDEBAR_SIZE = 187
    GAMEBOARD_SIZE = SPRITE_SIZE * c.PLAYFIELD_SIZE
    BOARD_GUTTER = 17
    OFFSET_LEFT = BOARD_GUTTER  # XOffset
    OFFSET_TOP = BOARD_GUTTER + MENUBAR_SIZE  # YOffset
    DISPLAY_SIZE = (
        OFFSET_LEFT + GAMEBOARD_SIZE + BOARD_GUTTER + SIDEBAR_SIZE,
        OFFSET_TOP + GAMEBOARD_SIZE + BOARD_GUTTER,
    )

    TUNNEL_ID_COLOURS = [
        # c: 0x00bbggrr
        # py:0xrrggbbaa
        pygame.Color(0xFF_00_00_FF),  # Red
        pygame.Color(0x00_FF_00_FF),  # Green
        pygame.Color(0x00_00_FF_FF),  # Blue
        pygame.Color(0x00_FF_FF_FF),  # Cyan
        pygame.Color(0xFF_FF_00_FF),  # Yellow
        pygame.Color(0xFF_00_FF_FF),  # Magenta
        pygame.Color(0xFF_FF_FF_FF),  # White
        pygame.Color(0x80_80_80_FF),  # Gray
    ]

    LASER_COLOURS = {
        c.LaserColorG: pygame.Color(0x00FF00FF),
        c.LaserColorR: pygame.Color(0xFF0000FF),
    }
    LASER_OFFSET = 13  # LaserOffset
    ANIMATION_RATE = 20

    BLACK = pygame.Color(0, 0, 0)
    LIGHT_GRAY = pygame.Color(192, 192, 192)
    GRAY = pygame.Color(128, 128, 128)
    WHITE = pygame.Color(255, 255, 255)
    RED = pygame.Color(255, 0, 0)
    FONT_SIZE_COORDS = 13

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=self.DISPLAY_SIZE, flags=0)
        self.spritesheet = pygame.image.load(DEFAULT_SPRITESHEET_LOC).convert_alpha()
        self.animation_counter = 0
        self.animation_rate_counter = 0
        self.screen.fill(self.LIGHT_GRAY)
        self.font = pygame.font.SysFont("arial", size=self.FONT_SIZE_COORDS)

        self.rect_menu = pygame.Rect(0, 0, self.DISPLAY_SIZE[0], self.MENUBAR_SIZE)
        self.rect_playfield = pygame.Rect(self.OFFSET_LEFT, self.OFFSET_TOP, self.GAMEBOARD_SIZE, self.GAMEBOARD_SIZE)
        self.rect_coords = pygame.Rect(0, self.MENUBAR_SIZE,
                                       self.GAMEBOARD_SIZE + self.BOARD_GUTTER + self.BOARD_GUTTER,
                                       self.GAMEBOARD_SIZE + self.BOARD_GUTTER + self.BOARD_GUTTER)

    def _increment_animation_counter(self):
        self.animation_rate_counter += 1
        if self.animation_rate_counter >= self.ANIMATION_RATE:
            self.animation_rate_counter = 0
            self.animation_counter = (self.animation_counter + 1) % 3

    def _draw_text(self, text, position, colour, background):
        rendered_text = self.font.render(str(text), True, colour, background)
        self.screen.blit(rendered_text, rendered_text.get_rect(center=position))

    def _draw_embossed(self, rect: pygame.Rect, inner=True, double=False):
        if inner:
            colour1 = self.WHITE
            colour2 = self.GRAY

            pygame.draw.line(self.screen, colour1, (rect.left + 1, rect.bottom - 2), (rect.left + 1, rect.top + 1))
            pygame.draw.line(self.screen, colour1, (rect.left + 2, rect.top + 1), (rect.right - 3, rect.top + 1))
            pygame.draw.line(self.screen, colour2, (rect.left + 2, rect.bottom - 2), (rect.right - 3, rect.bottom - 2))
            pygame.draw.line(self.screen, colour2, (rect.right - 2, rect.bottom - 2), (rect.right - 2, rect.top + 1))

        else:
            colour1 = self.GRAY
            colour2 = self.WHITE
            pygame.draw.line(self.screen, colour1, (rect.left - 1, rect.bottom), (rect.left - 1, rect.top - 1))
            pygame.draw.line(self.screen, colour1, (rect.left, rect.top - 1), (rect.right - 1, rect.top - 1))
            pygame.draw.line(self.screen, colour2, (rect.left, rect.bottom), (rect.right, rect.bottom))
            pygame.draw.line(self.screen, colour2, (rect.right, rect.bottom - 1), (rect.right, rect.top - 1))
            if double:
                pygame.draw.line(self.screen, colour1, (rect.left - 2, rect.bottom + 1), (rect.left - 2, rect.top - 2))
                pygame.draw.line(self.screen, colour1, (rect.left - 1, rect.top - 2), (rect.right, rect.top - 2))
                pygame.draw.line(self.screen, colour2, (rect.left - 1, rect.bottom + 1),
                                 (rect.right + 1, rect.bottom + 1))
                pygame.draw.line(self.screen, colour2, (rect.right + 1, rect.bottom), (rect.right + 1, rect.top - 2))

    def _draw_board_coords(self):
        for i in range(c.PLAYFIELD_SIZE):
            l = str(i + 1)
            x = self.rect_playfield.left - int(self.BOARD_GUTTER / 2) - 1
            y = self.rect_playfield.top + int(self.rect_playfield.height / c.PLAYFIELD_SIZE * (i + 0.5))
            self._draw_text(l, (x, y), self.GRAY, self.LIGHT_GRAY)
            x = self.rect_playfield.right + int(self.BOARD_GUTTER / 2)
            self._draw_text(l, (x, y), self.GRAY, self.LIGHT_GRAY)

            l = chr(ord("A") + i)
            x = self.rect_playfield.left + int(self.rect_playfield.width / c.PLAYFIELD_SIZE * (i + 0.5))
            y = self.rect_playfield.top - int(self.BOARD_GUTTER / 2)
            self._draw_text(l, (x, y), self.GRAY, self.LIGHT_GRAY)
            y = self.rect_playfield.bottom + int(self.BOARD_GUTTER / 2)
            self._draw_text(l, (x, y), self.GRAY, self.LIGHT_GRAY)

    def draw_board(self, game: Game):
        self._draw_menu()
        self._draw_sidebar()
        self._draw_background()
        self._draw_board_coords()
        self._draw_embossed(self.rect_playfield, inner=False, double=True)
        self._draw_embossed(self.rect_coords)

        for sq in SQUARES:
            self._draw_sprite(game.state.terrain[sq], sq)
            self._draw_sprite(game.state.items[sq], sq)
        self._draw_tank(game.state.tank.sq, game.state.tank.direction)
        if game.state.laser_live:
            self._draw_laser(game.state.laser)
        pygame.display.update()
        self._increment_animation_counter()

    def _draw_menu(self):
        pygame.draw.rect(self.screen, self.WHITE, self.rect_menu, width=0, border_radius=0)

    def _draw_sidebar(self):
        sidebar_rect = pygame.Rect(
            self.OFFSET_LEFT + self.GAMEBOARD_SIZE + self.BOARD_GUTTER,
            self.MENUBAR_SIZE,
            self.SIDEBAR_SIZE,
            self.DISPLAY_SIZE[1] - self.MENUBAR_SIZE
        )
        pygame.draw.rect(self.screen, self.LIGHT_GRAY, sidebar_rect, width=0, border_radius=0)

    def _draw_background(self):
        pass

    def _draw_sprite(self, entity_id, square: Square):
        board_location = (
            self.OFFSET_LEFT + (square.x * self.SPRITE_SIZE),
            self.OFFSET_TOP + (square.y * self.SPRITE_SIZE),
            self.SPRITE_SIZE,
            self.SPRITE_SIZE,
        )
        if entity_id == c.EMPTY:
            # Don't need to draw empty item squares
            return
        elif entity_id in c.TunnelID:
            colour = self.TUNNEL_ID_COLOURS[c.TunnelID[entity_id]]
            pygame.draw.rect(self.screen, colour, board_location)
            bmp_id = c.BMP_TUNNEL_MASK
        else:
            try:
                bmp_id = c.SPRITE_MAPPING[entity_id]
            except KeyError:
                assert False, f"Cannot draw entity with ID {entity_id}"

        if isinstance(bmp_id, tuple):
            bmp_id = bmp_id[self.animation_counter]
        sprite_sheet_location = (
            self.SPRITE_SIZE * ((bmp_id - 1) % self.SPRITE_SHEET_COLUMNS),
            self.SPRITE_SIZE
            * ((bmp_id - 1) // self.SPRITE_SHEET_COLUMNS % self.SPRITE_SHEET_ROWS),
            self.SPRITE_SIZE,
            self.SPRITE_SIZE,
        )
        self.screen.blit(self.spritesheet, board_location, sprite_sheet_location)

    def _draw_tank(self, square: Square, direction: Direction):
        board_location = (
            self.OFFSET_LEFT + (square.x * self.SPRITE_SIZE),
            self.OFFSET_TOP + (square.y * self.SPRITE_SIZE),
            self.SPRITE_SIZE,
            self.SPRITE_SIZE,
        )
        TANK_DIRECTION_MAPPING = {
            UP: c.TANK_UP,
            RIGHT: c.TANK_RIGHT,
            DOWN: c.TANK_DOWN,
            LEFT: c.TANK_LEFT,
        }
        bmp_id = c.SPRITE_MAPPING[TANK_DIRECTION_MAPPING[direction]]
        sprite_sheet_location = (
            self.SPRITE_SIZE * ((bmp_id - 1) % self.SPRITE_SHEET_COLUMNS),
            self.SPRITE_SIZE
            * ((bmp_id - 1) // self.SPRITE_SHEET_COLUMNS % self.SPRITE_SHEET_ROWS),
            self.SPRITE_SIZE,
            self.SPRITE_SIZE,
        )
        self.screen.blit(self.spritesheet, board_location, sprite_sheet_location)

    def _draw_laser(self, laser: LaserRec):
        # if laser.Firing:
        colour = self.LASER_COLOURS[laser.colour]
        x = self.OFFSET_LEFT + (laser.sq.x * self.SPRITE_SIZE)
        y = self.OFFSET_TOP + (laser.sq.y * self.SPRITE_SIZE)
        h = self.SPRITE_SIZE / 2
        if laser.dir_front == laser.dir_back:
            # Not deflecting
            if laser.dir_front == UP or laser.dir_front == DOWN:
                # Vertical
                beam = pygame.Rect(
                    x + self.LASER_OFFSET,
                    y,
                    self.SPRITE_SIZE - self.LASER_OFFSET - self.LASER_OFFSET,
                    self.SPRITE_SIZE,
                )
            else:
                # Horizontal
                beam = pygame.Rect(
                    x,
                    y + self.LASER_OFFSET,
                    self.SPRITE_SIZE,
                    self.SPRITE_SIZE - self.LASER_OFFSET - self.LASER_OFFSET,
                )
            pygame.draw.rect(self.screen, colour, beam, width=0, border_radius=2)
            pygame.draw.rect(self.screen, self.BLACK, beam, width=1, border_radius=2)
        else:
            # Deflecting off mirror
            # Draw two parts of the reflecting laser
            def laser_dir_to_rect(direction):
                if direction == UP:
                    return pygame.Rect(
                        x + self.LASER_OFFSET,
                        y,
                        self.SPRITE_SIZE - self.LASER_OFFSET - self.LASER_OFFSET,
                        h,
                    )
                elif direction == RIGHT:
                    return pygame.Rect(
                        x + h,
                        y + self.LASER_OFFSET,
                        self.SPRITE_SIZE - h,
                        self.SPRITE_SIZE - self.LASER_OFFSET - self.LASER_OFFSET,
                    )
                elif direction == DOWN:
                    return pygame.Rect(
                        x + self.LASER_OFFSET,
                        y + h,
                        self.SPRITE_SIZE - self.LASER_OFFSET - self.LASER_OFFSET,
                        self.SPRITE_SIZE - h,
                    )
                elif direction == LEFT:
                    return pygame.Rect(
                        x,
                        y + self.LASER_OFFSET,
                        h,
                        self.SPRITE_SIZE - self.LASER_OFFSET - self.LASER_OFFSET,
                    )

            INVERT_DIRECTION = {
                UP: DOWN,
                RIGHT: LEFT,
                DOWN: UP,
                LEFT: RIGHT,
            }

            beam_a = laser_dir_to_rect(laser.dir_front)
            beam_b = laser_dir_to_rect(INVERT_DIRECTION[laser.dir_back])

            pygame.draw.rect(self.screen, colour, beam_a, width=0, border_radius=2)
            pygame.draw.rect(self.screen, self.BLACK, beam_a, width=1, border_radius=2)

            pygame.draw.rect(self.screen, colour, beam_b, width=0, border_radius=2)
            pygame.draw.rect(self.screen, self.BLACK, beam_b, width=1, border_radius=2)

    @staticmethod
    def colour_helper(c_format_str="0x00bbggrr"):
        """Convert a win32 COLORREF value to a hex HTML"""
        # c: 0x00bbggrr
        # py:0xrrggbbaa
        a = "FF"
        r = c_format_str[8:10]
        g = c_format_str[6:8]
        b = c_format_str[4:6]
        return f"0x{r}{g}{b}{a}"


class InputEngine:
    def __init__(self):
        pygame.init()

    def get_inputs(self):
        # Get inputs
        translated_events = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                    event.type == pygame.locals.KEYDOWN
                    and event.key == pygame.locals.K_ESCAPE
            ):
                return [c.K_QUIT]
            elif (
                    event.type == pygame.locals.KEYDOWN and event.key == pygame.locals.K_UP
            ):
                translated_events.append(c.K_UP)
            elif (
                    event.type == pygame.locals.KEYDOWN
                    and event.key == pygame.locals.K_DOWN
            ):
                translated_events.append(c.K_DOWN)
            elif (
                    event.type == pygame.locals.KEYDOWN
                    and event.key == pygame.locals.K_LEFT
            ):
                translated_events.append(c.K_LEFT)
            elif (
                    event.type == pygame.locals.KEYDOWN
                    and event.key == pygame.locals.K_RIGHT
            ):
                translated_events.append(c.K_RIGHT)
            elif (
                    event.type == pygame.locals.KEYDOWN
                    and event.key == pygame.locals.K_SPACE
            ):
                translated_events.append(c.K_SHOOT)
            elif event.type == pygame.locals.KEYDOWN and event.key == pygame.locals.K_u:
                translated_events.append(c.K_UNDO)
            elif event.type == pygame.locals.KEYDOWN and event.key == pygame.locals.K_r:
                return [c.K_RESET]
            elif event.type == pygame.locals.KEYDOWN and (event.key == pygame.locals.K_PAGEDOWN or event.key ==
                                                          pygame.locals.K_p):
                return [c.K_LVL_PRE]
            elif event.type == pygame.locals.KEYDOWN and (event.key == pygame.locals.K_PAGEUP or event.key ==
                                                          pygame.locals.K_s):
                return [c.K_LVL_NXT]

        return translated_events

    def wait_for_anykey(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (
                        event.type == pygame.locals.KEYDOWN
                        and event.key == pygame.locals.K_ESCAPE
                ):
                    return [c.K_QUIT]
                elif event.type == pygame.locals.KEYDOWN:
                    return []


class TextGraphics:
    @staticmethod
    def draw_interesting_crop(game: Game):
        x_min = y_min = c.PLAYFIELD_SIZE
        x_max = y_max = 0
        for sq in SQUARES:
            if (
                    game.state.terrain[sq] not in (c.GRASS, c.WATER)
                    or game.state.items[sq] != c.EMPTY
                    or game.state.tank.sq == sq
            ):
                # Square of interest
                x_min = min(x_min, sq.x)
                y_min = min(y_min, sq.y)
                x_max = max(x_max, sq.x)
                y_max = max(y_max, sq.y)
        # print(f"x_min: {x_min},y_min: {y_min},x_max: {x_max},y_max: {y_max}")
        print(
            "       "
            + "       ".join(
                [TextGraphics.coordinate(x=x) for x in range(x_min, x_max + 1)]
            )
        )
        for y in range(y_min, y_max + 1):
            print(
                TextGraphics.coordinate(y=y)
                + " : "
                + " | ".join(
                    [
                        TextGraphics.cell_as_numbers(game, Square(x, y))
                        for x in range(x_min, x_max + 1)
                    ]
                )
            )

    @staticmethod
    def print_directions(moves):
        move_mapping = {
            c.K_SHOOT: "*",
            c.K_LEFT: "⮜",
            c.K_UP: "⮝",
            c.K_RIGHT: "⮞",
            c.K_DOWN: "⮟",
        }
        return "".join(move_mapping[m] for m in moves)

    @staticmethod
    def coordinate(x=None, y=None):
        """Translate coordinate to algebraic notation. i.e. (1,2) = 'B03'"""
        x_val = chr(ord("A") + x) if x is not None else ""
        y_val = f"{y + 1:02}" if y is not None else ""
        return f"{x_val}{y_val}"

    @staticmethod
    def cell_as_numbers(game: Game, sq: Square):
        terrain = game.state.terrain[sq]
        item = game.state.items[sq]
        if terrain == c.GRASS:
            terrain = " "
        if item == c.EMPTY:
            item = " "
        if game.state.tank.sq == sq:
            item = "T"
        if game.state.laser_live and game.state.laser.sq == sq:
            terrain = "-"

        return f"{terrain: >2}{item: >3}"


def load_level(filename, level_number):
    game = Game()
    game.load_level(level_number=level_number, filename=filename)
    return game


def convert_null_terminated_bytes_to_str_helper(in_bytes):
    """Convert null terminated string from bytes to python string"""
    return in_bytes.split(b"\x00")[0].decode("mbcs")


def load_playback(filename):
    struct_format = "<31s31sHH"  # PBSRec (tRecordRec) C structure
    chunk_size = struct.calcsize(struct_format)  # 66
    with open(filename, "rb") as f:
        info_chunk = f.read(chunk_size)
        if not info_chunk:
            return None
        level_name, player_name, level_number, buffer_size = struct.unpack(
            struct_format, info_chunk
        )
        moves_chunk = f.read(buffer_size)

    # Clean up byte data
    level_name = convert_null_terminated_bytes_to_str_helper(level_name)
    player_name = convert_null_terminated_bytes_to_str_helper(player_name)
    playback = []
    for move_byte in moves_chunk:
        if move_byte == 0x20:
            playback.append(c.K_SHOOT)
        elif move_byte == 0x25:
            playback.append(c.K_LEFT)
        elif move_byte == 0x26:
            playback.append(c.K_UP)
        elif move_byte == 0x27:
            playback.append(c.K_RIGHT)
        elif move_byte == 0x28:
            playback.append(c.K_DOWN)
        else:
            break
    return {
        "number": level_number,
        "title": level_name,
        "player_name": player_name,
        "playback": playback,
    }


def execute_playback(inputs: list, game: Game):
    game.queue_new_inputs(inputs)
    while game.running and not game.is_inputs_queued():
        game.tick()
    if game.state.reached_flag:
        return "WIN"
    elif game.state.player_dead:
        return "DEAD"
    else:
        return "UNFINISHED"


def debug_level(level_name, level_number):
    pb = load_playback(f"resources/levels/{level_name}_{level_number:04}.lpb")
    game = load_level(f"resources/levels/{level_name}.lvl", pb["number"])
    game.queue_new_inputs(pb["playback"])

    graphics = Graphics()
    txtgrphcs = TextGraphics()
    clock = pygame.time.Clock()
    inputs = InputEngine()

    tick_counter = 0
    timeout_counter = 0
    moves_left_prev = 0

    def display():
        graphics.draw_board(game)
        print("")
        print(f"Tick: {tick_counter}")
        print(f"Moves:{txtgrphcs.print_directions(game.moves_buffer)}")
        print(f"Actions:")
        print(f"Sliding: {game.state.sliding_items}")
        print("Board:")
        txtgrphcs.draw_interesting_crop(game)
        # game.queue_new_inputs(inputs.wait_for_anykey())

    # Initial State
    display()

    while game.running and timeout_counter < 2000:

        # End early if stuck on no moves or inf loop
        moves_left = len(game.moves_buffer)
        if moves_left == 0 or moves_left == moves_left_prev:
            timeout_counter += 1
        else:
            timeout_counter = 0
        moves_left_prev = moves_left

        game.tick()
        tick_counter += 1

        display()

    print(f"End State: {game.state.reached_flag}")
    # game.queue_new_inputs(inputs.wait_for_anykey())


def play_level(level_name, level_number):
    game = load_level(f"resources/levels/{level_name}.lvl", level_number)

    graphics = Graphics()
    clock = pygame.time.Clock()
    inputs = InputEngine()

    graphics.draw_board(game)

    while game.running:
        game.queue_new_inputs(inputs.get_inputs())
        game.tick()
        graphics.draw_board(game)
        clock.tick(100)

    print(f"End State: {game.state.reached_flag}")


if __name__ == "__main__":
    # debug_level("tricks/Tricks", 26)
    play_level("standard_levels/LaserTank", 1)
