from enum import Enum

from old_graphics import *
from old_VectorFuncs import *

image_dict = init_graphics()


def get_frames(name):
    return image_dict[name]


SPRITE_SIZE = 32
ANIMATE_AFTER_NUM_FRAMES = 8

GameBoardOffsetX = 0
GameBoardOffsetY = 0
GameBoardWidth = SPRITE_SIZE * 16 + 2 * GameBoardOffsetX
GameBoardHeight = SPRITE_SIZE * 16 + 2 * GameBoardOffsetY


def square_to_pixels(square):
    x, y = square
    return (GameBoardOffsetX + x * SPRITE_SIZE, GameBoardOffsetY + y * SPRITE_SIZE)


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


def NoneObject(position):
    return None


class LTSprite(pygame.sprite.Sprite):
    frames = []
    gameboard = None
    animation_frame_counter = 0

    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        assert len(self.frames) > 0, "Sprite loaded without any animation frames!"
        self.image = self.frames[0]
        self.animation_index = 0
        self.position = position
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = square_to_pixels(self.position)

    def draw(self, surface):
        # Animate every X frames by loading frames[i] into image
        self.animation_frame_counter += 1
        if self.animation_frame_counter >= ANIMATE_AFTER_NUM_FRAMES:
            self.animation_frame_counter = 0
            self.animation_index = (self.animation_index + 1) % len(self.frames)
            self.image = self.frames[self.animation_index]

        self.rect.topleft = square_to_pixels(self.position)
        surface.blit(self.image, self.rect.topleft)


class Laser(LTSprite):
    images = get_frames("laser")  # laser_sprites[DIR in][DIR out]["red/green"]

    def __init__(self):
        self.exists = False
        self.colour = "red"
        self.dir = Direction.NONE
        self.from_direction = Direction.NONE
        self.frames = [self.images["blank"]]
        LTSprite.__init__(self, (0, 0))

    def update(self):
        if self.exists:
            self.from_direction = Direction.get_opposite(self.dir)  # Save previous direction
            self.position = vec_add(self.position, Direction.get_xy(self.dir))

            if self.gameboard.is_within_board(self.position):
                x, y = self.position
                interacting_item = self.gameboard.items[x][y]
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
        self.update_frames()

    def update_frames(self):
        # self.frames = [ get_laser_frame(self.from_direction, self.dir, self.colour) ]
        if (
                not self.exists
                or self.from_direction == Direction.NONE
                or self.dir == Direction.NONE
        ):
            self.frames = [self.images["blank"]]
            # print('Laser Frame: blank')
        else:
            self.frames = [self.images[f"{self.from_direction}_{self.dir}_{self.colour}"]]
            # self.images[self.from_direction][self.dir][self.colour]
            # print(f"Laser Frame: {self.from_direction}_{self.dir}_{self.colour}")
        self.image = self.frames[0]

    # def draw(self, surface):
    #     if (
    #             self.exists
    #             and self.from_direction != DIR.NONE
    #             and self.dir != DIR.NONE
    #     ):
    #         self.rect.topleft = square_to_pixels(self.position)
    #         surface.blit(self.image, self.rect.topleft)
    #         # LTSprite.draw(self, surface)
    #         # print(f"Laser drawn: {self.from_direction}_{self.dir}_{self.colour}")
    #     else:
    #         # Don't draw if not on screen or if just spawned (self.from_direction=DIR.NONE)
    #         pass

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
    frames = get_frames("grass")

    def __init__(self, position):
        Terrain.__init__(self, position)


class Flag(Terrain):
    frames = get_frames("flag")

    def __init__(self, position):
        Terrain.__init__(self, position)

    def effect(self, item_on):
        if isinstance(item_on, Tank):
            self.gameboard.win()


class Water(Terrain):
    frames = get_frames("water")

    def __init__(self, position):
        Terrain.__init__(self, position)

    def effect(self, item_on):
        item_on.momentum = Direction.NONE
        if isinstance(item_on, Tank):
            self.gameboard.game_over()
        elif isinstance(item_on, Block):
            x, y = self.position
            self.gameboard.ground[x][y] = Bridge((x, y))
        item_on.destroy()


class Conveyor(Terrain):
    def __init__(self, direction, position):
        self.dir = direction
        self.frames = get_frames("conveyor" + self.dir)
        Terrain.__init__(self, position)

    def effect(self, item_on):
        if isinstance(item_on, Tank):
            item_on.push(self.dir)


class Ice(Terrain):
    frames = get_frames("ice")

    def __init__(self, position):
        Terrain.__init__(self, position)

    def effect(self, item_on):
        # Keep current momentum
        pass


class ThinIce(Terrain):
    frames = get_frames("ice_thin")

    def __init__(self, position):
        Terrain.__init__(self, position)

    def effect(self, item_on):
        # Keep current momentum
        pass

    def obj_leaving(self):
        x, y = self.position
        self.gameboard.ground[x][y] = Water((x, y))


class Bridge(Terrain):
    frames = get_frames("bridge")

    def __init__(self, position):
        Terrain.__init__(self, position)


class Tunnel(Terrain):
    links = {}  # { id:[tunnel_a, tunnel_b, ...], id:[tunnel_c, ...], ... }

    def __init__(self, tunnel_id, position):
        self.frames = get_frames("teleport_{tunnel_id}")
        Terrain.__init__(self, position)
        self.tunnel_id = tunnel_id
        if self.tunnel_id not in Tunnel.links:
            Tunnel.links[self.tunnel_id] = []
        Tunnel.links[self.tunnel_id].append(self)
        Tunnel.links[self.tunnel_id].sort(
            key=lambda temp_tunnel: (temp_tunnel.position[1], temp_tunnel.position[0])
        )  # Sort by y, x
        self.waiting = False  # Waiting for an open exit

    def effect(self, item_on):
        # Search for open exit
        exits = self.get_exits()
        if len(exits) == 0:
            # Black Hole
            item_on.destroy()
            return
        else:
            # Find an unblocked exit
            for link in exits:
                x, y = link.position
                if self.gameboard.items[x][y] is None:  # is unblocked?
                    item_on.teleport((x, y))  # Teleport
                    return
            # Only blocked exit(s) so set tunnel as waiting
            # will transport when another tunnel is unblocked
            self.waiting = True

    def get_exits(self):
        return [link for link in Tunnel.links[self.tunnel_id] if link is not self]

    def get_item_waiting(self):
        x, y = self.position
        if self.gameboard.items[x][y] is not None:
            return self.gameboard.items[x][y]
        elif self.gameboard.tank.position == (x, y):
            return self.gameboard.tank
        else:
            print('Tunnel error')
            return None

    def obj_leaving(self):
        x, y = self.position
        if self.gameboard.items[x][y] is None and self.gameboard.tank.position != (x, y):
            self.waiting = False
        for link in self.get_exits():
            if link.waiting:
                link.waiting = False
                link.effect(link.get_item_waiting())
                return


# Objects
class Item(LTSprite):
    def __init__(self, init_pos):
        self.movable = {
            Direction.N: True,
            Direction.E: True,
            Direction.S: True,
            Direction.W: True,
        }
        self.momentum = Direction.NONE
        if not isinstance(self.frames, list) or len(self.frames) == 0:
            print("Frame error")
        LTSprite.__init__(self, init_pos)

    # def teleport(self, exit_list):
    #     if len(exit_list) == 0:
    #         self.destroy()  # Black hole
    #     else:
    #         for exit in exit_list:
    #             # TODO: Move object to unblocked exit
    #             pass

    def teleport(self, destination):
        self.momentum = Direction.NONE
        orig_x, orig_y = self.position
        dest_x, dest_y = destination
        if not isinstance(self, Tank):
            self.gameboard.items[orig_x][orig_y] = NoneObject(self.position)
            assert self.gameboard.items[dest_x][dest_y] == None, "Can't move item into occupied space!"
            self.gameboard.items[dest_x][dest_y] = self
        self.position = destination

    def set_position(self, destination):
        orig_x, orig_y = self.position
        dest_x, dest_y = destination
        if not isinstance(self, Tank):
            self.gameboard.items[orig_x][orig_y] = NoneObject(self.position)
            assert self.gameboard.items[dest_x][dest_y] == None, "Can't move item into occupied space!"
            self.gameboard.items[dest_x][dest_y] = self
        self.position = destination
        # Resolve effects on terrain
        self.gameboard.ground[orig_x][orig_y].obj_leaving()
        self.gameboard.ground[dest_x][dest_y].effect(self)

    def destroy(self):
        self.gameboard.destroy_item(self.position)

    def push(self, direction):
        # Apply and resolve a force on an object
        if self.movable[direction]:
            self.momentum = direction
            if self not in self.gameboard.sliding_items:
                self.gameboard.sliding_items.append(self)
            return True
        else:
            return False

    def resolve_momentum(self):
        destination = vec_add(self.position, Direction.get_xy(self.momentum))
        if self.gameboard.can_move_into(destination):
            self.set_position(destination)
        else:
            self.momentum = Direction.NONE

    def hit_with_laser(self, from_direction):
        # Hit this item with a laser from the direction, return exiting direction
        assert False, f"Hit with Laser not implemented for {type(self)}!"

    # def resolve_terrain_effect(self):
    #     x, y = self.position
    #     self.gameboard.ground[x][y].effect(self)
    #
    # def sink(self):
    #     self.destroy()


class DirectionalItem:
    images = {Direction.N: [], Direction.E: [], Direction.S: [], Direction.W: []}

    def rotate(self, direction):
        self.dir = direction
        self.update_frames()

    def update_frames(self):
        self.frames = self.images[self.dir]
        self.image = self.frames[0]


class Tank(Item, DirectionalItem):
    images = {
        Direction.N: [get_frames("tank_up")],
        Direction.E: [get_frames("tank_right")],
        Direction.S: [get_frames("tank_down")],
        Direction.W: [get_frames("tank_left")],
    }

    def __init__(self, direction, position):
        self.dir = direction
        self.update_frames()
        self.alive = True
        self.firing = False
        Item.__init__(self, position)

    def shoot(self):
        self.gameboard.laser.fire(self.position, self.dir, good=True)

    def destroy(self):
        self.gameboard.game_over()

    def update(self):
        x, y = self.position
        self.gameboard.ground[x][y].effect()
        # TODO: Move based on momentum

    def hit_with_laser(self, from_direction):
        # Hit this item with a laser from the direction, return exiting direction
        self.gameboard.game_over()


class Solid(Item):
    frames = [get_frames("solid")]

    def __init__(self, position):
        Item.__init__(self, position)

    def hit_with_laser(self, from_direction):
        return Direction.NONE


class Block(Item):
    frames = [get_frames("block")]

    def __init__(self, position):
        Item.__init__(self, position)

    def hit_with_laser(self, from_direction):
        # Hit this item with a laser from the direction, return exiting direction
        self.push(Direction.get_opposite(from_direction))
        return Direction.NONE


class Wall(Item):
    frames = [get_frames("wall")]

    def __init__(self, position):
        Item.__init__(self, position)

    def hit_with_laser(self, from_direction):
        self.destroy()
        return Direction.NONE


class Antitank(Item, DirectionalItem):
    images = {
        Direction.N: [
            get_frames("antitank_up_1"),
            get_frames("antitank_up_2"),
            get_frames("antitank_up_3"),
        ],
        Direction.E: [
            get_frames("antitank_right_1"),
            get_frames("antitank_right_2"),
            get_frames("antitank_right_3"),
        ],
        Direction.S: [
            get_frames("antitank_down_1"),
            get_frames("antitank_down_2"),
            get_frames("antitank_down_3"),
        ],
        Direction.W: [
            get_frames("antitank_left_1"),
            get_frames("antitank_left_2"),
            get_frames("antitank_left_3"),
        ],
    }
    dead_images = {
        Direction.N: [get_frames("antitank_up_dead"), ],
        Direction.E: [get_frames("antitank_right_dead"), ],
        Direction.S: [get_frames("antitank_down_dead"), ],
        Direction.W: [get_frames("antitank_left_dead"), ],
    }

    def __init__(self, direction, position):
        self.dir = direction
        self.alive = True
        self.firing = False
        self.update_frames()
        Item.__init__(self, position)
        self.movable[Direction.get_opposite(self.dir)] = False

    def die(self):
        self.alive = False
        self.images = self.dead_images
        self.movable = {
            Direction.N: False,
            Direction.E: False,
            Direction.S: False,
            Direction.W: False,
        }
        self.update_frames()

    def hit_with_laser(self, from_direction):
        if not self.alive:
            return Direction.NONE

        if from_direction == self.dir:
            self.die()
            return Direction.NONE
        else:
            self.push(Direction.get_opposite(from_direction))
            return Direction.NONE

    def shoot(self):
        self.gameboard.laser.fire(self.position, self.dir, good=False)


class AntitankDead(Item, DirectionalItem):
    images = {
        Direction.N: [
            get_frames("antitank_up_1"),
            get_frames("antitank_up_2"),
            get_frames("antitank_up_3"),
        ],
        Direction.E: [
            get_frames("antitank_right_1"),
            get_frames("antitank_right_2"),
            get_frames("antitank_right_3"),
        ],
        Direction.S: [
            get_frames("antitank_down_1"),
            get_frames("antitank_down_2"),
            get_frames("antitank_down_3"),
        ],
        Direction.W: [
            get_frames("antitank_left_1"),
            get_frames("antitank_left_2"),
            get_frames("antitank_left_3"),
        ],
    }
    dead_images = {
        Direction.N: [get_frames("antitank_up_dead"), ],
        Direction.E: [get_frames("antitank_right_dead"), ],
        Direction.S: [get_frames("antitank_down_dead"), ],
        Direction.W: [get_frames("antitank_left_dead"), ],
    }

    def __init__(self, direction, position):
        self.dir = direction
        self.alive = True
        self.firing = False
        self.update_frames()
        Item.__init__(self, position)
        self.movable[Direction.get_opposite(self.dir)] = False

    def die(self):
        self.alive = False
        self.images = self.dead_images
        self.movable = {
            Direction.N: False,
            Direction.E: False,
            Direction.S: False,
            Direction.W: False,
        }
        self.update_frames()

    def hit_with_laser(self, from_direction):
        return Direction.NONE


class Mirror(Item, DirectionalItem):
    images = {
        Direction.N: [get_frames("mirror_left_up")],
        Direction.E: [get_frames("mirror_up_right")],
        Direction.S: [get_frames("mirror_right_down")],
        Direction.W: [get_frames("mirror_down_left")],
    }

    def __init__(self, angle, position):
        self.dir = angle
        self.alive = True
        self.firing = False
        self.update_frames()
        Item.__init__(self, position)

    def hit_with_laser(self, from_direction):
        dir1, dir2 = Angle.to_dirs(self.dir)
        if from_direction == dir1:
            return dir2
        elif from_direction == dir2:
            return dir1
        else:
            self.push(Direction.get_opposite(from_direction))
            return Direction.NONE


class Glass(Item):
    frames = [get_frames("glass")]
    movable = {
        Direction.N: False,
        Direction.E: False,
        Direction.S: False,
        Direction.W: False,
    }

    def __init__(self, position):
        Item.__init__(self, position)

    def hit_with_laser(self, from_direction):
        # Hit this item with a laser from the direction, return exiting direction
        return Direction.get_opposite(from_direction)


class RotMirror(Item, DirectionalItem):
    images = {
        Direction.N: [get_frames("rotmirror_left_up")],
        Direction.E: [get_frames("rotmirror_up_right")],
        Direction.S: [get_frames("rotmirror_right_down")],
        Direction.W: [get_frames("rotmirror_down_left")],
    }
    movable = {
        Direction.N: False,
        Direction.E: False,
        Direction.S: False,
        Direction.W: False,
    }

    def __init__(self, angle, position):
        self.dir = angle
        self.alive = True
        self.firing = False
        self.update_frames()
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
