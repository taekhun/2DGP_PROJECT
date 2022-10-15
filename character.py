from pico2d import *


class Character:
    def __init__(self):
        self.running = True
        self.i = 13
        self.right = False
        self.up = False
        self.down = False
        self.left = False
        self.frame = 0
        self.lr_dir = 0  # 좌우
        self.ud_dir = 0  # 상하
        self.x, self.y = 400, 32
        self.frame = 0
        self.image = load_image('character.png')

    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                self.running = False
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_RIGHT:
                    self.lr_dir += 1
                    if not self.up and not self.down:
                        self.i = 5
                    if self.up:
                        self.i = 6
                    if self.down:
                        self.i = 4
                    self.right = True
                elif event.key == SDLK_LEFT:
                    self.lr_dir -= 1
                    if not self.up and not self.down:
                        self.i = 1
                    if self.up:
                        self.i = 0
                    if self.down:
                        self.i = 2
                    self.left = True
                elif event.key == SDLK_UP:
                    self.ud_dir += 1
                    if not self.right and not self.left:
                        self.i = 7
                    if self.right:
                        self.i = 6
                    if self.left:
                        self.i = 0
                    self.up = True
                elif event.key == SDLK_DOWN:
                    self.ud_dir -= 1
                    if not self.right and not self.left:
                        self.i = 3
                    elif self.right:
                        self.i = 4
                    elif self.left:
                        self.i = 2
                    self.down = True
                elif event.key == SDLK_ESCAPE:
                    self.running = False

            elif event.type == SDL_KEYUP:
                if event.key == SDLK_RIGHT:
                    self.lr_dir -= 1
                    if self.up:
                        self.i = 7
                    elif self.down:
                        self.i = 3
                    else:
                        self.i = 13
                    self.right = False
                elif event.key == SDLK_LEFT:
                    self.lr_dir += 1
                    if self.up:
                        self.i = 7
                    elif self.down:
                        self.i = 3
                    else:
                        self.i = 9
                    self.left = False
                elif event.key == SDLK_UP:
                    self.ud_dir -= 1
                    if self.right:
                        self.i = 5
                    elif self.left:
                        self.i = 1
                    else:
                        self.i = 15
                    self.up = False
                elif event.key == SDLK_DOWN:
                    self.ud_dir += 1
                    if self.right:
                        self.i = 5
                    elif self.left:
                        self.i = 1
                    else:
                        self.i = 11
                    self.down = False

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.lr_dir * 1
        self.y += self.ud_dir * 1

    def draw(self):
        self.image.clip_draw(self.frame * 32, 32 * self.i, 32, 32, self.x, self.y)
