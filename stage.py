from pico2d import *


class Stage:
    def __init__(self):
        self.image = load_image('stage1.png')

    def draw(self):
        self.image.draw(400, 300)