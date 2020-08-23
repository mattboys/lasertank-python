import Direction


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

    def pack(self):
        """ Return minimal dict to save game state when idle"""
        attributes = dict([(k, v) for k, v in self.__dict__.items() if not k.startswith("_") and k not in ["gameboard",
                                                                                                           "position"]])
        return type(self).__name__, attributes


class Laser(LaserTankObject):

    def __init__(self, exists=False, colour="red", direction=Direction.NONE, from_direction=Direction.NONE,
                 position=(0, 0)):
        self.exists = exists
        self.colour = colour
        self.direction = direction
        self.from_direction = from_direction
        LaserTankObject.__init__(self, position)

    def update(self):
        if self.exists:
            self.from_direction = Direction.get_opposite(self.direction)  # Save previous direction

            # Reset any glowing glass previously under laser
            previous_interacting_item = self.gameboard.get_item(self.position)
            if isinstance(previous_interacting_item, Glass):
                previous_interacting_item.colour = 'none'

            self.position = vec_add(self.position, Direction.get_xy(self.direction))

            if self.gameboard.is_within_board(self.position):
                interacting_item = self.gameboard.get_tank_or_item(self.position)
                self.direction = interacting_item.hit_with_laser(
                    self.from_direction
                )
                if self.direction == Direction.NONE:
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
            self.direction = direction
            self.from_direction = Direction.NONE
            if good:
                self.colour = "green"
            else:
                self.colour = "red"
            return True

    def die(self):
        self.exists = False

    def pack(self):
        """ Return minimal dict to save game state when idle"""
        obj_name, attributes = LaserTankObject.pack(self)
        attributes["position"] = self.position
        return obj_name, attributes



# Objects
class Item(LaserTankObject):

    def __init__(self, init_pos):
        LaserTankObject.__init__(self, init_pos)

    def destroy(self):
        self.gameboard.destroy_item(self.position)

    def hit_with_laser(self, from_direction):
        """ Hit this item with a laser from the direction, return exiting direction """
        return Direction.get_opposite(from_direction)


class ItemMovable(Item):
    def __init__(self, init_pos):
        self._momentum = Direction.NONE
        Item.__init__(self, init_pos)

    def push(self, direction):
        """ Assumes this object can legally move in direction, then set momentum and add to gameboard.sliding list """
        self._momentum = direction
        self.gameboard.start_sliding(self)

    def resolve_momentum(self):
        destination = vec_add(self.position, Direction.get_xy(self._momentum))
        if self.gameboard.can_move_into(destination):
            # Set new position
            original_position = self.position
            if not isinstance(self, Tank):
                self.gameboard.put_item(original_position, Empty(original_position))
                assert self.gameboard.is_square_empty(destination), "Can't move item into occupied space!"
                self.gameboard.put_item(destination, self)
            self.position = destination
            # Resolve effects on terrain
            self.gameboard.get_terrain(original_position).obj_leaving()
            self.gameboard.get_terrain(destination).effect(self)
        else:
            self._momentum = Direction.NONE
            self.gameboard.get_terrain(self.position).effect(self)

    def teleport(self, destination):
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

    def pack(self):
        """ Return minimal dict to save game state when idle"""
        obj_name, attributes = LaserTankObject.pack(self)
        attributes["position"] = self.position
        return obj_name, attributes


class Solid(Item):
    def __init__(self, position):
        Item.__init__(self, position)

    def hit_with_laser(self, from_direction):
        return Direction.NONE


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


class Wall(Item):
    def __init__(self, position):
        Item.__init__(self, position)

    def hit_with_laser(self, from_direction):
        self.destroy()
        return Direction.NONE


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


class AntitankDead(Item):
    def __init__(self, direction, position):
        self.direction = direction
        Item.__init__(self, position)

    def hit_with_laser(self, from_direction):
        return Direction.NONE


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


class Glass(Item):

    def __init__(self, position):
        Item.__init__(self, position)
        self._colour = 'none'

    def hit_with_laser(self, from_direction):
        # Hit this item with a laser from the direction, return exiting direction
        self._colour = self.gameboard.get_laser().colour
        return Direction.get_opposite(from_direction)


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


class Terrain(LaserTankObject):
    def __init__(self, init_pos):
        LaserTankObject.__init__(self, init_pos)

    def effect(self, item_on):
        item_on._momentum = Direction.NONE

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
        item_on._momentum = Direction.NONE
        if isinstance(item_on, Tank):
            raise GameOver
        elif isinstance(item_on, Block):
            self.gameboard.put_terrain(self.position, Bridge(self.position))
        item_on.destroy()


class Conveyor(Terrain):
    def __init__(self, direction, position):
        self.direction = direction
        Terrain.__init__(self, position)

    def effect(self, item_on):
        if isinstance(item_on, Tank):
            item_on.push(self.direction)


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
        self.gameboard.put_terrain(self.position, Water(self.position))
        # TODO: Tank should sink next tick if stopped on thin ice


class Bridge(Terrain):
    def __init__(self, position):
        Terrain.__init__(self, position)


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
                    item_on.teleport(exit_tunnel.position)  # Teleport
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
        constants.Mirror_NW: ("Mirror", Direction.N),
        constants.Mirror_NE: ("Mirror", Direction.E),
        constants.Mirror_SE: ("Mirror", Direction.S),
        constants.Mirror_SW: ("Mirror", Direction.W),
        constants.Glass: ("Glass", None),
        constants.RotMirror_NW: ("RotMirror", Direction.N),
        constants.RotMirror_NE: ("RotMirror", Direction.E),
        constants.RotMirror_SE: ("RotMirror", Direction.S),
        constants.RotMirror_SW: ("RotMirror", Direction.W),
    }
    obj, param = mapping[object_string]
    if param is None:
        return getattr(__import__("sprites"), obj)(position)
    else:
        return getattr(__import__("sprites"), obj)(param, position)


def unpack(obj_name, params_dict):
    """ Return an object from the packed version
    obj_name: str representation of the object name
    params_dict: dictionary of object parameters to use in constructor
     i.e.: unpack("Conveyor", {'direction': 'S', 'position': (9, 14)}) """
    return getattr(__import__("sprites"), obj_name)(**params_dict)
