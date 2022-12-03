from pico2d import *

import game_framework
import gameclear_state

class Stage:
    def __init__(self):
        self.image = load_image('./png/stage_1.png')
        self.timer = 60.0
        self.font = load_font('ENCR10B.TTF', 16)


    def update(self):
        self.timer -= game_framework.frame_time
        if self.timer <= 0:
            game_framework.push_state(gameclear_state)
        pass

    def draw(self):
        self.image.draw(400, 300)
        # draw_rectangle(*self.get_bb_1())
        # draw_rectangle(*self.get_bb_2())
        # draw_rectangle(*self.get_bb_3())
        # draw_rectangle(*self.get_bb_4())
        self.font.draw(100, 550, f'Time: {self.timer:.2f}', (255, 0, 0))

    def get_bb_1(self):
        return 0, 0, 365 - 2, 30

    def get_bb_2(self):
        return 440 + 1, 0, 800, 30

    def get_bb_3(self):
        return 0, 520, 365 - 2, 600

    def get_bb_4(self):
        return 440 + 1, 520, 800, 600

    def handle_collision(self, other, group):
        pass
