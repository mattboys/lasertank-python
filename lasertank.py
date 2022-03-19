import struct

import pygame
import pygame.locals

import constants as c

BOARDSIZE = 16  # Playfield is 16x16 grid

DEFAULT_LEVEL_LOC = "./resources/LaserTank.lvl"
DEFAULT_SPRITESHEET_LOC = "./resources/spritesheet.png"
DEFAULT_LPB_LOC = "./resources/LaserTank_0001.lpb"


class TankRec:
    def __init__(self, x, y, direction):
        self.X = x
        self.Y = y
        self.Dir = direction
        self.Firing = False  # Is laser on the board, move to board object?
        self.on_waiting_tunnel = False  # Indicates that tank is on a waiting tunnel


class LaserRec:
    def __init__(self):
        self.X = 5
        self.Y = 10
        self.Dir = c.D_UP
        # self.Firing = False  # Used only to update sprites
        self.Good = False
        # Other laser-related fields
        self.oDir = c.D_LEFT
        self.LaserColor = c.LaserColorR
        self.LaserBounceOnIce = False  # If laser bouncing off sliding mirror
        self.ConvMoving = False


class LevelInfo:
    def __init__(self):
        self.name = ""
        self.number = 1


class TIceRec:  # Sliding Struct
    def __init__(
            self,
            x,
            y,
            dx,
            dy,
            s=True,
    ):
        self.x = x  # Last XY position of object to move
        self.y = y
        self.dx = dx  # Direction to move in Delta Cords
        self.dy = dy
        self.s = s  # True if sliding


class GameState:
    def __init__(self):
        self.change_log = []
        self.terrain = [[c.GRASS for _ in range(BOARDSIZE)] for _2 in range(BOARDSIZE)]
        self.items = [[c.EMPTY for _ in range(BOARDSIZE)] for _2 in range(BOARDSIZE)]
        self.tank = TankRec(x=7, y=15, direction=c.D_UP)
        self.laser = LaserRec()
        self.sliding_items = []  # SlideMem is list of TIceRec structs
        self.moves_history = []
        self.moves_buffer = []  # RecBuffer
        self.score_shots = 0
        self.score_moves = 0
        self.undo_state = []
        self.sounds_buffer = []
        self.info = {
            "number": 1,
            "title": "",
            "hint": "",
            "author": "",
            "difficulty": "",
        }

        # Control flags
        self.running = True
        self.reached_flag = False
        self.player_dead = False

        # Flags
        self.tank_moving_on_conveyor = False
        self.tank_sliding_data = TIceRec(
            0, 0, 0, 0, False
        )  # Momentum of tank where SlideT.s = is tank sliding?
        # self.previous_tunnel_waiting = False  # Found tunnel output on PF2 (under something)
        # self.previous_tunnel_blackhole = (
        #     False  # True if we TunnleTranslae to a Black Hole (no exit found)
        # )
        self.wasIce = False

    def is_objects_sliding(self):
        # Was named SlideO_s
        # Is anything sliding?
        return len(self.sliding_items) > 0

    def is_inputs_queued(self):
        """Are there player moves waiting in the buffer to be played?"""
        return len(self.moves_buffer) > 0

    def load_level(self, level_number, filename=DEFAULT_LEVEL_LOC):
        self.sliding_items = []
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
        self.info = {
            "number": level_number,
            "title": title,
            "hint": hint,
            "author": author,
            "difficulty": difficulty,
        }

        for x in range(BOARDSIZE):
            for y in range(BOARDSIZE):
                # Note that lvl files are saved in columns and playfield is in [x][y]
                i = int(playfield_ints[y + x * BOARDSIZE])
                terrain, item = c.DECODE_TABLE.get(i, (c.GRASS, c.EMPTY))
                # Tank is not placed in the items array
                if item == c.TANK:
                    self.tank = TankRec(x=x, y=y, direction=c.D_UP)
                else:
                    self.items[x][y] = item
                self.terrain[x][y] = terrain

    def queue_new_inputs(self, new_inputs):
        self.moves_buffer.extend(new_inputs)

    def tick(self):
        # TODO: handle an undo to avoid inf loop
        self.change_log = []

        # Main game loop (see C-3043)
        if self.tank.Firing:
            self.MoveLaser()

        # Process keyboard buffer
        if self.moves_buffer and not (
                self.tank.Firing
                or self.tank_moving_on_conveyor
                or self.is_objects_sliding()
                or self.tank_sliding_data.s
        ):
            move = self.moves_buffer.pop(0)
            self.change_log.append(f"Popped movement {move}")
            if move == c.K_UP:
                self.MoveTank(c.D_UP)
            elif move == c.K_RIGHT:
                self.MoveTank(c.D_RIGHT)
            elif move == c.K_DOWN:
                self.MoveTank(c.D_DOWN)
            elif move == c.K_LEFT:
                self.MoveTank(c.D_LEFT)
            elif move == c.K_SHOOT:
                self.UpdateUndo()
                self.score_shots += 1
                self.FireLaser(
                    self.tank.X, self.tank.Y, self.tank.Dir, True
                )
            self.AntiTank()

        self.change_log.append("Resolving momenta")
        # Resolve Momenta
        if self.is_objects_sliding():
            self.IceMoveO()  # NOTE: IceMoveO includes additional AntiTank() moves
        if self.tank_sliding_data.s:
            self.IceMoveT()
        self.tank_moving_on_conveyor = False  # used to disable Laser on the conveyor

        self.change_log.append("Checking tank square")
        if self.is_tank_on_terrain():
            # Check where the tank ended up
            tank_terrain = self.terrain[self.tank.X][self.tank.Y]
            if tank_terrain == c.FLAG:
                self.game_over(victorious=True)
            elif tank_terrain == c.WATER:
                self.game_over(victorious=False)
            elif tank_terrain == c.CONVEYOR_UP:
                if self.CheckLoc(self.tank.X, self.tank.Y - 1):
                    self.ConvMoveTank(0, -1, True)
            elif tank_terrain == c.CONVEYOR_RIGHT:
                if self.CheckLoc(self.tank.X + 1, self.tank.Y):
                    self.ConvMoveTank(1, 0, True)
            elif tank_terrain == c.CONVEYOR_DOWN:
                if self.CheckLoc(self.tank.X, self.tank.Y + 1):
                    self.ConvMoveTank(0, 1, True)
            elif tank_terrain == c.CONVEYOR_LEFT:
                if self.CheckLoc(self.tank.X - 1, self.tank.Y):
                    self.ConvMoveTank(-1, 0, True)

    def is_tank_on_terrain(self):
        """If the tank up on an object from a trick-shot then the tank is not on the terrain"""
        return self.items[self.tank.X][self.tank.Y] == c.EMPTY

    def game_over(self, victorious):
        self.running = False
        # Skipping sound, playback, save recording
        if victorious:
            # self.CheckHighScore()
            self.reached_flag = True
        else:
            self.player_dead = True
        print(f"Game over! {'Win!' if victorious else 'Dead!'}")

    def LoadPlayback(self, filename=DEFAULT_LPB_LOC):
        # C-2574
        # Read off PBRec and Pec
        # TODO
        pass

    def ConvMoveTank(self, x, y, check_ice):
        self.tank.Y += y
        self.tank.X += x

        if self.ISTunnel(self.tank.X, self.tank.Y):
            tunnel_exit = self.find_tunnel_exit(self.tank.X, self.tank.Y)
            if tunnel_exit is None:
                # Tank fell in a black hole
                self.game_over(victorious=False)
                return
            elif tunnel_exit == (self.tank.X, self.tank.Y):
                # Blocked exit found
                self.tank.on_waiting_tunnel = True
            else:
                self.tank.X, self.tank.Y = tunnel_exit

        self.tank_moving_on_conveyor = True
        if self.wasIce and check_ice:
            self.tank_sliding_data.x = self.tank.X
            self.tank_sliding_data.y = self.tank.Y
            self.tank_sliding_data.s = True
            self.tank_sliding_data.dx = x
            self.tank_sliding_data.dy = y
        self.AntiTank()

    def CheckLoc(self, x, y):
        # Sets wasIce to True if the square is ice or thin ice
        # then checks if space can be moved into by tank

        # Check if destination is on the board
        if x < 0 or x > 15 or y < 0 or y > 15:
            return False

        # Set the wasIce flag if tested square is an empty ice or thin ice
        self.wasIce = (
                              self.terrain[x][y] == c.ICE or self.terrain[x][y] == c.THINICE
                      ) and self.items[x][y] == c.EMPTY
        # if self.terrain[x][y] in c.TUNNEL_ALL:
        #     return True

        return self.items[x][y] == c.EMPTY

    def AntiTank(self):
        self.change_log.append("AntiTank Move")
        # Look for antitanks on same row/col as tank and let them fire (only if laser not already existing)
        # Order: Right, left, down, above from Tank

        # Only one laser on board so returns if laser exists
        if self.tank.Firing:
            return

        x = self.tank.X  # Look to the right
        while self.CheckLoc(x, self.tank.Y):
            x += 1
        if (
                (x < c.PLAYFIELD_SIZE)
                and (self.items[x][self.tank.Y] == c.ANTITANK_LEFT)
                and (self.tank.X != x)
        ):
            self.FireLaser(x, self.tank.Y, c.D_LEFT, False)
            return

        x = self.tank.X  # Look to the left
        while self.CheckLoc(x, self.tank.Y):
            x -= 1
        if (
                (x >= 0)
                and (self.items[x][self.tank.Y] == c.ANTITANK_RIGHT)
                and (self.tank.X != x)
        ):
            self.FireLaser(x, self.tank.Y, c.D_RIGHT, False)
            return

        y = self.tank.Y  # Look Down
        while self.CheckLoc(self.tank.X, y):
            y += 1
        if (
                (y < c.PLAYFIELD_SIZE)
                and (self.items[self.tank.X][y] == c.ANTITANK_UP)
                and (self.tank.Y != y)
        ):
            self.FireLaser(self.tank.X, y, c.D_UP, False)
            return

        y = self.tank.Y  # Look Up
        while self.CheckLoc(self.tank.X, y):
            y -= 1
        if (
                (y >= 0)
                and (self.items[self.tank.X][y] == c.ANTITANK_DOWN)
                and (self.tank.Y != y)
        ):
            self.FireLaser(self.tank.X, y, c.D_DOWN, False)
            return

    def FireLaser(self, x, y, d, is_player_tank):

        self.tank.Firing = True

        self.laser.Dir = d
        self.laser.oDir = d
        self.laser.X = x
        self.laser.Y = y
        # self.laser.Firing = False  # True if laser has been moved. Used only to update sprited
        self.laser.Good = is_player_tank

        if is_player_tank:
            self.SoundPlay(c.S_Fire)
        else:
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

    def MoveTank(self, d):
        if self.tank.Dir != d:
            # Tank is turning
            self.tank.Dir = d
            self.SoundPlay(c.S_Turn)
            return

        if d == c.D_UP:
            if self.CheckLoc(self.tank.X, self.tank.Y - 1):
                self.UpDateTankPos(0, -1)
            else:
                self.SoundPlay(c.S_Head)  # Bumpping into something
            self.tank_sliding_data.dy = -1
            self.tank_sliding_data.dx = 0
        elif d == c.D_RIGHT:
            if self.CheckLoc(self.tank.X + 1, self.tank.Y):
                self.UpDateTankPos(1, 0)
            else:
                self.SoundPlay(c.S_Head)
            self.tank_sliding_data.dy = 0
            self.tank_sliding_data.dx = 1
        elif d == c.D_DOWN:
            if self.CheckLoc(self.tank.X, self.tank.Y + 1):
                self.UpDateTankPos(0, 1)
            else:
                self.SoundPlay(c.S_Head)
            self.tank_sliding_data.dy = 1
            self.tank_sliding_data.dx = 0
        elif d == c.D_LEFT:
            if self.CheckLoc(self.tank.X - 1, self.tank.Y):
                self.UpDateTankPos(-1, 0)
            else:
                self.SoundPlay(c.S_Head)
            self.tank_sliding_data.dy = 0
            self.tank_sliding_data.dx = -1

        if self.wasIce:
            self.tank_sliding_data.x = self.tank.X
            self.tank_sliding_data.y = self.tank.Y
            self.tank_sliding_data.s = True

    def MoveLaser(self):
        self.change_log.append("Laser moving")

        if not self.running:
            return

        LaserBounceOnIce = True
        while LaserBounceOnIce:
            LaserBounceOnIce = False

            x = 0
            y = 0
            if self.laser.Dir == c.D_UP:
                y = -1
            elif self.laser.Dir == c.D_RIGHT:
                x = +1
            elif self.laser.Dir == c.D_DOWN:
                y = +1
            elif self.laser.Dir == c.D_LEFT:
                x = -1

            self.laser.oDir = self.laser.Dir

            # Check destination square and start objects there moving if needed
            if self.CheckLLoc(self.laser.X + x, self.laser.Y + y, x, y):
                # Laser is still on the board
                self.laser.Y += y
                self.laser.X += x

                reflecting_item = self.items[self.laser.X][
                    self.laser.Y
                ]
                if reflecting_item in c.MIRROR_ALL:
                    # Reflect off mirror

                    # Update laser direction if hitting a mirror
                    if (
                            reflecting_item == c.MIRROR_LEFT_UP
                            or reflecting_item == c.ROTMIRROR_LEFT_UP
                    ):
                        if self.laser.Dir == c.D_RIGHT:
                            self.laser.Dir = c.D_UP
                        else:
                            self.laser.Dir = c.D_LEFT
                    elif (
                            reflecting_item == c.MIRROR_UP_RIGHT
                            or reflecting_item == c.ROTMIRROR_UP_RIGHT
                    ):
                        if self.laser.Dir == c.D_DOWN:
                            self.laser.Dir = c.D_RIGHT
                        else:
                            self.laser.Dir = c.D_UP
                    elif (
                            reflecting_item == c.MIRROR_RIGHT_DOWN
                            or reflecting_item == c.ROTMIRROR_RIGHT_DOWN
                    ):
                        if self.laser.Dir == c.D_UP:
                            self.laser.Dir = c.D_RIGHT
                        else:
                            self.laser.Dir = c.D_DOWN
                    elif (
                            reflecting_item == c.MIRROR_DOWN_LEFT
                            or reflecting_item == c.ROTMIRROR_DOWN_LEFT
                    ):
                        if self.laser.Dir == c.D_UP:
                            self.laser.Dir = c.D_LEFT
                        else:
                            self.laser.Dir = c.D_DOWN

                    # UpdateLaserBounce() updates the LaserBounceOnIce
                    # Allows a second laser movement if laser is contacting a sliding mirror
                    for sliding_item in self.sliding_items:
                        if (
                                sliding_item.s
                                and sliding_item.x == self.laser.X
                                and sliding_item.y == self.laser.Y
                        ):
                            LaserBounceOnIce = True

                    self.SoundPlay(c.S_Deflb)
                # self.laser.Firing = True
            else:
                # Laser is off the board / hit something solid
                self.tank.Firing = False

                # Antitank Turn
                self.AntiTank()

                def TestIfConvCanMoveTank():
                    # Used to handle a bug :  the speed bug
                    # Return True if the tank is on Conveyor and can move.
                    terrain_tank_on = self.terrain[self.tank.X][
                        self.tank.Y
                    ]
                    if self.is_tank_on_terrain():
                        if terrain_tank_on == c.CONVEYOR_UP:
                            if self.CheckLoc(self.tank.X, self.tank.Y - 1):
                                return True
                        elif terrain_tank_on == c.CONVEYOR_RIGHT:
                            if self.CheckLoc(self.tank.X + 1, self.tank.Y):
                                return True
                        elif terrain_tank_on == c.CONVEYOR_DOWN:
                            if self.CheckLoc(self.tank.X, self.tank.Y + 1):
                                return True
                        elif terrain_tank_on == c.CONVEYOR_LEFT:
                            if self.CheckLoc(self.tank.X - 1, self.tank.Y):
                                return True
                    return False

                if TestIfConvCanMoveTank():
                    self.tank_moving_on_conveyor = True
        # loops here if LaserBounceOnIce was set in the loop

    def ISTunnel(self, x, y):
        return self.terrain[x][y] in c.TUNNEL_ALL

    def UpDateTankPos(self, x, y):
        self.change_log.append("Tank position updated")
        self.SoundPlay(c.S_Move)
        self.UpdateUndo()

        self.score_moves += 1

        self.tank.Y += y
        self.tank.X += x
        self.tank.on_waiting_tunnel = False  # Flag required for if we move off a tunnel
        if self.ISTunnel(self.tank.X, self.tank.Y):
            tunnel_exit = self.find_tunnel_exit(self.tank.X, self.tank.Y)
            if tunnel_exit is None:
                # Tank fell in a black hole
                self.game_over(victorious=False)
                return
            elif tunnel_exit == (self.tank.X, self.tank.Y):
                # Blocked exit found
                self.tank.on_waiting_tunnel = True
            else:
                self.tank.X, self.tank.Y = tunnel_exit

    def SoundPlay(self, sound_id):
        self.sounds_buffer.append(sound_id)

    def find_tunnel_exit(self, x, y):
        """ Look for other tunnels that match the one on this square (x,y)
        Return:
            (cx, cy) != x, y if empty exit found
            (x, y) if blocked exit(s) found
            None if black hole (no exits on map)
        """

        tunnel_id = self.terrain[x][y]

        found_blocked_exit = False

        for cy in range(c.PLAYFIELD_SIZE):
            for cx in range(c.PLAYFIELD_SIZE):
                # Find an empty destination tunnel
                if (
                        self.terrain[cx][cy] == tunnel_id
                        and not (x == cx and y == cy)
                ):
                    # Found an exit tunnel (and not the same as entry)
                    if self.items[cx][cy] != c.EMPTY:
                        # Exit is blocked
                        found_blocked_exit = True
                    else:
                        return (cx, cy)

        if found_blocked_exit:
            return (x, y)
        else:
            # No exit found, so Tunnel is a Black Hole
            return None

    def MoveObj(self, x, y, dx, dy, sf):
        self.change_log.append(
            f"MoveObj: Object ({self.items[x][y]}) on {x},{y} requesting to move to {x + dx}"
            f",{y + dy}"
        )
        # Try to move object on square x,y that was pushed in dir dx,dy then play sound sf
        # Update terrain under object's initial position (x,y)
        # Also unblock tunnel if Obj blocking tunnel and let other end activate (cx,cy)
        # used by CheckLLoc and IceMoveO
        obt = self.items[x][y]  # Get object type
        terrain_loc = self.terrain[x][y]

        # Empty the vacating square
        self.change_log.append(
            f"MoveObj: Item is {obt} and vacating terrain is {terrain_loc}"
        )
        # Trigger waiting tunnel if vacating a tunnel
        if terrain_loc in c.TUNNEL_ALL:  # Check if Tunnel
            # Unblock tunnel

            # Search for a blocked tunnel with the same ID
            # signifies that tunnel has an object on it waiting to be transported
            bb = c.Tunnel_Set_Waiting[terrain_loc]

            cx = None
            cy = None
            ok = False
            for cy in range(c.PLAYFIELD_SIZE):
                for cx in range(c.PLAYFIELD_SIZE):
                    if (
                            self.terrain[cx][cy] == bb
                            and self.items[cx][cy] != c.EMPTY
                            and not (x == cx and y == cy)
                    ):
                        # Search for another covered tunnel with the same ID (and not the same square)
                        ok = True
                        break
                if ok:
                    break
            # MoveObj1 goto
            if ok:
                self.change_log.append(f"MoveObj: Found an exit on {cx},{cy}")
                # We are moving an object through a tunnel
                # Other end of blocked tunnel had an object so move it through now
                # Move object through a tunnel (from xy to cx, cy)
                # Transfer blocked object
                self.items[x][y] = self.items[cx][cy]
                self.items[cx][cy] = c.EMPTY
                self.terrain[cx][cy] = c.Tunnel_Set_Not_Waiting[
                    self.terrain[cx][cy]
                ]
            else:
                self.change_log.append(f"MoveObj: Found no exit")
                # Did not find another end of this tunnel with an object on
                # Not Blocked Anymore
                self.items[x][y] = c.EMPTY
                self.terrain[x][y] = c.Tunnel_Set_Not_Waiting[
                    self.terrain[x][y]
                ]

                # We didn't find a match so maybe the tank is it
                if (
                        self.terrain[self.tank.X][self.tank.Y]
                        == c.Tunnel_Set_Not_Waiting[bb]
                ) and self.tank.on_waiting_tunnel:
                    self.score_moves -= 1
                    self.UpDateTankPos(0, 0)
                    self.PopUndo()
        else:
            self.items[x][y] = c.EMPTY

        # Now update destination
        dest_x = x + dx
        dest_y = y + dy

        # If destination is a tunnel then set x,y to tunnel's exit
        if self.ISTunnel(dest_x, dest_y):
            tunnel_exit = self.find_tunnel_exit(dest_x, dest_y)
            if tunnel_exit is None:
                return  # The tunnel was a black hole
            elif tunnel_exit == (dest_x, dest_y):
                self.terrain[dest_x][dest_y] = c.Tunnel_Set_Waiting[self.terrain[dest_x][dest_y]]
            else:
                dest_x, dest_y = tunnel_exit

        if self.terrain[dest_x][dest_y] != c.WATER:
            # Move object to destination square
            self.items[dest_x][dest_y] = obt
        else:
            # Destination square is water
            sf = c.S_Sink
            if obt == c.BLOCK:
                self.items[dest_x][dest_y] = c.EMPTY
                self.terrain[dest_x][dest_y] = c.BRIDGE

    def CheckLLoc(self, x, y, dx, dy):
        def del_SlideO_from_Mem(x, y):
            self.change_log.append("Object stopped sliding")
            # If an object is sliding and is hit by a laser,
            # delete it from stack. (Done before adding new slide direction to stack.)
            for iSlideObj in reversed(self.sliding_items):
                if iSlideObj.x == x and iSlideObj.y == y:
                    iSlideObj.s = False
                    break
            self.sliding_items = [slide for slide in self.sliding_items if slide.s]

        def add_SlideO_to_Mem(sliding_obj):
            self.change_log.append("Object started sliding")
            # Add an object in the stack for slidings objects
            # But, if this object is already in this stack,
            # just change dir and don't increase the counter.
            if len(self.sliding_items) < c.MAX_TICEMEM:
                # Search for square in SlideMem and update if already there
                for count, iSlideObj in enumerate(self.sliding_items):
                    if iSlideObj.x == sliding_obj.x and iSlideObj.y == sliding_obj.y:
                        self.sliding_items[count] = sliding_obj  # TODO: check
                        return
                # Not found so add to SlideMem
                self.sliding_items.append(sliding_obj)
            else:
                print("Debug: Sliding stack full.")

        # Check destination square of laser, and start objects there moving if needed
        #  this is were the laser does its damage
        # returns true if laser didn't hit anything and still in board
        if x not in range(c.PLAYFIELD_SIZE) or y not in range(c.PLAYFIELD_SIZE):
            # Laser out of board
            return False

        if x == self.tank.X and y == self.tank.Y:
            # Hit tank
            self.game_over(victorious=False)
            return False

        self.wasIce = False

        item_loc = self.items[x][y]
        if item_loc == c.EMPTY:
            return True
        elif item_loc in c.SOLID_ITEMS:  # Include dead tanks as solid items
            self.SoundPlay(c.S_LaserHit)
        elif item_loc == c.BLOCK:
            if self.CheckLoc(
                    x + dx, y + dy
            ):  # Can block be moved in direction of laser? Is square free
                self.MoveObj(x, y, dx, dy, c.S_Push1)  # Push block
            else:
                self.SoundPlay(c.S_LaserHit)
        elif item_loc == c.WALL:
            self.items[x][y] = c.EMPTY  # Destroy wall with laser
            self.SoundPlay(c.S_Bricks)

        elif item_loc == c.ANTITANK_UP:
            if dy == 1:  # Laser hit front of antitank
                # KillAtank()
                self.items[x][y] = c.DEADANTITANK_UP
                self.SoundPlay(c.S_Anti1)
                return False
            elif self.CheckLoc(x + dx, y + dy):
                self.MoveObj(x, y, dx, dy, c.S_Push3)
            else:
                self.SoundPlay(c.S_LaserHit)
        elif item_loc == c.ANTITANK_RIGHT:
            if dx == -1:
                self.items[x][y] = c.DEADANTITANK_RIGHT
                self.SoundPlay(c.S_Anti1)
                return False
            elif self.CheckLoc(x + dx, y + dy):
                self.MoveObj(x, y, dx, dy, c.S_Push3)
            else:
                self.SoundPlay(c.S_LaserHit)
        elif item_loc == c.ANTITANK_DOWN:
            if dy == -1:
                self.items[x][y] = c.DEADANTITANK_DOWN
                self.SoundPlay(c.S_Anti1)
                return False
            elif self.CheckLoc(x + dx, y + dy):
                self.MoveObj(x, y, dx, dy, c.S_Push3)
            else:
                self.SoundPlay(c.S_LaserHit)
        elif item_loc == c.ANTITANK_LEFT:
            if dx == 1:
                self.items[x][y] = c.DEADANTITANK_LEFT
                self.SoundPlay(c.S_Anti1)
                return False
            elif self.CheckLoc(x + dx, y + dy):
                self.MoveObj(x, y, dx, dy, c.S_Push3)
            else:
                self.SoundPlay(c.S_LaserHit)

        elif item_loc == c.MIRROR_LEFT_UP:
            if self.laser.Dir == c.D_RIGHT or self.laser.Dir == c.D_DOWN:
                return True
            if self.CheckLoc(x + dx, y + dy):
                self.MoveObj(x, y, dx, dy, c.S_Push2)
            else:
                self.SoundPlay(c.S_LaserHit)
        elif item_loc == c.MIRROR_UP_RIGHT:
            if self.laser.Dir == c.D_DOWN or self.laser.Dir == c.D_LEFT:
                return True
            if self.CheckLoc(x + dx, y + dy):
                self.MoveObj(x, y, dx, dy, c.S_Push2)
            else:
                self.SoundPlay(c.S_LaserHit)
        elif item_loc == c.MIRROR_RIGHT_DOWN:
            if self.laser.Dir == c.D_UP or self.laser.Dir == c.D_LEFT:
                return True
            if self.CheckLoc(x + dx, y + dy):
                self.MoveObj(x, y, dx, dy, c.S_Push2)
            else:
                self.SoundPlay(c.S_LaserHit)
        elif item_loc == c.MIRROR_DOWN_LEFT:
            if self.laser.Dir == c.D_UP or self.laser.Dir == c.D_RIGHT:
                return True
            if self.CheckLoc(x + dx, y + dy):
                self.MoveObj(x, y, dx, dy, c.S_Push2)
            else:
                self.SoundPlay(c.S_LaserHit)

        elif item_loc == c.GLASS:
            # In original, this is where glass is set to a glowing sprite
            return True

        elif item_loc == c.ROTMIRROR_LEFT_UP:
            if self.laser.Dir == 2 or self.laser.Dir == 3:
                return True
            self.items[x][y] = c.ROTMIRROR_UP_RIGHT
            self.SoundPlay(c.S_Rotate)
        elif item_loc == c.ROTMIRROR_UP_RIGHT:
            if self.laser.Dir == 3 or self.laser.Dir == 4:
                return True
            self.items[x][y] = c.ROTMIRROR_RIGHT_DOWN
            self.SoundPlay(c.S_Rotate)
        elif item_loc == c.ROTMIRROR_RIGHT_DOWN:
            if self.laser.Dir == 1 or self.laser.Dir == 4:
                return True
            self.items[x][y] = c.ROTMIRROR_DOWN_LEFT
            self.SoundPlay(c.S_Rotate)
        elif item_loc == c.ROTMIRROR_DOWN_LEFT:
            if self.laser.Dir == 1 or self.laser.Dir == 2:
                return True
            self.items[x][y] = c.ROTMIRROR_LEFT_UP
            self.SoundPlay(c.S_Rotate)

        # If object is moving into an ice square then add it to the Sliding stack
        if self.wasIce:
            # If is already sliding, del it !
            del_SlideO_from_Mem(x, y)
            # and add a new slide in a new direction
            SlideO = TIceRec(x + dx, y + dy, dx, dy, True)
            add_SlideO_to_Mem(SlideO)
        else:
            del_SlideO_from_Mem(x, y)

        return False

    def IceMoveO(self):
        self.change_log.append("Slid object on ice")
        # Move an item on the ice
        for SlideO in reversed(self.sliding_items):
            if self.terrain[SlideO.x][SlideO.y] == c.THINICE:
                # Sliding off thin ice so melt the ice into water
                self.terrain[SlideO.x][SlideO.y] = c.WATER

            # if destination is empty (not item and not tank)
            # note: CheckLoc also sets wasIce to True is destination is Ice or ThinIce
            if self.CheckLoc(SlideO.x + SlideO.dx, SlideO.y + SlideO.dy) and not (
                    SlideO.x + SlideO.dx == self.tank.X
                    and SlideO.y + SlideO.dy == self.tank.Y
            ):
                savei = self.wasIce
                self.MoveObj(SlideO.x, SlideO.y, SlideO.dx, SlideO.dy, c.S_Push2)
                self.AntiTank()

                # Update position of tracked sliding object
                SlideO.x += SlideO.dx
                SlideO.y += SlideO.dy
                if not savei:
                    SlideO.s = False  # Mark for deletion
            else:
                if self.terrain[SlideO.x][SlideO.y] == c.WATER:
                    # Drop into water if ice melted and item couldn't move
                    self.MoveObj(SlideO.x, SlideO.y, 0, 0, c.S_Sink)
                SlideO.s = False
                self.AntiTank()
        # Remove items that are no-longer sliding (sub_SlideO_from_Mem)
        self.sliding_items = [slide for slide in self.sliding_items if slide.s]

    def IceMoveT(self):
        self.change_log.append("Slid tank on ice")
        #  Move the tank on the Ice
        if self.terrain[self.tank_sliding_data.x][self.tank_sliding_data.y] == c.THINICE:
            self.terrain[self.tank_sliding_data.x][self.tank_sliding_data.y] = c.WATER

        if self.CheckLoc(
                self.tank_sliding_data.x + self.tank_sliding_data.dx,
                self.tank_sliding_data.y + self.tank_sliding_data.dy
        ):
            savei = self.wasIce
            self.ConvMoveTank(self.tank_sliding_data.dx, self.tank_sliding_data.dy, False)

            self.tank_sliding_data.x += self.tank_sliding_data.dx
            self.tank_sliding_data.y += self.tank_sliding_data.dy
            if not savei:
                self.tank_sliding_data.s = False

        else:
            self.tank_sliding_data.s = False


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
        pygame.Color(0xFF0000FF),
        pygame.Color(0x00FF00FF),
        pygame.Color(0x0000FFFF),
        pygame.Color(0x00FFFFFF),
        pygame.Color(0x00FFFFFF),
        pygame.Color(0xFF00FFFF),
        pygame.Color(0xFFFFFFFF),
        pygame.Color(0x808080FF),
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
        for y in range(c.PLAYFIELD_SIZE):
            for x in range(c.PLAYFIELD_SIZE):
                self._draw_sprite(game.terrain[x][y], x, y)
                self._draw_sprite(game.items[x][y], x, y)
        self._draw_tank(game.tank.X, game.tank.Y, game.tank.Dir)
        if game.tank.Firing:
            self._draw_laser(game.laser)
        pygame.display.update()
        self._increment_animation_counter()

    def _draw_sprite(self, entity_id, square_x, square_y):
        board_location = (
            self.GAMEBOARD_OFFSET_X_PX + (square_x * self.SPRITE_SIZE),
            self.GAMEBOARD_OFFSET_Y_PX + (square_y * self.SPRITE_SIZE),
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

    def _draw_tank(self, square_x, square_y, direction):
        board_location = (
            self.GAMEBOARD_OFFSET_X_PX + (square_x * self.SPRITE_SIZE),
            self.GAMEBOARD_OFFSET_Y_PX + (square_y * self.SPRITE_SIZE),
            self.SPRITE_SIZE,
            self.SPRITE_SIZE,
        )
        bmp_id = c.SPRITE_MAPPING[c.GetTankDirectional[direction]]
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
        colour = self.LASER_COLOURS[laser.LaserColor]
        x = self.GAMEBOARD_OFFSET_X_PX + (laser.X * self.SPRITE_SIZE)
        y = self.GAMEBOARD_OFFSET_Y_PX + (laser.Y * self.SPRITE_SIZE)
        h = self.SPRITE_SIZE / 2
        if laser.Dir == laser.oDir:
            # Not deflecting
            if laser.Dir == c.D_UP or laser.Dir == c.D_DOWN:
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
                if direction == c.D_UP:
                    return pygame.Rect(
                        x + self.LASER_OFFSET,
                        y,
                        self.SPRITE_SIZE - self.LASER_OFFSET - self.LASER_OFFSET,
                        h,
                    )
                elif direction == c.D_RIGHT:
                    return pygame.Rect(
                        x + h,
                        y + self.LASER_OFFSET,
                        self.SPRITE_SIZE - h,
                        self.SPRITE_SIZE - self.LASER_OFFSET - self.LASER_OFFSET,
                    )
                elif direction == c.D_DOWN:
                    return pygame.Rect(
                        x + self.LASER_OFFSET,
                        y + h,
                        self.SPRITE_SIZE - self.LASER_OFFSET - self.LASER_OFFSET,
                        self.SPRITE_SIZE - h,
                    )
                elif direction == c.D_LEFT:
                    return pygame.Rect(
                        x,
                        y + self.LASER_OFFSET,
                        h,
                        self.SPRITE_SIZE - self.LASER_OFFSET - self.LASER_OFFSET,
                    )

            beam_a = laser_dir_to_rect(laser.Dir)
            beam_b = laser_dir_to_rect(c.D_INVERT[laser.oDir])

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
        for y in range(c.PLAYFIELD_SIZE):
            for x in range(c.PLAYFIELD_SIZE):
                if (
                        game.terrain[x][y] not in (c.GRASS, c.WATER)
                        or game.items[x][y] != c.EMPTY
                        or (game.tank.X == x and game.tank.Y == y)
                ):
                    # Square of interest
                    x_min = min(x_min, x)
                    y_min = min(y_min, y)
                    x_max = max(x_max, x)
                    y_max = max(y_max, y)
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
                        TextGraphics.cell_as_numbers(game, x, y)
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
    def cell_as_numbers(game: GameState, x, y):
        terrain = game.terrain[x][y]
        item = game.items[x][y]
        if terrain == c.GRASS:
            terrain = " "
        if item == c.EMPTY:
            item = " "
        if game.tank.X == x and game.tank.Y == y:
            item = "T"
        if game.tank.Firing and game.laser.X == x and game.laser.Y == y:
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
        print(f"Tick: {tick_counter}")
        print(f"Moves:{txtgrphcs.print_directions(game.moves_buffer)}")
        print(f"Actions: {game.change_log}")
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
    debug_level("tricks/Tricks", 5)
