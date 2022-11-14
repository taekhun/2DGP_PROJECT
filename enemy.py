from pico2d import *
import random
import game_framework
import game_world

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0) / 60.0
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Enemy:
    image = None

    def __init__(self):
        if Enemy.image == None:
            Enemy.image = load_image('turtle_1.png')
        self.frame = random.randint(0, 7)
        self.x = random.randint(380, 430)
        self.y = 600
        self.move_speed = 0.5

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.y -= self.move_speed * RUN_SPEED_PPS * game_framework.frame_time
        if self.y < 0:
            game_world.remove_object(self)

    def draw(self):
        self.image.clip_draw(int(self.frame) * 32, 32 * 3, 32, 32, self.x, self.y)
        # draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 10, self.y + 15

    def handle_collision(self, other, group):
        if group == 'star:enemies':
            game_world.remove_object(self)
        # if group == 'character:enemies':
        #     game_world.remove_object(self)
