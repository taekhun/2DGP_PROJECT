from pico2d import *


class Stage_2:
    def __init__(self):
        self.image = load_image('stage_2.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 300)
