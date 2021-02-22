import Direction
import constants


class Solved(Exception):
    pass


class GameOver(Exception):
    pass


def vec_add(a, b):
    return a[0] + b[0], a[1] + b[1]


class LaserTankObject:
    gameboard = None

    def __init__(self, position):
        self.position = position


class Laser(LaserTankObject):

    def __init__(self, exists=False, colour="red", direction=Direction.NONE, from_direction=Direction.NONE,
                 position=(0, 0)):
        self.exists = exists
        self.colour = colour
        self.direction = direction
        self.from_direction = from_direction
        LaserTankObject.__init__(self, position)

    def update(self):
        """ Move laser each tick if existing - implementation of MoveLaser() c function """
        if self.exists:
            self.from_direction = Direction.get_opposite(self.direction)  # Save previous direction

            # # Reset any glowing glass previously under laser
            # previous_interacting_item = self.gameboard.get_item(self.position)
            # if isinstance(previous_interacting_item, Glass):
            #     previous_interacting_item.colour = 'none'

            self.position = vec_add(self.position, Direction.get_xy(self.direction))

            if self.gameboard.is_within_board(self.position):
                interacting_item = self.gameboard.get_tank_or_item(self.position)
                self.direction = interacting_item.hit_with_laser(
                    self.from_direction
                )
                if self.direction == Direction.NONE:
                    self.die()

                # Implement the LaserBounceOnIce logic where the laser moves twice if reflecting on a sliding mirror
                if self.exists and self.gameboard.is_sliding(interacting_item):
                    self.update()
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
            self.direction = direction
            self.from_direction = Direction.NONE
            if good:
                self.colour = "green"
            else:
                self.colour = "red"
            return True

    def die(self):
        self.exists = False

    def serialize(self):
        """ Return minimal dict to save game state when idle"""
        return self.exists, self.colour, self.direction, self.from_direction, self.position


# Objects
class Item(LaserTankObject):

    def __init__(self, init_pos):
        LaserTankObject.__init__(self, init_pos)

    def destroy(self):
        self.gameboard.destroy_item(self.position)

    def hit_with_laser(self, from_direction):
        """ Hit this item with a laser from the direction, return exiting direction """
        return Direction.get_opposite(from_direction)

    def serialize(self):
        raise ValueError(f"Serialize function unavailable for {self.__name__}")


class ItemMovable(Item):
    def __init__(self, init_pos):
        self._momentum = Direction.NONE
        Item.__init__(self, init_pos)

    def is_sliding(self):
        return self._momentum != Direction.NONE

    def push(self, direction):
        """ Assumes this object can legally move in direction, then set momentum and add to gameboard.sliding list """
        self._momentum = direction
        self.gameboard.start_sliding(self)

    def resolve_momentum(self):
        """ Try to move item in the direction of it's momentum """
        destination = vec_add(self.position, Direction.get_xy(self._momentum))
        if self.gameboard.can_move_into(destination):
            original_position = self.position
            # Set new position
            self.change_position(destination)
            # Resolve effects on terrain
            self.gameboard.get_terrain(destination).effect(self)
            self.gameboard.get_terrain(original_position).obj_leaving()
        else:
            self._momentum = Direction.NONE
            # Melt ThinIce if on currently
            if isinstance(self.gameboard.get_terrain(self.position), ThinIce):
                self.gameboard.get_terrain(self.position).obj_leaving()
                self.gameboard.get_terrain(self.position).effect(self)

    def change_position(self, destination):
        if not isinstance(self, Tank):
            self.gameboard.put_item(self.position, Empty(self.position))
            assert self.gameboard.is_square_empty(destination), "Can't move item into occupied space!"
            self.gameboard.put_item(destination, self)
        self.position = destination


class Empty(Item):
    def __init__(self, position):
        Item.__init__(self, position)

    def destroy(self):
        pass

    def serialize(self):
        return constants.Empty


class Tank(ItemMovable):
    def __init__(self, direction, position):
        self.direction = direction
        ItemMovable.__init__(self, position)

    def shoot(self):
        self.gameboard.get_laser().fire(self.position, self.direction, good=True)

    def destroy(self):
        raise GameOver

    def hit_with_laser(self, from_direction):
        # Hit this item with a laser from the direction, return exiting direction
        raise GameOver

    def rotate(self, direction):
        """ Face direction specified without moving spaces """
        self.direction = direction

    def move(self, direction):
        self.push(direction)

    def serialize(self):
        """ Return minimal dict to save game state when idle"""
        return self.direction, self.position


class Solid(Item):
    def __init__(self, position):
        Item.__init__(self, position)

    def hit_with_laser(self, from_direction):
        return Direction.NONE

    def serialize(self):
        return constants.Solid


class Block(ItemMovable):
    def __init__(self, position):
        self._momentum = Direction.NONE
        Item.__init__(self, position)

    def hit_with_laser(self, from_direction):
        # Hit this item with a laser from the direction, return exiting direction
        self.push(Direction.get_opposite(from_direction))
        return Direction.NONE

    def push(self, direction):
        """ Assumes this object can legally move in direction, then set momentum and add to gameboard.sliding list """
        self._momentum = direction
        self.gameboard.start_sliding(self)

    def serialize(self):
        return constants.Block


class Wall(Item):
    def __init__(self, position):
        Item.__init__(self, position)

    def hit_with_laser(self, from_direction):
        self.destroy()
        return Direction.NONE

    def serialize(self):
        return constants.Wall


class Antitank(ItemMovable):
    def __init__(self, direction, position):
        self.direction = direction
        Item.__init__(self, position)

    def hit_with_laser(self, from_direction):
        if from_direction == self.direction:
            self.gameboard.put_item(self.position, AntitankDead(self.direction, self.position))
            return Direction.NONE
        else:
            self.push(Direction.get_opposite(from_direction))
            return Direction.NONE

    def shoot(self):
        self.gameboard.get_laser().fire(self.position, self.direction, good=False)

    def serialize(self):
        if self.direction == Direction.N:
            return constants.Antitank_N
        elif self.direction == Direction.E:
            return constants.Antitank_E
        elif self.direction == Direction.W:
            return constants.Antitank_W
        elif self.direction == Direction.S:
            return constants.Antitank_S
        else:
            raise ValueError("Cannot serialize Antitank")


class AntitankDead(Item):
    def __init__(self, direction, position):
        self.direction = direction
        Item.__init__(self, position)

    def hit_with_laser(self, from_direction):
        return Direction.NONE

    def serialize(self):
        if self.direction == Direction.N:
            return constants.DeadAntitank_N
        elif self.direction == Direction.E:
            return constants.DeadAntitank_E
        elif self.direction == Direction.W:
            return constants.DeadAntitank_W
        elif self.direction == Direction.S:
            return constants.DeadAntitank_S
        else:
            raise ValueError("Cannot serialize AntitankDead")


class Mirror(ItemMovable):
    def __init__(self, direction, position):
        self.direction = direction
        ItemMovable.__init__(self, position)

    def hit_with_laser(self, from_direction):
        dir1, dir2 = Direction.reflection_angle_to_dirs(self.direction)
        if from_direction == dir1:
            return dir2
        elif from_direction == dir2:
            return dir1
        else:
            self.push(Direction.get_opposite(from_direction))
            return Direction.NONE

    def serialize(self):
        if self.direction == Direction.N:
            return constants.Mirror_N
        elif self.direction == Direction.E:
            return constants.Mirror_E
        elif self.direction == Direction.W:
            return constants.Mirror_W
        elif self.direction == Direction.S:
            return constants.Mirror_S
        else:
            raise ValueError("Cannot serialize Mirror")


class Glass(Item):

    def __init__(self, position):
        Item.__init__(self, position)
        # self._colour = 'none'

    def hit_with_laser(self, from_direction):
        # Hit this item with a laser from the direction, return exiting direction
        # self._colour = self.gameboard.get_laser().colour
        return Direction.get_opposite(from_direction)

    def serialize(self):
        return constants.Glass


class RotMirror(Item):

    def __init__(self, direction, position):
        self.direction = direction
        Item.__init__(self, position)

    def hit_with_laser(self, from_direction):
        dir1, dir2 = Direction.reflection_angle_to_dirs(self.direction)
        if from_direction == dir1:
            return dir2
        elif from_direction == dir2:
            return dir1
        else:
            self.rotate(Direction.get_clockwise(self.direction))
            return Direction.NONE

    def rotate(self, direction):
        """ Face direction specified without moving spaces """
        self.direction = direction

    def serialize(self):
        if self.direction == Direction.N:
            return constants.RotMirror_N
        elif self.direction == Direction.E:
            return constants.RotMirror_E
        elif self.direction == Direction.W:
            return constants.RotMirror_W
        elif self.direction == Direction.S:
            return constants.RotMirror_S
        else:
            raise ValueError("Cannot serialize RotMirror")


class Terrain(LaserTankObject):
    def __init__(self, init_pos):
        LaserTankObject.__init__(self, init_pos)

    def effect(self, item_on):
        item_on._momentum = Direction.NONE

    def obj_leaving(self):
        """ An item is sliding off the square """
        pass


class Grass(Terrain):
    def __init__(self, position):
        Terrain.__init__(self, position)

    def serialize(self):
        return constants.Grass


class Flag(Terrain):
    def __init__(self, position):
        Terrain.__init__(self, position)

    def effect(self, item_on):
        if isinstance(item_on, Tank):
            raise Solved

    def serialize(self):
        return constants.Flag


class Water(Terrain):
    def __init__(self, position):
        Terrain.__init__(self, position)

    def effect(self, item_on):
        item_on._momentum = Direction.NONE
        if isinstance(item_on, Tank):
            raise GameOver
        elif isinstance(item_on, Block):
            self.gameboard.put_terrain(self.position, Bridge(self.position))
        item_on.destroy()

    def serialize(self):
        return constants.Water


class Conveyor(Terrain):
    def __init__(self, direction, position):
        self.direction = direction
        Terrain.__init__(self, position)

    def effect(self, item_on):
        if isinstance(item_on, Tank):
            item_on.push(self.direction)

    def serialize(self):
        if self.direction == Direction.N:
            return constants.Conveyor_N
        elif self.direction == Direction.E:
            return constants.Conveyor_E
        elif self.direction == Direction.W:
            return constants.Conveyor_W
        elif self.direction == Direction.S:
            return constants.Conveyor_S
        else:
            raise ValueError("Cannot serialize Conveyor")


class Ice(Terrain):
    def __init__(self, position):
        Terrain.__init__(self, position)

    def effect(self, item_on):
        # Keep current momentum
        pass

    def serialize(self):
        return constants.Ice


class ThinIce(Terrain):
    def __init__(self, position):
        Terrain.__init__(self, position)

    def obj_leaving(self):
        self.gameboard.put_terrain(self.position, Water(self.position))

    def serialize(self):
        return constants.ThinIce


class Bridge(Terrain):
    def __init__(self, position):
        Terrain.__init__(self, position)

    def serialize(self):
        return constants.Bridge


class Tunnel(Terrain):

    def __init__(self, tunnel_id, position, waiting=False):
        Terrain.__init__(self, position)
        self.tunnel_id = tunnel_id
        self.waiting = waiting  # Waiting for an open exit

    def _get_exits(self):
        exits = self.gameboard.get_tunnels(self.tunnel_id)
        exits.remove(self)
        return exits

    def effect(self, item_on: ItemMovable):
        exits = self._get_exits()
        if len(exits) == 0:
            # Black Hole
            item_on.destroy()
            return
        else:
            # Find an unblocked exit
            for exit_tunnel in exits:
                if self.gameboard.is_square_empty(exit_tunnel.position):  # is unblocked?
                    item_on.change_position(exit_tunnel.position)  # Teleport
                    return
            # Only blocked exit(s) so set tunnel as waiting
            # will transport when another tunnel is unblocked
            self.waiting = True

    def release(self):
        """ Was waiting and now an exit is free """
        self.waiting = False
        if not self.gameboard.is_square_empty(self.position):
            return self.gameboard.get_item(self.position)
        elif self.gameboard.board_tank.position == self.position:
            return self.gameboard.get_tank()
        else:
            print('Tunnel error')
            return None

    def obj_leaving(self):
        if self.gameboard.is_square_empty(self.position) and self.gameboard.get_tank().position != self.position:
            self.waiting = False
        for link in self._get_exits():
            if link.waiting:
                link.release()
                # Only release first waiting instance
                return

    def serialize(self):
        if self.tunnel_id == 0:
            if self.waiting:
                return constants.Tunnel_0_waiting
            else:
                return constants.Tunnel_0
        elif self.tunnel_id == 1:
            if self.waiting:
                return constants.Tunnel_1_waiting
            else:
                return constants.Tunnel_1
        elif self.tunnel_id == 2:
            if self.waiting:
                return constants.Tunnel_2_waiting
            else:
                return constants.Tunnel_2
        elif self.tunnel_id == 3:
            if self.waiting:
                return constants.Tunnel_3_waiting
            else:
                return constants.Tunnel_3
        elif self.tunnel_id == 4:
            if self.waiting:
                return constants.Tunnel_4_waiting
            else:
                return constants.Tunnel_4
        elif self.tunnel_id == 5:
            if self.waiting:
                return constants.Tunnel_5_waiting
            else:
                return constants.Tunnel_5
        elif self.tunnel_id == 6:
            if self.waiting:
                return constants.Tunnel_6_waiting
            else:
                return constants.Tunnel_6
        elif self.tunnel_id == 7:
            if self.waiting:
                return constants.Tunnel_7_waiting
            else:
                return constants.Tunnel_7
        elif self.tunnel_id == 8:
            if self.waiting:
                return constants.Tunnel_8_waiting
            else:
                return constants.Tunnel_8
        elif self.tunnel_id == 9:
            if self.waiting:
                return constants.Tunnel_9_waiting
            else:
                return constants.Tunnel_9
        else:
            raise ValueError("Cannot serialize Tunnel")


def map_strings_to_objects(object_string, position):
    import constants
    mapping = {
        constants.Empty: ("Empty", None),
        constants.Grass: ("Grass", None),
        constants.Flag: ("Flag", None),
        constants.Water: ("Water", None),
        constants.Conveyor_N: ("Conveyor", Direction.N),
        constants.Conveyor_S: ("Conveyor", Direction.S),
        constants.Conveyor_E: ("Conveyor", Direction.E),
        constants.Conveyor_W: ("Conveyor", Direction.W),
        constants.Ice: ("Ice", None),
        constants.ThinIce: ("ThinIce", None),
        constants.Bridge: ("Bridge", None),
        constants.Tunnel_0: ("Tunnel", 0),
        constants.Tunnel_1: ("Tunnel", 1),
        constants.Tunnel_2: ("Tunnel", 2),
        constants.Tunnel_3: ("Tunnel", 3),
        constants.Tunnel_4: ("Tunnel", 4),
        constants.Tunnel_5: ("Tunnel", 5),
        constants.Tunnel_6: ("Tunnel", 6),
        constants.Tunnel_7: ("Tunnel", 7),
        constants.Tunnel_8: ("Tunnel", 8),
        constants.Tunnel_9: ("Tunnel", 9),
        constants.Tank_N: ("Tank", Direction.N),
        constants.Tank_S: ("Tank", Direction.S),
        constants.Tank_E: ("Tank", Direction.E),
        constants.Tank_W: ("Tank", Direction.W),
        constants.Solid: ("Solid", None),
        constants.Block: ("Block", None),
        constants.Wall: ("Wall", None),
        constants.Antitank_N: ("Antitank", Direction.N),
        constants.Antitank_S: ("Antitank", Direction.S),
        constants.Antitank_E: ("Antitank", Direction.E),
        constants.Antitank_W: ("Antitank", Direction.W),
        constants.DeadAntitank_N: ("AntitankDead", Direction.N),
        constants.DeadAntitank_S: ("AntitankDead", Direction.S),
        constants.DeadAntitank_E: ("AntitankDead", Direction.E),
        constants.DeadAntitank_W: ("AntitankDead", Direction.W),
        constants.Mirror_N: ("Mirror", Direction.N),
        constants.Mirror_E: ("Mirror", Direction.E),
        constants.Mirror_S: ("Mirror", Direction.S),
        constants.Mirror_W: ("Mirror", Direction.W),
        constants.Glass: ("Glass", None),
        constants.RotMirror_N: ("RotMirror", Direction.N),
        constants.RotMirror_E: ("RotMirror", Direction.E),
        constants.RotMirror_S: ("RotMirror", Direction.S),
        constants.RotMirror_W: ("RotMirror", Direction.W),
    }
    obj, param = mapping[object_string]
    if param is None:
        return getattr(__import__("sprites"), obj)(position)
    else:
        return getattr(__import__("sprites"), obj)(param, position)


def deserialize(obj_name, position):
    """ Return an object from the serialized version
    obj_name: str representation of the object name
    params_dict: dictionary of object parameters to use in constructor
     i.e.: deserialize("Conveyor", {'direction': 'S', 'position': (9, 14, position)}, position) """

    if obj_name == constants.Grass:
        return Grass(position)
    elif obj_name == constants.Flag:
        return Flag(position)
    elif obj_name == constants.Water:
        return Water(position)
    elif obj_name == constants.Conveyor_N:
        return Conveyor(Direction.N, position)
    elif obj_name == constants.Conveyor_S:
        return Conveyor(Direction.S, position)
    elif obj_name == constants.Conveyor_E:
        return Conveyor(Direction.E, position)
    elif obj_name == constants.Conveyor_W:
        return Conveyor(Direction.W, position)
    elif obj_name == constants.Ice:
        return Ice(position)
    elif obj_name == constants.ThinIce:
        return ThinIce(position)
    elif obj_name == constants.Bridge:
        return Bridge(position)
    elif obj_name == constants.Tunnel_0:
        return Tunnel(0, position)
    elif obj_name == constants.Tunnel_1:
        return Tunnel(1, position)
    elif obj_name == constants.Tunnel_2:
        return Tunnel(2, position)
    elif obj_name == constants.Tunnel_3:
        return Tunnel(3, position)
    elif obj_name == constants.Tunnel_4:
        return Tunnel(4, position)
    elif obj_name == constants.Tunnel_5:
        return Tunnel(5, position)
    elif obj_name == constants.Tunnel_6:
        return Tunnel(6, position)
    elif obj_name == constants.Tunnel_7:
        return Tunnel(7, position)
    elif obj_name == constants.Tunnel_8:
        return Tunnel(8, position)
    elif obj_name == constants.Tunnel_9:
        return Tunnel(9, position)
    elif obj_name == constants.Tunnel_0_waiting:
        return Tunnel(0, True, position)
    elif obj_name == constants.Tunnel_1_waiting:
        return Tunnel(1, True, position)
    elif obj_name == constants.Tunnel_2_waiting:
        return Tunnel(2, True, position)
    elif obj_name == constants.Tunnel_3_waiting:
        return Tunnel(3, True, position)
    elif obj_name == constants.Tunnel_4_waiting:
        return Tunnel(4, True, position)
    elif obj_name == constants.Tunnel_5_waiting:
        return Tunnel(5, True, position)
    elif obj_name == constants.Tunnel_6_waiting:
        return Tunnel(6, True, position)
    elif obj_name == constants.Tunnel_7_waiting:
        return Tunnel(7, True, position)
    elif obj_name == constants.Tunnel_8_waiting:
        return Tunnel(8, True, position)
    elif obj_name == constants.Tunnel_9_waiting:
        return Tunnel(9, True, position)
    elif obj_name == constants.Tank_N:
        return Tank(Direction.N, position)
    elif obj_name == constants.Tank_S:
        return Tank(Direction.S, position)
    elif obj_name == constants.Tank_E:
        return Tank(Direction.E, position)
    elif obj_name == constants.Tank_W:
        return Tank(Direction.W, position)
    elif obj_name == constants.Empty:
        return Empty(position)
    elif obj_name == constants.Solid:
        return Solid(position)
    elif obj_name == constants.Block:
        return Block(position)
    elif obj_name == constants.Wall:
        return Wall(position)
    elif obj_name == constants.Antitank_N:
        return Antitank(Direction.N, position)
    elif obj_name == constants.Antitank_S:
        return Antitank(Direction.S, position)
    elif obj_name == constants.Antitank_E:
        return Antitank(Direction.E, position)
    elif obj_name == constants.Antitank_W:
        return Antitank(Direction.W, position)
    elif obj_name == constants.DeadAntitank_N:
        return AntitankDead(Direction.N, position)
    elif obj_name == constants.DeadAntitank_S:
        return AntitankDead(Direction.S, position)
    elif obj_name == constants.DeadAntitank_E:
        return AntitankDead(Direction.E, position)
    elif obj_name == constants.DeadAntitank_W:
        return AntitankDead(Direction.W, position)
    elif obj_name == constants.Mirror_N:
        return Mirror(Direction.N, position)
    elif obj_name == constants.Mirror_S:
        return Mirror(Direction.S, position)
    elif obj_name == constants.Mirror_E:
        return Mirror(Direction.E, position)
    elif obj_name == constants.Mirror_W:
        return Mirror(Direction.W, position)
    elif obj_name == constants.Glass:
        return Glass(position)
    elif obj_name == constants.RotMirror_N:
        return RotMirror(Direction.N, position)
    elif obj_name == constants.RotMirror_S:
        return RotMirror(Direction.S, position)
    elif obj_name == constants.RotMirror_E:
        return RotMirror(Direction.E, position)
    elif obj_name == constants.RotMirror_W:
        return RotMirror(Direction.W, position)
    else:
        raise ValueError(f"Cannot deserialize {obj_name}, {position}")


def deserialize_laser(parameters):
    exists, colour, direction, from_direction, position = parameters
    position = tuple(position)
    return Laser(exists, colour, direction, from_direction, position)


def deserialize_tank(parameters):
    direction, position = parameters
    position = tuple(position)
    return Tank(direction, position)
