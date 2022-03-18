from attempt_1.old_graphics import *
from attempt_1.old_VectorFuncs import *

DIR_UP = 0
DIR_RIGHT = 1
DIR_DOWN = 2
DIR_LEFT = 3
SHOOT = 5
DIR_NONE = -1

DIR_OPPOSITE = {
    DIR_UP: DIR_DOWN,
    DIR_DOWN: DIR_UP,
    DIR_RIGHT: DIR_LEFT,
    DIR_LEFT: DIR_RIGHT,
    DIR_NONE: DIR_NONE,
}

DIR_TO_XY = {
    DIR_UP: (0, -1),
    DIR_RIGHT: (1, 0),
    DIR_DOWN: (0, 1),
    DIR_LEFT: (-1, 0),
    DIR_NONE: (0, 0),
}

DIR_CLOCKWISE = {
    DIR_UP: DIR_RIGHT,
    DIR_RIGHT: DIR_DOWN,
    DIR_DOWN: DIR_LEFT,
    DIR_LEFT: DIR_UP,
}

ANG_LEFT_UP = 0
ANG_UP_RIGHT = 1
ANG_RIGHT_DOWN = 2
ANG_DOWN_LEFT = 3

ANG_TO_DIRS = {
    ANG_LEFT_UP: (DIR_LEFT, DIR_UP),
    ANG_UP_RIGHT: (DIR_UP, DIR_RIGHT),
    ANG_RIGHT_DOWN: (DIR_RIGHT, DIR_DOWN),
    ANG_DOWN_LEFT: (DIR_DOWN, DIR_LEFT),
}

ANIMATE_AFTER_NUM_FRAMES = 8

# MOVE_UP = ()

image_dict = init_graphics()


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
    images = image_dict["laser"]  # laser_sprites[DIR in][DIR our]["red/green"]

    def __init__(self):
        self.exists = False
        self.colour = "red"
        self.dir = DIR_NONE
        self.from_direction = DIR_NONE
        self.frames = [self.images["blank"]]
        LTSprite.__init__(self, (0, 0))

    def update(self):
        if self.exists:
            self.from_direction = DIR_OPPOSITE[
                self.dir
            ]  # Save previous direction
            self.position = vec_add(self.position, DIR_TO_XY[self.dir])

            if self.gameboard.is_within_board(self.position):
                x, y = self.position
                interacting_item = self.gameboard.board_items[x][y]
                if interacting_item is not None:
                    self.dir = interacting_item.hit_with_laser(
                        self.from_direction
                    )
                else:
                    # Passing through an empty square
                    self.dir = DIR_OPPOSITE[self.from_direction]
                if self.dir == DIR_NONE:
                    self.die()
            else:
                self.die()
        self.update_frames()

    def update_frames(self):
        # self.frames = [ get_laser_frame(self.from_direction, self.dir, self.colour) ]
        if (
                not self.exists
                or self.from_direction == DIR_NONE
                or self.dir == DIR_NONE
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
    #             and self.from_direction != DIR_NONE
    #             and self.dir != DIR_NONE
    #     ):
    #         self.rect.topleft = square_to_pixels(self.position)
    #         surface.blit(self.image, self.rect.topleft)
    #         # LTSprite.draw(self, surface)
    #         # print(f"Laser drawn: {self.from_direction}_{self.dir}_{self.colour}")
    #     else:
    #         # Don't draw if not on screen or if just spawned (self.from_direction=DIR_NONE)
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
            self.from_direction = DIR_NONE
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
        item_on.momentum = DIR_NONE

    def obj_leaving(self):
        pass


class Grass(Terrain):
    frames = [image_dict["grass"]]

    def __init__(self, position):
        Terrain.__init__(self, position)


class Flag(Terrain):
    frames = [image_dict["flag_1"], image_dict["flag_2"], image_dict["flag_3"]]

    def __init__(self, position):
        Terrain.__init__(self, position)

    def effect(self, item_on):
        if isinstance(item_on, Tank):
            self.gameboard.win()


class Water(Terrain):
    frames = [image_dict["water_1"], image_dict["water_2"], image_dict["water_3"]]

    def __init__(self, position):
        Terrain.__init__(self, position)

    def effect(self, item_on):
        item_on.momentum = DIR_NONE
        if isinstance(item_on, Tank):
            self.gameboard.game_over()
        elif isinstance(item_on, Block):
            x, y = self.position
            self.gameboard.ground[x][y] = Bridge((x, y))
        item_on.destroy()


class Conveyor(Terrain):
    def __init__(self, direction, position):
        self.dir = direction
        if self.dir == DIR_UP:
            self.frames = [
                image_dict["conveyor_up_1"],
                image_dict["conveyor_up_2"],
                image_dict["conveyor_up_3"],
            ]
        elif self.dir == DIR_RIGHT:
            self.frames = [
                image_dict["conveyor_right_1"],
                image_dict["conveyor_right_2"],
                image_dict["conveyor_right_3"],
            ]
        elif self.dir == DIR_DOWN:
            self.frames = [
                image_dict["conveyor_down_1"],
                image_dict["conveyor_down_2"],
                image_dict["conveyor_down_3"],
            ]
        elif self.dir == DIR_LEFT:
            self.frames = [
                image_dict["conveyor_left_1"],
                image_dict["conveyor_left_2"],
                image_dict["conveyor_left_3"],
            ]
        Terrain.__init__(self, position)

    def effect(self, item_on):
        if isinstance(item_on, Tank):
            item_on.push(self.dir)


class Ice(Terrain):
    frames = [image_dict["ice"]]

    def __init__(self, position):
        Terrain.__init__(self, position)

    def effect(self, item_on):
        # Keep current momentum
        pass


class ThinIce(Terrain):
    frames = [image_dict["ice_thin"]]

    def __init__(self, position):
        Terrain.__init__(self, position)

    def effect(self, item_on):
        # Keep current momentum
        pass

    def obj_leaving(self):
        x, y = self.position
        self.gameboard.ground[x][y] = Water((x, y))


class Bridge(Terrain):
    frames = [image_dict["bridge"]]

    def __init__(self, position):
        Terrain.__init__(self, position)


class Tunnel(Terrain):
    links = {}  # { id:[tunnel_a, tunnel_b, ...], id:[tunnel_c, ...], ... }
    id_colours = [
        pygame.Color(0xFF0000FF),
        pygame.Color(0x00FF00FF),
        pygame.Color(0x0000FFFF),
        pygame.Color(0x00FFFFFF),
        pygame.Color(0x00FFFFFF),
        pygame.Color(0xFF00FFFF),
        pygame.Color(0xFFFFFFFF),
        pygame.Color(0x808080FF),
    ]

    def __init__(self, tunnel_id, position):
        uncoloured_sprite = image_dict["teleport"]
        coloured_sprite = pygame.Surface.copy(uncoloured_sprite)
        coloured_sprite.fill(self.id_colours[tunnel_id])
        coloured_sprite.blit(uncoloured_sprite, (0, 0))
        self.frames = [coloured_sprite]

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
        # TODO: Search for open exit or set as waiting
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
                if self.gameboard.board_items[x][y] is None:  # is unblocked?
                    item_on.teleport((x, y))  # Teleport
                    return
            # Only blocked exit(s) so set tunnel as waiting
            # will transport when another tunnel is unblocked        
            self.waiting = True

    def get_exits(self):
        return [link for link in Tunnel.links[self.tunnel_id] if link is not self]

    def get_item_waiting(self):
        x, y = self.position
        if self.gameboard.board_items[x][y] is not None:
            return self.gameboard.board_items[x][y]
        elif self.gameboard.board_tank.position == (x, y):
            return self.gameboard.board_tank
        else:
            print('Tunnel error')
            return None

    def obj_leaving(self):
        x, y = self.position
        if self.gameboard.board_items[x][y] is None and self.gameboard.board_tank.position != (x, y):
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
            DIR_UP: True,
            DIR_RIGHT: True,
            DIR_DOWN: True,
            DIR_LEFT: True,
        }
        self.momentum = DIR_NONE
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
        self.momentum = DIR_NONE
        orig_x, orig_y = self.position
        dest_x, dest_y = destination
        if not isinstance(self, Tank):
            self.gameboard.board_items[orig_x][orig_y] = NoneObject(self.position)
            assert self.gameboard.board_items[dest_x][dest_y] == None, "Can't move item into occupied space!"
            self.gameboard.board_items[dest_x][dest_y] = self
        self.position = destination

    def set_position(self, destination):
        orig_x, orig_y = self.position
        dest_x, dest_y = destination
        if not isinstance(self, Tank):
            self.gameboard.board_items[orig_x][orig_y] = NoneObject(self.position)
            assert self.gameboard.board_items[dest_x][dest_y] == None, "Can't move item into occupied space!"
            self.gameboard.board_items[dest_x][dest_y] = self
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
        destination = vec_add(self.position, DIR_TO_XY[self.momentum])
        if self.gameboard.can_move_into(destination):
            self.set_position(destination)
        else:
            self.momentum = DIR_NONE

    def hit_with_laser(self, from_direction):
        # Hit this item with a laser from the direction, return exiting direction
        assert False, f"Hit with Laser not implemented for {type(self)}!"

    # def resolve_terrain_effect(self):
    #     x, y = self.position
    #     self.gameboard.ground[x][y].effect(self)
    # 
    # def sink(self):
    #     self.destroy()


class RotatableItem:
    images = {DIR_UP: [], DIR_RIGHT: [], DIR_DOWN: [], DIR_LEFT: []}

    def rotate(self, direction):
        self.dir = direction
        self.update_frames()

    def update_frames(self):
        self.frames = self.images[self.dir]
        self.image = self.frames[0]


class Tank(Item, RotatableItem):
    images = {
        DIR_UP: [image_dict["tank_up"]],
        DIR_RIGHT: [image_dict["tank_right"]],
        DIR_DOWN: [image_dict["tank_down"]],
        DIR_LEFT: [image_dict["tank_left"]],
    }

    def __init__(self, direction, position):
        self.dir = direction
        self.update_frames()
        self.alive = True
        self.firing = False
        Item.__init__(self, position)

    def shoot(self):
        self.gameboard.board_laser.fire(self.position, self.dir, good=True)

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
    frames = [image_dict["solid"]]

    def __init__(self, position):
        Item.__init__(self, position)

    def hit_with_laser(self, from_direction):
        return DIR_NONE


class Block(Item):
    frames = [image_dict["block"]]

    def __init__(self, position):
        Item.__init__(self, position)

    def hit_with_laser(self, from_direction):
        # Hit this item with a laser from the direction, return exiting direction
        self.push(DIR_OPPOSITE[from_direction])
        return DIR_NONE


class Wall(Item):
    frames = [image_dict["wall"]]

    def __init__(self, position):
        Item.__init__(self, position)

    def hit_with_laser(self, from_direction):
        self.destroy()
        return DIR_NONE


class Antitank(Item, RotatableItem):
    images = {
        DIR_UP: [
            image_dict["antitank_up_1"],
            image_dict["antitank_up_2"],
            image_dict["antitank_up_3"],
        ],
        DIR_RIGHT: [
            image_dict["antitank_right_1"],
            image_dict["antitank_right_2"],
            image_dict["antitank_right_3"],
        ],
        DIR_DOWN: [
            image_dict["antitank_down_1"],
            image_dict["antitank_down_2"],
            image_dict["antitank_down_3"],
        ],
        DIR_LEFT: [
            image_dict["antitank_left_1"],
            image_dict["antitank_left_2"],
            image_dict["antitank_left_3"],
        ],
    }
    dead_images = {
        DIR_UP: [image_dict["antitank_up_dead"], ],
        DIR_RIGHT: [image_dict["antitank_right_dead"], ],
        DIR_DOWN: [image_dict["antitank_down_dead"], ],
        DIR_LEFT: [image_dict["antitank_left_dead"], ],
    }

    def __init__(self, direction, position):
        self.dir = direction
        self.alive = True
        self.firing = False
        self.update_frames()
        Item.__init__(self, position)
        self.movable[DIR_OPPOSITE[self.dir]] = False

    def die(self):
        self.alive = False
        self.images = self.dead_images
        self.movable = {
            DIR_UP: False,
            DIR_RIGHT: False,
            DIR_DOWN: False,
            DIR_LEFT: False,
        }
        self.update_frames()

    def hit_with_laser(self, from_direction):
        if not self.alive:
            return DIR_NONE

        if from_direction == self.dir:
            self.die()
            return DIR_NONE
        else:
            self.push(DIR_OPPOSITE[from_direction])
            return DIR_NONE

    def shoot(self):
        self.gameboard.board_laser.fire(self.position, self.dir, good=False)


class Mirror(Item, RotatableItem):
    images = {
        DIR_UP: [image_dict["mirror_left_up"]],
        DIR_RIGHT: [image_dict["mirror_up_right"]],
        DIR_DOWN: [image_dict["mirror_right_down"]],
        DIR_LEFT: [image_dict["mirror_down_left"]],
    }

    def __init__(self, angle, position):
        self.dir = angle
        self.alive = True
        self.firing = False
        self.update_frames()
        Item.__init__(self, position)

    def hit_with_laser(self, from_direction):
        dir1, dir2 = ANG_TO_DIRS[self.dir]
        if from_direction == dir1:
            return dir2
        elif from_direction == dir2:
            return dir1
        else:
            self.push(DIR_OPPOSITE[from_direction])
            return DIR_NONE


class Glass(Item):
    frames = [image_dict["glass"]]
    movable = {
        DIR_UP: False,
        DIR_RIGHT: False,
        DIR_DOWN: False,
        DIR_LEFT: False,
    }

    def __init__(self, position):
        Item.__init__(self, position)

    def hit_with_laser(self, from_direction):
        # Hit this item with a laser from the direction, return exiting direction
        return DIR_OPPOSITE[from_direction]


class RotMirror(Item, RotatableItem):
    images = {
        DIR_UP: [image_dict["rotmirror_left_up"]],
        DIR_RIGHT: [image_dict["rotmirror_up_right"]],
        DIR_DOWN: [image_dict["rotmirror_right_down"]],
        DIR_LEFT: [image_dict["rotmirror_down_left"]],
    }
    movable = {
        DIR_UP: False,
        DIR_RIGHT: False,
        DIR_DOWN: False,
        DIR_LEFT: False,
    }

    def __init__(self, angle, position):
        self.dir = angle
        self.alive = True
        self.firing = False
        self.update_frames()
        Item.__init__(self, position)

    def hit_with_laser(self, from_direction):
        dir1, dir2 = ANG_TO_DIRS[self.dir]
        if from_direction == dir1:
            return dir2
        elif from_direction == dir2:
            return dir1
        else:
            self.rotate(DIR_CLOCKWISE[self.dir])
            return DIR_NONE
