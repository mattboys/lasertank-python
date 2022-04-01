import struct

import pygame
import pygame.locals

import constants as c

c.PLAYFIELD_SIZE = 16  # Playfield is 16x16 grid

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
    def __new__(cls, x, y):
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
    def __init__(self, sq: Square, direction: Direction):
        self.sq: Square = sq
        self.direction: Direction = direction
        # self.Firing = False  # Is laser on the board, move to board object?
        self.on_waiting_tunnel = False  # Indicates that tank is on a waiting tunnel
        self.is_sliding = False
        self.sliding_sq: Square = Square(0, 0)
        self.sliding_dr: Direction = STATIONARY


class LaserRec:
    def __init__(self):
        self.sq: Square = Square(5, 10)
        self.dir_front: Direction = UP
        self.dir_back: Direction = LEFT
        self.colour = c.LaserColorR


class LevelInfo:
    def __init__(
            self,
            number: int,
            title: str,
            hint: str,
            author: str,
            difficulty: str,
    ):
        self.number: int = number
        self.title: str = title
        self.hint: str = hint
        self.author: str = author
        self.difficulty: str = difficulty


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
        self.change_log = []
        self.terrain = [c.GRASS for _ in range(c.PLAYFIELD_SIZE ** 2)]
        self.items = [c.EMPTY for _ in range(c.PLAYFIELD_SIZE ** 2)]
        self.tank = TankRec(Square(x=7, y=15), direction=UP)
        self.laser = LaserRec()
        self.laser_live = False
        self.sliding_items: dict[Square, Direction] = {}
        self.moves_history = []
        self.moves_buffer = []  # RecBuffer
        self.score_shots = 0
        self.score_moves = 0
        self.undo_state = []
        self.sounds_buffer = []

        # Static Info
        self.level_info = LevelInfo(1, "", "", "", "")

        # Control flags
        self.running = True
        self.reached_flag = False
        self.player_dead = False

        # Dynamic flags
        self.tank_moving_on_conveyor = False
        # Momentum of tank where SlideT.s = is tank sliding?
        # self.tank_sliding_data = SlidingData(Square(0, 0), STATIONARY)
        # self.previous_tunnel_waiting = False  # Found tunnel output on PF2 (under something)
        # self.previous_tunnel_blackhole = (
        #     False  # True if we TunnleTranslae to a Black Hole (no exit found)
        # )
        # self.wasIce = False

    def is_objects_sliding(self):
        # Was named SlideO_s
        # Is anything sliding?
        return len(self.sliding_items) > 0

    def is_inputs_queued(self):
        """Are there player moves waiting in the buffer to be played?"""
        return len(self.moves_buffer) > 0

    def is_tank_on_terrain(self):
        """If the tank up on an object from a trick-shot then the tank is not on the terrain"""
        return self.items[self.tank.sq] == c.EMPTY

    def is_ice(self, sq: Square):
        return self.terrain[sq] == c.ICE or self.terrain[sq] == c.THINICE

    def load_level(self, level_number, filename=DEFAULT_LEVEL_LOC):
        self.sliding_items = {}
        self.moves_history = []
        self.moves_buffer = []
        self.score_shots = 0
        self.score_moves = 0
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
        self.level_info = LevelInfo(level_number, title, hint, author, difficulty)

        for sq in SQUARES:
            # Note that lvl files are saved in columns and playfield is in [x][y]
            i = int(playfield_ints[sq.y + sq.x * c.PLAYFIELD_SIZE])
            terrain, item = c.DECODE_TABLE.get(i, (c.GRASS, c.EMPTY))
            # Tank is not placed in the items array
            if item == c.TANK:
                self.tank = TankRec(sq, direction=UP)
            else:
                self.items[sq] = item
            self.terrain[sq] = terrain

    def queue_new_inputs(self, new_inputs):
        self.moves_buffer.extend(new_inputs)

    def tick(self):
        # Main game loop (see C-3043)
        # TODO: handle an undo to avoid inf loop
        self.change_log = []
        self.tick_laser_turn()
        self.tick_tank_turn()
        self.tick_resolve_object_momenta()
        self.tick_resolve_tank_momenta()
        self.tick_tank_destination()

    def tick_laser_turn(self):
        if self.laser_live:
            self.MoveLaser()

    def tick_tank_turn(self):
        # Process keyboard buffer
        if self.moves_buffer and not (
                self.laser_live
                or self.tank_moving_on_conveyor
                or self.is_objects_sliding()
                or self.tank.is_sliding
        ):
            move = self.moves_buffer.pop(0)
            self.change_log.append(f"Popped movement {move}")
            if move == c.K_UP:
                self.MoveTank(UP)
            elif move == c.K_RIGHT:
                self.MoveTank(RIGHT)
            elif move == c.K_DOWN:
                self.MoveTank(DOWN)
            elif move == c.K_LEFT:
                self.MoveTank(LEFT)
            elif move == c.K_SHOOT:
                self.UpdateUndo()
                self.score_shots += 1
                self.FireLaser(self.tank.sq, self.tank.direction, True)
            self.AntiTank()

    def tick_resolve_object_momenta(self):
        self.change_log.append("Resolving momenta")
        # Resolve Momenta
        if self.is_objects_sliding():
            # self.IceMoveO()  # NOTE: IceMoveO includes additional AntiTank() moves
            self.change_log.append("Slid object on ice")
            # Move an item on the ice
            for sliding_item_sq, sliding_item_dr in reversed(list(self.sliding_items.items())):
                if self.terrain[sliding_item_sq] == c.THINICE:
                    # Sliding off thin ice so melt the ice into water
                    self.terrain[sliding_item_sq] = c.WATER

                # if destination is empty (not item and not tank)
                # note: CheckLoc also sets wasIce to True is destination is Ice or ThinIce
                destination = sliding_item_sq.relative(sliding_item_dr)
                if self.is_on_board_and_empty(destination) and not destination == self.tank.sq:
                    self.MoveObj(sliding_item_sq, sliding_item_dr, c.S_Push2)
                    self.AntiTank()
                    if not self.is_ice(destination):
                        del self.sliding_items[sliding_item_sq]
                    else:
                        # Update position of tracked sliding object
                        # Insert destination item at the position of the original
                        new_list = {}
                        for s, d in self.sliding_items.items():
                            if s == sliding_item_sq:
                                new_list[destination] = d
                            else:
                                new_list[s] = d
                        new_list[destination] = sliding_item_dr
                        self.sliding_items = new_list
                else:
                    if self.terrain[sliding_item_sq] == c.WATER:
                        # Drop into water if ice melted and item couldn't move
                        self.MoveObj(sliding_item_sq, STATIONARY, c.S_Sink)
                    del self.sliding_items[sliding_item_sq]
                    self.AntiTank()

    def tick_resolve_tank_momenta(self):
        if self.tank.is_sliding:
            # self.IceMoveT()
            self.change_log.append("Slid tank on ice")
            #  Move the tank on the Ice
            if self.terrain[self.tank.sliding_sq] == c.THINICE:
                self.terrain[self.tank.sliding_sq] = c.WATER

            destination = self.tank.sliding_sq.relative(self.tank.sliding_dr)
            if self.is_on_board_and_empty(destination):
                self.ConvMoveTank(self.tank.sliding_dr)
                self.check_tunnel_tank()
                self.AntiTank()
                # Move tank an additional square
                self.tank.sliding_sq = self.tank.sliding_sq.relative(self.tank.sliding_dr)
                if not self.is_ice(destination):
                    self.tank.is_sliding = False
            else:
                self.tank.is_sliding = False
        self.tank_moving_on_conveyor = False  # used to disable Laser on the conveyor

    def tick_tank_destination(self):
        self.change_log.append("Checking tank square")
        if self.is_tank_on_terrain():
            # Check where the tank ended up
            tank_terrain = self.terrain[self.tank.sq]
            if tank_terrain == c.FLAG:
                self.game_over(victorious=True)
            elif tank_terrain == c.WATER:
                self.game_over(victorious=False)
            elif tank_terrain in CONVEYORS_DIRECTIONS:
                direction = CONVEYORS_DIRECTIONS.get(tank_terrain)
                if self.is_on_board_and_empty(self.tank.sq.relative(direction)):
                    self.ConvMoveTank(direction)
                    self.check_tunnel_tank()
                    self.check_ice_tank(direction)
                    self.AntiTank()

    def game_over(self, victorious):
        self.running = False
        # Skipping sound, playback, save recording
        if victorious:
            # self.CheckHighScore()
            self.reached_flag = True
        else:
            self.player_dead = True
        print(f"Game over! {'Win!' if victorious else 'Dead!'}")

    def change_tank_sq(self, destination):
        self.change_log.append((c.TANK, self.tank.sq, destination))
        self.tank.sq = destination

    def change_item(self, sq, new_item):
        self.change_log.append((self.items[sq], sq, new_item))
        self.items[sq] = new_item

    def change_terrain(self, sq, new_terrain):
        self.change_log.append((self.terrain[sq], sq, new_terrain))
        self.terrain[sq] = new_terrain

    def ConvMoveTank(self, direction):
        # Move tank in the direction of the conveyor
        self.tank.sq = self.tank.sq.relative(direction)
        self.tank_moving_on_conveyor = True

    def check_tunnel_tank(self):
        # Check if tank ended up on a tunnel
        if self.is_tunnel(self.tank.sq):
            tunnel_exit = self.find_tunnel_exit(self.tank.sq)
            if tunnel_exit is None:
                # Tank fell in a black hole
                self.game_over(victorious=False)
            elif tunnel_exit == self.tank.sq:
                # Blocked exit found
                self.tank.on_waiting_tunnel = True
            else:
                self.tank.sq = tunnel_exit

    def check_ice_tank(self, direction):
        if self.is_ice(self.tank.sq):
            self.tank.sliding_sq = self.tank.sq
            self.tank.is_sliding = True
            self.tank.sliding_dr = direction

    def is_on_board_and_empty(self, sq):
        return False if sq is None else self.items[sq] == c.EMPTY

    def check_loc_move_start_sliding(self, sq, dr):

        # Stop it sliding if already
        self.sliding_items.pop(sq, None)

        destination = sq.relative(dr)
        if destination is None:
            # Hitting edge of board
            return False

        if self.items[destination] != c.EMPTY:
            return False

        sf = c.S_Push1

        # def MoveObj2(sq: Square, dr: Direction, sf):
        # Try to move object on square x,y that was pushed in dir dx,dy then play sound sf
        # Update terrain under object's initial position (x,y)
        # Also unblock tunnel if Obj blocking tunnel and let other end activate (cx,cy)
        # used by CheckLLoc and IceMoveO
        item = self.items[sq]  # Get object type

        # Trigger waiting tunnel if vacating a tunnel
        if self.is_tunnel(sq):
            # Unblock tunnel

            # Search for a blocked tunnel with the same ID
            tunnel_waiting_id = c.Tunnel_Set_Waiting[self.terrain[sq]]

            for sqx in SQUARES:
                if (
                        self.terrain[sqx] == tunnel_waiting_id
                        and self.items[sqx] != c.EMPTY
                        and not (sqx == sq)
                ):
                    # We are moving an object through a tunnel
                    # Other end of blocked tunnel had an object so move it through now
                    # Move object through a tunnel (from xy to cx, cy)
                    # Transfer blocked object
                    self.items[sq] = self.items[sqx]
                    self.items[sqx] = c.EMPTY
                    self.terrain[sqx] = c.Tunnel_Set_Not_Waiting[
                        self.terrain[sqx]
                    ]
                    break
            else:
                # Did not find another end of this tunnel with an object on
                # Not Blocked Anymore
                self.items[sq] = c.EMPTY
                self.terrain[sq] = c.Tunnel_Set_Not_Waiting[
                    self.terrain[sq]
                ]

                # We didn't find a match so maybe the tank is it
                if (
                        self.terrain[self.tank.sq]
                        == c.Tunnel_Set_Not_Waiting[tunnel_waiting_id]
                ) and self.tank.on_waiting_tunnel:
                    self.score_moves -= 1
                    self.UpDateTankPos(STATIONARY)
                    self.PopUndo()
        else:
            self.items[sq] = c.EMPTY

        # Now update destination
        dest = sq.relative(dr)

        # If destination is a tunnel then set x,y to tunnel's exit
        if self.is_tunnel(dest):
            tunnel_exit = self.find_tunnel_exit(dest)
            if tunnel_exit is None:
                return  # The tunnel was a black hole
            elif tunnel_exit == dest:
                self.terrain[dest] = c.Tunnel_Set_Waiting[self.terrain[dest]]
            else:
                dest = tunnel_exit

        if self.terrain[dest] != c.WATER:
            # Move object to destination square
            self.items[dest] = item
        else:
            # Destination square is water
            sf = c.S_Sink
            if item == c.BLOCK:
                self.items[dest] = c.EMPTY
                self.terrain[dest] = c.BRIDGE
        self.SoundPlay(sf)

        # MoveObj2(sq, dr, c.S_Push1)
        if self.is_ice(destination):
            self.sliding_items[destination] = dr

        return True

    def AntiTank(self):
        self.change_log.append("AntiTank Move")
        # Look for antitanks on same row/col as tank and let them fire (only if laser not already existing)
        # Order: Right, left, down, above from Tank

        # Only one laser on board so returns if laser exists
        if self.laser_live:
            return

        # Tank on an item is hidden from AntiTanks
        if not self.is_tank_on_terrain():
            return

        # def find_next_object(direction: Direction):
        #     sq = self.tank.sq
        #     while self.is_on_board_and_empty(sq := sq.relative(direction)):
        #         pass
        #     return sq

        for scan_dir, antitank, shoot_dir in [
            (RIGHT, c.ANTITANK_LEFT, LEFT),
            (LEFT, c.ANTITANK_RIGHT, RIGHT),
            (DOWN, c.ANTITANK_UP, UP),
            (UP, c.ANTITANK_DOWN, DOWN),
        ]:
            sq = self.tank.sq
            while self.is_on_board_and_empty(sq := sq.relative(scan_dir)):
                pass
            if sq is not None and (self.items[sq] == antitank):
                self.FireLaser(sq, shoot_dir, False)
                break

        # s = find_next_object(RIGHT)
        # if s is not None and (self.items[s] == c.ANTITANK_LEFT):
        #     self.FireLaser(s, LEFT, False)
        #     return
        #
        # s = find_next_object(LEFT)
        # if s is not None and (self.items[s] == c.ANTITANK_RIGHT):
        #     self.FireLaser(s, RIGHT, False)
        #     return
        #
        # s = find_next_object(DOWN)
        # if s is not None and (self.items[s] == c.ANTITANK_UP):
        #     self.FireLaser(s, UP, False)
        #     return
        #
        # s = find_next_object(UP)
        # if s is not None and (self.items[s] == c.ANTITANK_DOWN):
        #     self.FireLaser(s, DOWN, False)
        #     return

    def FireLaser(self, sq, dr, is_player_tank):

        self.laser_live = True

        self.laser.dir_front = dr
        self.laser.dir_back = dr
        self.laser.sq = sq

        if is_player_tank:
            self.laser.colour = c.LaserColorG
            self.SoundPlay(c.S_Fire)
        else:
            self.laser.colour = c.LaserColorR
            self.SoundPlay(c.S_Anti2)
        self.MoveLaser()

    def UpdateUndo(self):
        # Should be done whenever player moves or shoots
        # TODO
        # self.undo_state.append(self.deepcopy())
        pass

    def PopUndo(self):
        # Remove an undo when tank moving through a tunnel
        # TODO
        pass

    def MoveTank(self, d: Direction):
        if self.tank.direction != d:
            # Tank is turning
            self.tank.direction = d
            self.SoundPlay(c.S_Turn)
        else:
            destination = self.tank.sq.relative(d)
            if self.is_on_board_and_empty(destination):
                self.UpDateTankPos(d)
                if self.is_ice(destination):
                    self.tank.sliding_sq = self.tank.sq
                    self.tank.is_sliding = True
            else:
                self.SoundPlay(c.S_Head)  # Bumping into something
            self.tank.sliding_dr = d

    def MoveLaser(self):
        self.change_log.append("Laser moving")

        if not self.running:
            return

        LaserBounceOnIce = True
        while LaserBounceOnIce:
            LaserBounceOnIce = False

            dr = self.laser.dir_front

            self.laser.dir_back = self.laser.dir_front

            # def CheckLLoc(self, sq: Square, dr: Direction):
            laser_still_live = False
            sq = self.laser.sq.relative(dr)

            if sq is None:
                # Laser out of board
                laser_still_live = False
            elif sq == self.tank.sq:
                # Hit tank
                self.game_over(victorious=False)
                laser_still_live = False
            else:
                # self.wasIce = False
                # destination = sq.relative(dr)

                item_loc = self.items[sq]
                if item_loc == c.EMPTY:
                    laser_still_live = True
                elif item_loc in c.DEADANTITANK_ALL:  # Include dead tanks as solid items
                    self.SoundPlay(c.S_LaserHit)
                    self.sliding_items.pop(sq, None)

                elif item_loc == c.SOLID:
                    self.SoundPlay(c.S_LaserHit)

                elif item_loc == c.BLOCK:
                    # Can block be moved in direction of laser? Is square free
                    if not self.check_loc_move_start_sliding(sq, dr):
                        self.SoundPlay(c.S_LaserHit)

                elif item_loc == c.WALL:
                    self.items[sq] = c.EMPTY  # Destroy wall with laser
                    self.SoundPlay(c.S_Bricks)

                elif item_loc == c.ANTITANK_UP:
                    if dr == DOWN:  # Laser hit front of antitank
                        # Kill Atank
                        self.items[sq] = c.DEADANTITANK_UP
                        self.SoundPlay(c.S_Anti1)
                        laser_still_live = False
                    elif not self.check_loc_move_start_sliding(sq, dr):
                        self.SoundPlay(c.S_LaserHit)
                elif item_loc == c.ANTITANK_RIGHT:
                    if dr == LEFT:
                        self.items[sq] = c.DEADANTITANK_RIGHT
                        self.SoundPlay(c.S_Anti1)
                        laser_still_live = False
                    elif not self.check_loc_move_start_sliding(sq, dr):
                        self.SoundPlay(c.S_LaserHit)
                elif item_loc == c.ANTITANK_DOWN:
                    if dr == UP:
                        self.items[sq] = c.DEADANTITANK_DOWN
                        self.SoundPlay(c.S_Anti1)
                        laser_still_live = False
                    elif not self.check_loc_move_start_sliding(sq, dr):
                        self.SoundPlay(c.S_LaserHit)
                elif item_loc == c.ANTITANK_LEFT:
                    if dr == RIGHT:
                        self.items[sq] = c.DEADANTITANK_LEFT
                        self.SoundPlay(c.S_Anti1)
                        laser_still_live = False
                    elif not self.check_loc_move_start_sliding(sq, dr):
                        self.SoundPlay(c.S_LaserHit)

                elif item_loc == c.MIRROR_LEFT_UP:
                    if self.laser.dir_front == RIGHT or self.laser.dir_front == DOWN:
                        laser_still_live = True
                    elif not self.check_loc_move_start_sliding(sq, dr):
                        self.SoundPlay(c.S_LaserHit)
                elif item_loc == c.MIRROR_UP_RIGHT:
                    if self.laser.dir_front == DOWN or self.laser.dir_front == LEFT:
                        laser_still_live = True
                    elif not self.check_loc_move_start_sliding(sq, dr):
                        self.SoundPlay(c.S_LaserHit)
                elif item_loc == c.MIRROR_RIGHT_DOWN:
                    if self.laser.dir_front == UP or self.laser.dir_front == LEFT:
                        laser_still_live = True
                    elif not self.check_loc_move_start_sliding(sq, dr):
                        self.SoundPlay(c.S_LaserHit)
                elif item_loc == c.MIRROR_DOWN_LEFT:
                    if self.laser.dir_front == UP or self.laser.dir_front == RIGHT:
                        laser_still_live = True
                    elif not self.check_loc_move_start_sliding(sq, dr):
                        self.SoundPlay(c.S_LaserHit)

                elif item_loc == c.GLASS:
                    # In original, this is where glass is set to a glowing sprite
                    laser_still_live = True

                elif item_loc == c.ROTMIRROR_LEFT_UP:
                    if self.laser.dir_front == RIGHT or self.laser.dir_front == DOWN:
                        laser_still_live = True
                    else:
                        self.items[sq] = c.ROTMIRROR_UP_RIGHT
                        self.SoundPlay(c.S_Rotate)
                elif item_loc == c.ROTMIRROR_UP_RIGHT:
                    if self.laser.dir_front == DOWN or self.laser.dir_front == LEFT:
                        laser_still_live = True
                    else:
                        self.items[sq] = c.ROTMIRROR_RIGHT_DOWN
                        self.SoundPlay(c.S_Rotate)
                elif item_loc == c.ROTMIRROR_RIGHT_DOWN:
                    if self.laser.dir_front == UP or self.laser.dir_front == LEFT:
                        laser_still_live = True
                    else:
                        self.items[sq] = c.ROTMIRROR_DOWN_LEFT
                        self.SoundPlay(c.S_Rotate)
                elif item_loc == c.ROTMIRROR_DOWN_LEFT:
                    if self.laser.dir_front == UP or self.laser.dir_front == RIGHT:
                        laser_still_live = True
                    else:
                        self.items[sq] = c.ROTMIRROR_LEFT_UP
                        self.SoundPlay(c.S_Rotate)

            ############################
            # Check destination square and start objects there moving if needed
            if laser_still_live:
                # Laser is still on the board
                # Move laser
                self.laser.sq = self.laser.sq.relative(dr)

                reflecting_item = self.items[self.laser.sq]
                if reflecting_item in c.MIRROR_ALL:
                    # Reflect off mirror

                    # Update laser direction if hitting a mirror
                    if (
                            reflecting_item == c.MIRROR_LEFT_UP
                            or reflecting_item == c.ROTMIRROR_LEFT_UP
                    ):
                        if self.laser.dir_front == RIGHT:
                            self.laser.dir_front = UP
                        else:
                            self.laser.dir_front = LEFT
                    elif (
                            reflecting_item == c.MIRROR_UP_RIGHT
                            or reflecting_item == c.ROTMIRROR_UP_RIGHT
                    ):
                        if self.laser.dir_front == DOWN:
                            self.laser.dir_front = RIGHT
                        else:
                            self.laser.dir_front = UP
                    elif (
                            reflecting_item == c.MIRROR_RIGHT_DOWN
                            or reflecting_item == c.ROTMIRROR_RIGHT_DOWN
                    ):
                        if self.laser.dir_front == UP:
                            self.laser.dir_front = RIGHT
                        else:
                            self.laser.dir_front = DOWN
                    elif (
                            reflecting_item == c.MIRROR_DOWN_LEFT
                            or reflecting_item == c.ROTMIRROR_DOWN_LEFT
                    ):
                        if self.laser.dir_front == UP:
                            self.laser.dir_front = LEFT
                        else:
                            self.laser.dir_front = DOWN

                    # UpdateLaserBounce() updates the LaserBounceOnIce
                    # Allows a second laser movement if laser is contacting a sliding mirror
                    if self.laser.sq in self.sliding_items:
                        LaserBounceOnIce = True

                    self.SoundPlay(c.S_Deflb)
                # self.laser.Firing = True
            else:
                # Laser is off the board / hit something solid
                self.laser_live = False

                # Antitank Turn
                self.AntiTank()

                def TestIfConvCanMoveTank():
                    # Used to handle a bug :  the speed bug
                    # Return True if the tank is on Conveyor and can move.
                    terrain_tank_on = self.terrain[self.tank.sq]
                    if self.is_tank_on_terrain():
                        if terrain_tank_on == c.CONVEYOR_UP:
                            if self.is_on_board_and_empty(self.tank.sq.relative(UP)):
                                return True
                        elif terrain_tank_on == c.CONVEYOR_RIGHT:
                            if self.is_on_board_and_empty(self.tank.sq.relative(RIGHT)):
                                return True
                        elif terrain_tank_on == c.CONVEYOR_DOWN:
                            if self.is_on_board_and_empty(self.tank.sq.relative(DOWN)):
                                return True
                        elif terrain_tank_on == c.CONVEYOR_LEFT:
                            if self.is_on_board_and_empty(self.tank.sq.relative(LEFT)):
                                return True
                    return False

                if TestIfConvCanMoveTank():
                    self.tank_moving_on_conveyor = True
        # loops here if LaserBounceOnIce was set in the loop

    def is_tunnel(self, sq):
        return self.terrain[sq] in c.TUNNEL_ALL

    def UpDateTankPos(self, dr):
        self.change_log.append("Tank position updated")
        self.SoundPlay(c.S_Move)
        self.UpdateUndo()

        self.score_moves += 1

        self.tank.sq = self.tank.sq.relative(dr)
        self.tank.on_waiting_tunnel = False  # Flag required for if we move off a tunnel
        if self.is_tunnel(self.tank.sq):
            tunnel_exit = self.find_tunnel_exit(self.tank.sq)
            if tunnel_exit is None:
                # Tank fell in a black hole
                self.game_over(victorious=False)
                return
            elif tunnel_exit == self.tank.sq:
                # Blocked exit found
                self.tank.on_waiting_tunnel = True
            else:
                self.tank.sq = tunnel_exit

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

        tunnel_id = self.terrain[sq]

        found_blocked_exit = False

        # Find an empty destination tunnel
        for sqx in SQUARES:
            if self.terrain[sqx] == tunnel_id and not sqx == sq:
                # Found an exit tunnel (and not the same as entry)
                if self.items[sqx] != c.EMPTY:
                    # Exit is blocked
                    found_blocked_exit = True
                else:
                    return sqx

        if found_blocked_exit:
            return sq
        else:
            # No exit found, so Tunnel is a Black Hole
            return None

    def MoveObj(self, sq: Square, dr: Direction, sf):
        # Try to move object on square x,y that was pushed in dir dx,dy then play sound sf
        # Update terrain under object's initial position (x,y)
        # Also unblock tunnel if Obj blocking tunnel and let other end activate (cx,cy)
        # used by CheckLLoc and IceMoveO
        item = self.items[sq]  # Get object type

        # Trigger waiting tunnel if vacating a tunnel
        if self.is_tunnel(sq):
            # Unblock tunnel

            # Search for a blocked tunnel with the same ID
            tunnel_waiting_id = c.Tunnel_Set_Waiting[self.terrain[sq]]

            for sqx in SQUARES:
                if (
                        self.terrain[sqx] == tunnel_waiting_id
                        and self.items[sqx] != c.EMPTY
                        and not (sqx == sq)
                ):
                    # We are moving an object through a tunnel
                    # Other end of blocked tunnel had an object so move it through now
                    # Move object through a tunnel (from xy to cx, cy)
                    # Transfer blocked object
                    self.items[sq] = self.items[sqx]
                    self.items[sqx] = c.EMPTY
                    self.terrain[sqx] = c.Tunnel_Set_Not_Waiting[
                        self.terrain[sqx]
                    ]
                    break
            else:
                # Did not find another end of this tunnel with an object on
                # Not Blocked Anymore
                self.items[sq] = c.EMPTY
                self.terrain[sq] = c.Tunnel_Set_Not_Waiting[
                    self.terrain[sq]
                ]

                # We didn't find a match so maybe the tank is it
                if (
                        self.terrain[self.tank.sq]
                        == c.Tunnel_Set_Not_Waiting[tunnel_waiting_id]
                ) and self.tank.on_waiting_tunnel:
                    self.score_moves -= 1
                    self.UpDateTankPos(STATIONARY)
                    self.PopUndo()
        else:
            self.items[sq] = c.EMPTY

        # Now update destination
        dest = sq.relative(dr)

        # If destination is a tunnel then set x,y to tunnel's exit
        if self.is_tunnel(dest):
            tunnel_exit = self.find_tunnel_exit(dest)
            if tunnel_exit is None:
                return  # The tunnel was a black hole
            elif tunnel_exit == dest:
                self.terrain[dest] = c.Tunnel_Set_Waiting[self.terrain[dest]]
            else:
                dest = tunnel_exit

        if self.terrain[dest] != c.WATER:
            # Move object to destination square
            self.items[dest] = item
        else:
            # Destination square is water
            sf = c.S_Sink
            if item == c.BLOCK:
                self.items[dest] = c.EMPTY
                self.terrain[dest] = c.BRIDGE
        self.SoundPlay(sf)

    # def CheckLLoc(self, sq: Square, dr: Direction):
    #     # Check destination square of laser, and start objects there moving if needed
    #     #  this is were the laser does its damage
    #     # returns true if laser didn't hit anything and still in board
    #
    #     if sq is None:
    #         # Laser out of board
    #         return False
    #
    #     if sq == self.tank.sq:
    #         # Hit tank
    #         self.game_over(victorious=False)
    #         return False
    #
    #     # self.wasIce = False
    #     # destination = sq.relative(dr)
    #
    #     item_loc = self.items[sq]
    #     if item_loc == c.EMPTY:
    #         return True
    #     elif item_loc in c.DEADANTITANK_ALL:  # Include dead tanks as solid items
    #         self.SoundPlay(c.S_LaserHit)
    #         self.sliding_items.pop(sq, None)
    #
    #     elif item_loc == c.SOLID:
    #         self.SoundPlay(c.S_LaserHit)
    #
    #     elif item_loc == c.BLOCK:
    #         # Can block be moved in direction of laser? Is square free
    #         if not self.check_loc_move_start_sliding(sq, dr):
    #             self.SoundPlay(c.S_LaserHit)
    #
    #     elif item_loc == c.WALL:
    #         self.items[sq] = c.EMPTY  # Destroy wall with laser
    #         self.SoundPlay(c.S_Bricks)
    #
    #     elif item_loc == c.ANTITANK_UP:
    #         if dr == DOWN:  # Laser hit front of antitank
    #             # Kill Atank
    #             self.items[sq] = c.DEADANTITANK_UP
    #             self.SoundPlay(c.S_Anti1)
    #             return False
    #         elif not self.check_loc_move_start_sliding(sq, dr):
    #             self.SoundPlay(c.S_LaserHit)
    #     elif item_loc == c.ANTITANK_RIGHT:
    #         if dr == LEFT:
    #             self.items[sq] = c.DEADANTITANK_RIGHT
    #             self.SoundPlay(c.S_Anti1)
    #             return False
    #         elif not self.check_loc_move_start_sliding(sq, dr):
    #             self.SoundPlay(c.S_LaserHit)
    #     elif item_loc == c.ANTITANK_DOWN:
    #         if dr == UP:
    #             self.items[sq] = c.DEADANTITANK_DOWN
    #             self.SoundPlay(c.S_Anti1)
    #             return False
    #         elif not self.check_loc_move_start_sliding(sq, dr):
    #             self.SoundPlay(c.S_LaserHit)
    #     elif item_loc == c.ANTITANK_LEFT:
    #         if dr == RIGHT:
    #             self.items[sq] = c.DEADANTITANK_LEFT
    #             self.SoundPlay(c.S_Anti1)
    #             return False
    #         elif not self.check_loc_move_start_sliding(sq, dr):
    #             self.SoundPlay(c.S_LaserHit)
    #
    #     elif item_loc == c.MIRROR_LEFT_UP:
    #         if self.laser.dir_front == RIGHT or self.laser.dir_front == DOWN:
    #             return True
    #         if not self.check_loc_move_start_sliding(sq, dr):
    #             self.SoundPlay(c.S_LaserHit)
    #     elif item_loc == c.MIRROR_UP_RIGHT:
    #         if self.laser.dir_front == DOWN or self.laser.dir_front == LEFT:
    #             return True
    #         if not self.check_loc_move_start_sliding(sq, dr):
    #             self.SoundPlay(c.S_LaserHit)
    #     elif item_loc == c.MIRROR_RIGHT_DOWN:
    #         if self.laser.dir_front == UP or self.laser.dir_front == LEFT:
    #             return True
    #         if not self.check_loc_move_start_sliding(sq, dr):
    #             self.SoundPlay(c.S_LaserHit)
    #     elif item_loc == c.MIRROR_DOWN_LEFT:
    #         if self.laser.dir_front == UP or self.laser.dir_front == RIGHT:
    #             return True
    #         if not self.check_loc_move_start_sliding(sq, dr):
    #             self.SoundPlay(c.S_LaserHit)
    #
    #     elif item_loc == c.GLASS:
    #         # In original, this is where glass is set to a glowing sprite
    #         return True
    #
    #     elif item_loc == c.ROTMIRROR_LEFT_UP:
    #         if self.laser.dir_front == RIGHT or self.laser.dir_front == DOWN:
    #             return True
    #         self.items[sq] = c.ROTMIRROR_UP_RIGHT
    #         self.SoundPlay(c.S_Rotate)
    #     elif item_loc == c.ROTMIRROR_UP_RIGHT:
    #         if self.laser.dir_front == DOWN or self.laser.dir_front == LEFT:
    #             return True
    #         self.items[sq] = c.ROTMIRROR_RIGHT_DOWN
    #         self.SoundPlay(c.S_Rotate)
    #     elif item_loc == c.ROTMIRROR_RIGHT_DOWN:
    #         if self.laser.dir_front == UP or self.laser.dir_front == LEFT:
    #             return True
    #         self.items[sq] = c.ROTMIRROR_DOWN_LEFT
    #         self.SoundPlay(c.S_Rotate)
    #     elif item_loc == c.ROTMIRROR_DOWN_LEFT:
    #         if self.laser.dir_front == UP or self.laser.dir_front == RIGHT:
    #             return True
    #         self.items[sq] = c.ROTMIRROR_LEFT_UP
    #         self.SoundPlay(c.S_Rotate)
    #
    #     # # Stop it sliding if it is on the sliding_items list
    #     # self.sliding_items.pop(sq, None)
    #     #
    #     # # If object is moving into an ice square then add it to the Sliding stack
    #     # if self.wasIce:  # self.is_ice(destination):
    #     #     self.sliding_items[destination] = dr
    #
    #     return False

    # def IceMoveO(self):
    #     self.change_log.append("Slid object on ice")
    #     # Move an item on the ice
    #     for sliding_item_sq, sliding_item_dr in reversed(list(self.sliding_items.items())):
    #         if self.terrain[sliding_item_sq] == c.THINICE:
    #             # Sliding off thin ice so melt the ice into water
    #             self.terrain[sliding_item_sq] = c.WATER
    #
    #         # if destination is empty (not item and not tank)
    #         # note: CheckLoc also sets wasIce to True is destination is Ice or ThinIce
    #         destination = sliding_item_sq.relative(sliding_item_dr)
    #         if self.CheckLoc(destination) and not destination == self.tank.sq:
    #             savei = self.is_ice(destination)
    #             self.MoveObj(sliding_item_sq, sliding_item_dr, c.S_Push2)
    #             self.AntiTank()
    #             if not savei:
    #                 del self.sliding_items[sliding_item_sq]
    #             else:
    #                 # Update position of tracked sliding object
    #                 # Insert destination item at the position of the original
    #                 new_list = {}
    #                 for s, d in self.sliding_items.items():
    #                     if s == sliding_item_sq:
    #                         new_list[destination] = d
    #                     else:
    #                         new_list[s] = d
    #                 new_list[destination] = sliding_item_dr
    #                 self.sliding_items = new_list
    #         else:
    #             if self.terrain[sliding_item_sq] == c.WATER:
    #                 # Drop into water if ice melted and item couldn't move
    #                 self.MoveObj(sliding_item_sq, STATIONARY, c.S_Sink)
    #             del self.sliding_items[sliding_item_sq]
    #             self.AntiTank()

    # def IceMoveT(self):
    #     self.change_log.append("Slid tank on ice")
    #     #  Move the tank on the Ice
    #     if self.terrain[self.tank.sliding_sq] == c.THINICE:
    #         self.terrain[self.tank.sliding_sq] = c.WATER
    #
    #     destination = self.tank.sliding_sq.relative(self.tank.sliding_dr)
    #     if self.CheckLoc(destination):
    #         savei = self.is_ice(destination)
    #         self.ConvMoveTank(self.tank.sliding_dr, False)
    #         # Move tank an additional square
    #         self.tank.sliding_sq = self.tank.sliding_sq.relative(self.tank.sliding_dr)
    #         if not savei:
    #             self.tank_sliding_data.live = False
    #     else:
    #         self.tank_sliding_data.live = False


class Graphics:
    GAMEBOARD_OFFSET_X_PX = 17  # XOffset
    GAMEBOARD_OFFSET_Y_PX = 17  # YOffset
    SPRITE_SIZE = 32  # SpBm_Width, SpBm_Height
    SPRITE_SHEET_ROWS = 6
    SPRITE_SHEET_COLUMNS = 10
    DISPLAY_SIZE = (
        GAMEBOARD_OFFSET_X_PX * 2 + SPRITE_SIZE * 16,
        GAMEBOARD_OFFSET_Y_PX * 2 + SPRITE_SIZE * 16,
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
    BLACK = pygame.Color(0x000000FF)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=self.DISPLAY_SIZE, flags=0)
        self.spritesheet = pygame.image.load(DEFAULT_SPRITESHEET_LOC).convert_alpha()
        self.animation_counter = 0

    def _increment_animation_counter(self):
        self.animation_counter = (self.animation_counter + 1) % 3

    def draw_board(self, game: GameState):
        for sq in SQUARES:
            self._draw_sprite(game.terrain[sq], sq)
            self._draw_sprite(game.items[sq], sq)
        self._draw_tank(game.tank.sq, game.tank.direction)
        if game.laser_live:
            self._draw_laser(game.laser)
        pygame.display.update()
        self._increment_animation_counter()

    def _draw_sprite(self, entity_id, square: Square):
        board_location = (
            self.GAMEBOARD_OFFSET_X_PX + (square.x * self.SPRITE_SIZE),
            self.GAMEBOARD_OFFSET_Y_PX + (square.y * self.SPRITE_SIZE),
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
            self.GAMEBOARD_OFFSET_X_PX + (square.x * self.SPRITE_SIZE),
            self.GAMEBOARD_OFFSET_Y_PX + (square.y * self.SPRITE_SIZE),
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
        x = self.GAMEBOARD_OFFSET_X_PX + (laser.sq.x * self.SPRITE_SIZE)
        y = self.GAMEBOARD_OFFSET_Y_PX + (laser.sq.y * self.SPRITE_SIZE)
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
            pygame.draw.rect(self.screen, self.BLACK, beam, 3)
            pygame.draw.rect(self.screen, colour, beam)
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
    def draw_interesting_crop(game: GameState):
        x_min = y_min = c.PLAYFIELD_SIZE
        x_max = y_max = 0
        for sq in SQUARES:
            if (
                    game.terrain[sq] not in (c.GRASS, c.WATER)
                    or game.items[sq] != c.EMPTY
                    or game.tank.sq == sq
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
    def cell_as_numbers(game: GameState, sq: Square):
        terrain = game.terrain[sq]
        item = game.items[sq]
        if terrain == c.GRASS:
            terrain = " "
        if item == c.EMPTY:
            item = " "
        if game.tank.sq == sq:
            item = "T"
        if game.laser_live and game.laser.sq == sq:
            terrain = "-"

        return f"{terrain: >2}{item: >3}"


def load_level(filename, level_number):
    game = GameState()
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


def execute_playback(inputs: list, game: GameState):
    game.queue_new_inputs(inputs)
    while game.running and not game.is_inputs_queued():
        game.tick()
    if game.reached_flag:
        return "WIN"
    elif game.player_dead:
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
        print(f"Actions: {game.change_log}")
        print(f"Sliding: {game.sliding_items}")
        print("Board:")
        txtgrphcs.draw_interesting_crop(game)
        game.queue_new_inputs(inputs.wait_for_anykey())

    # Initial State
    display()

    while game.running and timeout_counter < 500:

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

    print(f"End State: {game.reached_flag}")
    # game.queue_new_inputs(inputs.wait_for_anykey())


if __name__ == "__main__":
    debug_level("standard_levels/LaserTank", 2)
