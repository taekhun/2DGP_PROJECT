from pico2d import *
import game_world


class Star:
    image = None

    def __init__(self, x = 800, y = 300, velocity = 1):
        if Star.image == None:
            Star.image = load_image('attack.png')
        self.x, self.y, self.velocity, self.RL_direction, self.UD_direction = x, y, velocity, 0, 0

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        if self.RL_direction == 1 or self.RL_direction == -1:
            self.x += self.velocity
        elif self.UD_direction == 1 or self.UD_direction == -1:
            self.y += self.velocity
        if self.x < 20 or self.x > 800 - 20 or self.y < 20 or self.y > 600 - 20:
            game_world.remove_object(self)

    def get_direction(self, cur_RL_dir, cur_UD_dir):
        self.RL_direction = cur_RL_dir
        self.UD_direction = cur_UD_dir
