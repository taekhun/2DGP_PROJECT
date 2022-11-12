from pico2d import *


class Stage:
    def __init__(self):
        self.image = load_image('stage_1.png')
        # self.font = load_font('ENCR10B.TTF', 16)

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 300)
        # draw_rectangle(*self.get_bb())
        # self.font.draw(100, 550, f'(Time: {get_time():.2f})', (255, 0, 0))

    # def get_bb(self):
    #     return 0, 0, 365 - 1, 40
    #
    # def handle_collision(self, other, group):
    #     pass
