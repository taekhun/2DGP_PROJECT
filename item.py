import random

from pico2d import *
import game_world
import server


class Item:
    image = None

    def __init__(self):
        if Item.image == None:
            Item.image = load_image('./png/special_attack.png')
        self.x, self.y = random.randint(0, 800), random.randint(40, 500)
        self.item_sound = load_wav('./sound/item.wav')
        self.item_sound.set_volume(32)
    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        # draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, other, group):
        if group == 'character:item':
            self.item_sound.play()
            game_world.remove_object(self)
            game_world.remove_turtle()
            game_world.remove_turtle_attack()
