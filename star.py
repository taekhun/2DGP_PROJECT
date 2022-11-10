from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 40.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0) / 60.0
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


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
            self.x += self.velocity * RUN_SPEED_PPS * game_framework.frame_time
        elif self.UD_direction == 1 or self.UD_direction == -1:
            self.y += self.velocity * RUN_SPEED_PPS * game_framework.frame_time
        if self.x < 20 or self.x > 800 - 20 or self.y < 20 or self.y > 600 - 20:
            game_world.remove_object(self)

    def get_direction(self, cur_RL_dir, cur_UD_dir):
        self.RL_direction = cur_RL_dir
        self.UD_direction = cur_UD_dir
