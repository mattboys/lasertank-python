from enum import Enum
from functools import partial


class Solved(Exception):
    pass


class GameOver(Exception):
    pass


class Direction(Enum):
    N = "N"
    E = "E"
    S = "S"
    W = "W"
    SHOOT = "F"
    NONE = "0"

    @staticmethod
    def get_opposite(direction):
        lookup = {
            Direction.N: Direction.S,
            Direction.S: Direction.N,
            Direction.E: Direction.W,
            Direction.W: Direction.E,
            Direction.NONE: Direction.NONE,
        }
        return lookup[direction]

    @staticmethod
    def get_clockwise(direction):
        lookup = {
            Direction.N: Direction.E,
            Direction.E: Direction.S,
            Direction.S: Direction.W,
            Direction.W: Direction.N,
        }
        return lookup[direction]

    @staticmethod
    def get_xy(direction):
        lookup = {
            Direction.N: (0, -1),
            Direction.E: (1, 0),
            Direction.S: (0, 1),
            Direction.W: (-1, 0),
            Direction.NONE: (0, 0),
        }
        return lookup[direction]


class Angle(Enum):
    NW = "NW"
    NE = "NE"
    SE = "SE"
    SW = "SW"

    @staticmethod
    def to_dirs(angle):
        lookup = {
            Angle.NW: (Direction.W, Direction.N),
            Angle.NE: (Direction.N, Direction.E),
            Angle.SE: (Direction.E, Direction.S),
            Angle.SW: (Direction.S, Direction.W),
        }
        return lookup[angle]


def vec_add(a, b):
    return a[0] + b[0], a[1] + b[1]


class LTSprite:
    gameboard = None

    def __init__(self, position):
        self.position = position


class Laser(LTSprite):

    def __init__(self):
        self.exists = False
        self.colour = "red"
        self.dir = Direction.NONE
        self.from_direction = Direction.NONE
        LTSprite.__init__(self, (0, 0))

    def update(self):
        if self.exists:
            self.from_direction = Direction.get_opposite(self.dir)  # Save previous direction
            self.position = vec_add(self.position, Direction.get_xy(self.dir))

            if self.gameboard.is_within_board(self.position):
                interacting_item = self.gameboard.get_item(self.position)
                if interacting_item is not None:
                    self.dir = interacting_item.hit_with_laser(
                        self.from_direction
                    )
                else:
                    # Passing through an empty square
                    self.dir = Direction.get_opposite(self.from_direction)
                if self.dir == Direction.NONE:
                    self.die()
            else:
                self.die()

    def fire(self, position, direction, good):
        if self.exists:
            # Only one laser allowed to exist on the board at once
            return False
        else:
            self.exists = True
            # Spawn at location and direction
            self.position = position
            self.dir = direction
            self.from_direction = Direction.NONE
            if good:
                self.colour = "green"
            else:
                self.colour = "red"
            return True

    def die(self):
        self.exists = False


class Terrain(LTSprite):
    def __init__(self, init_pos):
        LTSprite.__init__(self, init_pos)

    def effect(self, item_on):
        item_on.momentum = Direction.NONE

    def obj_leaving(self):
        pass


class Grass(Terrain):
    def __init__(self, position):
        Terrain.__init__(self, position)


class Flag(Terrain):
    def __init__(self, position):
        Terrain.__init__(self, position)

    def effect(self, item_on):
        if isinstance(item_on, Tank):
            raise Solved


class Water(Terrain):
    def __init__(self, position):
        Terrain.__init__(self, position)

    def effect(self, item_on):
        item_on.momentum = Direction.NONE
        if isinstance(item_on, Tank):
            raise GameOver
        elif isinstance(item_on, Block):
            self.gameboard.put_terrain(self.position, Bridge(self.position))
        item_on.destroy()


class Conveyor(Terrain):
    def __init__(self, direction, position):
        self.dir = direction
        Terrain.__init__(self, position)

    def effect(self, item_on):
        if isinstance(item_on, Tank):
            item_on._push(self.dir)


class Ice(Terrain):
    def __init__(self, position):
        Terrain.__init__(self, position)

    def effect(self, item_on):
        # Keep current momentum
        pass


class ThinIce(Terrain):
    def __init__(self, position):
        Terrain.__init__(self, position)

    def effect(self, item_on):
        # Keep current momentum
        pass

    def obj_leaving(self):
        self.gameboard.put_terrain(self.position, Water(self.position))


class Bridge(Terrain):
    def __init__(self, position):
        Terrain.__init__(self, position)


class Tunnel(Terrain):
    all_tunnels = []

    def __init__(self, tunnel_id, position):
        Terrain.__init__(self, position)
        self.tunnel_id = tunnel_id
        self.exits = []
        self.waiting = False  # Waiting for an open exit
        for other_tunnel in Tunnel.all_tunnels:
            if other_tunnel.tunnel_id == self.tunnel_id:
                other_tunnel.add_exit(self)
                self.add_exit(other_tunnel)

    def add_exit(self, other_tunnel):
        assert other_tunnel is not self, "Cannot add a tunnel as an exit to itself!"
        self.exits.append(other_tunnel)
        self.exits.sort(key=lambda temp_tunnel: (temp_tunnel.position[1], temp_tunnel.position[0]))

    def effect(self, item_on):
        if len(self.exits) == 0:
            # Black Hole
            item_on.destroy()
            return
        else:
            # Find an unblocked exit
            for exit_tunnel in self.exits:
                if self.gameboard.is_square_empty(exit_tunnel.position):  # is unblocked?
                    item_on.teleport(exit_tunnel.position)  # Teleport
                    return
            # Only blocked exit(s) so set tunnel as waiting
            # will transport when another tunnel is unblocked
            self.waiting = True

    def get_item_waiting(self):
        if not self.gameboard.is_square_empty(self.position):
            return self.gameboard.get_item(self.position)
        elif self.gameboard.tank.position == self.position:
            return self.gameboard.get_tank()
        else:
            print('Tunnel error')
            return None

    def obj_leaving(self):
        x, y = self.position
        if self.gameboard.is_square_empty(self.position) and self.gameboard.get_tank().position != self.position:
            self.waiting = False
        for link in self.exits:
            if link.waiting:
                link.waiting = False
                link.effect(link.get_item_waiting())
                return


# Objects
class Item(LTSprite):

    def __init__(self, init_pos):
        self.momentum = Direction.NONE
        LTSprite.__init__(self, init_pos)

    def destroy(self):
        self.gameboard.destroy_item(self.position)

    def teleport(self, destination):
        self.momentum = Direction.NONE
        if not isinstance(self, Tank):
            self.gameboard.put_item(self.position, Empty(self.position))
            assert self.gameboard.is_square_empty(destination), "Can't move item into occupied space!"
            self.gameboard.put_item(destination, self)
        self.position = destination

    def _set_position(self, destination):
        original_position = self.position
        if not isinstance(self, Tank):
            self.gameboard.put_item(original_position, Empty(original_position))
            assert self.gameboard.is_square_empty(destination), "Can't move item into occupied space!"
            self.gameboard.put_item(destination, self)
        self.position = destination
        # Resolve effects on terrain
        self.gameboard.get_terrain(original_position).obj_leaving()
        self.gameboard.get_terrain(destination).effect(self)

    def _push(self, direction):
        """ Assumes this object can legally move in direction, then set momentum and add to gameboard.sliding list """
        self.momentum = direction
        self.gameboard.start_sliding(self)

    def resolve_momentum(self):
        destination = vec_add(self.position, Direction.get_xy(self.momentum))
        if self.gameboard.can_move_into(destination):
            self._set_position(destination)
        else:
            self.momentum = Direction.NONE

    def hit_with_laser(self, from_direction):
        """ Hit this item with a laser from the direction, return exiting direction """
        return Direction.get_opposite(from_direction)


class Empty(Item):
    def __init__(self, init_pos):
        Item.__init__(self, init_pos)

    def destroy(self):
        pass


class Tank(Item):
    def __init__(self, direction, position):
        self.dir = direction
        self.firing = False
        Item.__init__(self, position)

    def shoot(self):
        self.gameboard.get_laser().fire(self.position, self.dir, good=True)

    def destroy(self):
        raise GameOver

    def hit_with_laser(self, from_direction):
        # Hit this item with a laser from the direction, return exiting direction
        raise GameOver

    def rotate(self, direction):
        """ Face direction specified without moving spaces """
        self.dir = direction


class Solid(Item):
    def __init__(self, position):
        Item.__init__(self, position)

    def hit_with_laser(self, from_direction):
        return Direction.NONE


class Block(Item):
    def __init__(self, position):
        Item.__init__(self, position)

    def hit_with_laser(self, from_direction):
        # Hit this item with a laser from the direction, return exiting direction
        self._push(Direction.get_opposite(from_direction))
        return Direction.NONE


class Wall(Item):
    def __init__(self, position):
        Item.__init__(self, position)

    def hit_with_laser(self, from_direction):
        self.destroy()
        return Direction.NONE


class Antitank(Item):
    def __init__(self, direction, position):
        self.dir = direction
        self.firing = False
        Item.__init__(self, position)

    def hit_with_laser(self, from_direction):
        if from_direction == self.dir:
            self.gameboard.put_item(self.position, AntitankDead(self.dir, self.position))
            return Direction.NONE
        else:
            self._push(Direction.get_opposite(from_direction))
            return Direction.NONE

    def shoot(self):
        self.gameboard.get_laser().fire(self.position, self.dir, good=False)


class AntitankDead(Item):
    def __init__(self, direction, position):
        self.dir = direction
        Item.__init__(self, position)

    def hit_with_laser(self, from_direction):
        return Direction.NONE


class Mirror(Item):
    def __init__(self, angle, position):
        self.dir = angle
        Item.__init__(self, position)

    def hit_with_laser(self, from_direction):
        dir1, dir2 = Angle.to_dirs(self.dir)
        if from_direction == dir1:
            return dir2
        elif from_direction == dir2:
            return dir1
        else:
            self._push(Direction.get_opposite(from_direction))
            return Direction.NONE


class Glass(Item):

    def __init__(self, position):
        Item.__init__(self, position)

    def hit_with_laser(self, from_direction):
        # Hit this item with a laser from the direction, return exiting direction
        return Direction.get_opposite(from_direction)


class RotMirror(Item):

    def __init__(self, angle, position):
        self.dir = angle
        Item.__init__(self, position)

    def hit_with_laser(self, from_direction):
        dir1, dir2 = Angle.to_dirs(self.dir)
        if from_direction == dir1:
            return dir2
        elif from_direction == dir2:
            return dir1
        else:
            self.rotate(Direction.get_clockwise(self.dir))
            return Direction.NONE

    def rotate(self, direction):
        """ Face direction specified without moving spaces """
        self.dir = direction


def map_strings_to_objects(object_string, position):
    import constants
    mapping = {
        constants.Empty: Empty(position),
        constants.Grass: Grass(position),
        constants.Flag: Flag(position),
        constants.Water: Water(position),
        constants.Conveyor_N: Conveyor(Direction.N, position),
        constants.Conveyor_S: Conveyor(Direction.S, position),
        constants.Conveyor_E: Conveyor(Direction.E, position),
        constants.Conveyor_W: Conveyor(Direction.W, position),
        constants.Ice: Ice(position),
        constants.ThinIce: ThinIce(position),
        constants.Bridge: Bridge(position),
        constants.Tunnel_0: Tunnel(0, position),
        constants.Tunnel_1: Tunnel(1, position),
        constants.Tunnel_2: Tunnel(2, position),
        constants.Tunnel_3: Tunnel(3, position),
        constants.Tunnel_4: Tunnel(4, position),
        constants.Tunnel_5: Tunnel(5, position),
        constants.Tunnel_6: Tunnel(6, position),
        constants.Tunnel_7: Tunnel(7, position),
        constants.Tunnel_8: Tunnel(8, position),
        constants.Tunnel_9: Tunnel(9, position),
        constants.Tank_N: Tank(Direction.N, position),
        constants.Tank_S: Tank(Direction.S, position),
        constants.Tank_E: Tank(Direction.E, position),
        constants.Tank_W: Tank(Direction.W, position),
        constants.Solid: Solid(position),
        constants.Block: Block(position),
        constants.Wall: Wall(position),
        constants.Antitank_N: Antitank(Direction.N, position),
        constants.Antitank_S: Antitank(Direction.S, position),
        constants.Antitank_E: Antitank(Direction.E, position),
        constants.Antitank_W: Antitank(Direction.W, position),
        constants.DeadAntitank_N: AntitankDead(Direction.N, position),
        constants.DeadAntitank_S: AntitankDead(Direction.S, position),
        constants.DeadAntitank_E: AntitankDead(Direction.E, position),
        constants.DeadAntitank_W: AntitankDead(Direction.W, position),
        constants.Mirror_NW: Mirror(Angle.NW, position),
        constants.Mirror_NE: Mirror(Angle.NE, position),
        constants.Mirror_SE: Mirror(Angle.SE, position),
        constants.Mirror_SW: Mirror(Angle.SW, position),
        constants.Glass: Glass(position),
        constants.RotMirror_NW: RotMirror(Angle.NW, position),
        constants.RotMirror_NE: RotMirror(Angle.NE, position),
        constants.RotMirror_SE: RotMirror(Angle.SE, position),
        constants.RotMirror_SW: RotMirror(Angle.SW, position),
    }
    return mapping[object_string]