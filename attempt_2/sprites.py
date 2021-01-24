from attempt_2 import Direction


class Solved(Exception):
    pass


class GameOver(Exception):
    pass


def vec_add(a: tuple, b: tuple):
    return a[0] + b[0], a[1] + b[1]


class LaserTankObject:
    _gameboard = None

    def __init__(self, position):
        self.position = position

    def pack(self):
        """ Return minimal dict to save game state when idle"""
        attributes = dict([(k, v) for k, v in self.__dict__.items() if not k.startswith("_")])
        return type(self).__name__, attributes

    def resolve_momentum(self):
        """ Momentum only should apply to ItemMovable objects """
        pass


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

            if self._gameboard.is_within_board(self.position):
                interacting_item = self._gameboard.get_tank_or_item(self.position)
                self.direction = interacting_item.hit_with_laser(
                    self.from_direction
                )
                if self.direction == Direction.NONE:
                    self.die()

                # Implement the LaserBounceOnIce logic where the laser moves twice if reflecting on a sliding mirror
                if self.exists and self._gameboard.is_sliding(interacting_item):
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


# Objects
class Item(LaserTankObject):

    def __init__(self, init_pos):
        LaserTankObject.__init__(self, init_pos)

    def destroy(self):
        self._gameboard.destroy_item(self.position)

    def hit_with_laser(self, from_direction):
        """ Hit this item with a laser from the direction, return exiting direction """
        return Direction.get_opposite(from_direction)


class ItemMovable(Item):
    def __init__(self, init_pos):
        self.momentum = Direction.NONE
        Item.__init__(self, init_pos)

    def push(self, direction):
        """ Assumes this object can legally move in direction, then set momentum and add to gameboard.sliding list """
        self.momentum = direction
        self._gameboard.start_sliding(self)

    def resolve_momentum(self):
        destination = vec_add(self.position, Direction.get_xy(self.momentum))
        if self._gameboard.can_move_into(destination):
            # Set new position
            original_position = self.position
            if not isinstance(self, Tank):
                self._gameboard.put_item(original_position, Empty(original_position))
                assert self._gameboard.is_square_empty(destination), "Can't move item into occupied space!"
                self._gameboard.put_item(destination, self)
            self.position = destination
            # Resolve effects on terrain
            self._gameboard.get_terrain(original_position).obj_leaving()
            self._gameboard.get_terrain(destination).effect(self)
        else:
            self.momentum = Direction.NONE
            self._gameboard.get_terrain(self.position).effect(self)

    def teleport(self, destination):
        if not isinstance(self, Tank):
            self._gameboard.put_item(self.position, Empty(self.position))
            assert self._gameboard.is_square_empty(destination), "Can't move item into occupied space!"
            self._gameboard.put_item(destination, self)
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
        self._gameboard.get_laser().fire(self.position, self.direction, good=True)

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
        self._gameboard.start_sliding(self)


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
            self._gameboard.put_item(self.position, AntitankDead(self.direction, self.position))
            return Direction.NONE
        else:
            self.push(Direction.get_opposite(from_direction))
            return Direction.NONE

    def shoot(self):
        self._gameboard.get_laser().fire(self.position, self.direction, good=False)


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
        # self._colour = 'none'

    def hit_with_laser(self, from_direction):
        # Hit this item with a laser from the direction, return exiting direction
        # self._colour = self.gameboard.get_laser().colour
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
            self._gameboard.put_terrain(self.position, Bridge(self.position))
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
        self._gameboard.put_terrain(self.position, Water(self.position))


class Bridge(Terrain):
    def __init__(self, position):
        Terrain.__init__(self, position)


class Tunnel(Terrain):

    def __init__(self, id, position, waiting=False):
        Terrain.__init__(self, position)
        self.id = id
        self.waiting = waiting  # Waiting for an open exit

    def _get_exits(self):
        exits = self._gameboard.get_tunnels(self.id)
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
                if self._gameboard.is_square_empty(exit_tunnel.position):  # is unblocked?
                    item_on.teleport(exit_tunnel.position)  # Teleport
                    return
            # Only blocked exit(s) so set tunnel as waiting
            # will transport when another tunnel is unblocked
            self.waiting = True

    def release(self):
        """ Was waiting and now an exit is free """
        self.waiting = False
        if not self._gameboard.is_square_empty(self.position):
            return self._gameboard.get_item(self.position)
        elif self._gameboard.board_tank.position == self.position:
            return self._gameboard.get_tank()
        else:
            print('Tunnel error')
            return None

    def obj_leaving(self):
        if self._gameboard.is_square_empty(self.position) and self._gameboard.get_tank().position != self.position:
            self.waiting = False
        for link in self._get_exits():
            if link.waiting:
                link.release()
                # Only release first waiting instance
                return


def unpack(packed_gameobj: tuple, position=None) -> LaserTankObject:
    obj_name = packed_gameobj[0]
    attributes = packed_gameobj[1] if len(packed_gameobj) > 1 else {}
    # Inject position attribute if provided
    if position is not None:
        attributes.update({"position": position})
    print(f"Unpacking {obj_name}(**{attributes})")
    constructor = globals()[obj_name]
    return constructor(**attributes)
