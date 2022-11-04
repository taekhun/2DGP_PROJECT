# from pico2d import *
#
#
# class Character:
#     def __init__(self):
#         self.running = True
#         self.i = 13
#         self.right = False
#         self.up = False
#         self.down = False
#         self.left = False
#         self.frame = 0
#         self.lr_dir = 0  # 좌우
#         self.ud_dir = 0  # 상하
#         self.x, self.y = 400, 32
#         self.image = load_image('character.png')
#
#         self.attack_image = load_image('attack.png')
#         self.attacks_right = []
#         self.attacks_left = []
#         self.attacks_up = []
#         self.attacks_down = []
#         self.attacks_up_right = []
#         self.attacks_up_left = []
#         self.attacks_down_left = []
#         self.attacks_down_right = []
#
#         self.attack_x = 0
#         self.attack_y = 0
#         self.attack_speed = 10
#         self.attack_right = False
#         self.attack_left = False
#         self.attack_up = False
#         self.attack_down = False
#         self.attack_up_right = False
#         self.attack_up_left = False
#         self.attack_down_left = False
#         self.attack_down_right = False
#
#     def handle_event(self, event):
#         # events = get_events()
#         # for event in events:
#             if event.type == SDL_QUIT:
#                 self.running = False
#             elif event.type == SDL_KEYDOWN:
#                 if event.key == SDLK_SPACE:
#                     self.attack_x = self.x
#                     self.attack_y = self.y
#                     if self.i == 5 or self.i == 13:
#                         self.attacks_right.append([self.attack_x, self.attack_y])
#                     elif self.i == 1 or self.i == 9:
#                         self.attacks_left.append([self.attack_x, self.attack_y])
#                     elif self.i == 7 or self.i == 15:
#                         self.attacks_up.append([self.attack_x, self.attack_y])
#                     elif self.i == 3 or self.i == 11:
#                         self.attacks_down.append([self.attack_x, self.attack_y])
#                     elif self.i == 6:
#                         self.attacks_up_right.append([self.attack_x, self.attack_y])
#                     elif self.i == 0:
#                         self.attacks_up_left.append([self.attack_x, self.attack_y])
#                     elif self.i == 2:
#                         self.attacks_down_left.append([self.attack_x, self.attack_y])
#                     elif self.i == 4:
#                         self.attacks_down_right.append([self.attack_x, self.attack_y])
#
#                 if event.key == SDLK_RIGHT:
#                     self.lr_dir += 1
#                     if not self.up and not self.down:
#                         self.i = 5
#                     if self.up:
#                         self.i = 6
#                         self.attack_up_right = True
#                     if self.down:
#                         self.i = 4
#                         self.attack_down_right = True
#                     self.right = True
#                     self.attack_right = True
#
#                 elif event.key == SDLK_LEFT:
#                     self.lr_dir -= 1
#                     if not self.up and not self.down:
#                         self.i = 1
#                     if self.up:
#                         self.i = 0
#                         self.attack_up_left = True
#                     if self.down:
#                         self.i = 2
#                         self.attack_down_left = True
#                     self.left = True
#                     self.attack_left = True
#
#                 elif event.key == SDLK_UP:
#                     self.ud_dir += 1
#                     if not self.right and not self.left:
#                         self.i = 7
#                     if self.right:
#                         self.i = 6
#                         self.attack_up_right = True
#                     if self.left:
#                         self.i = 0
#                         self.attack_up_left = True
#                     self.up = True
#                     self.attack_up = True
#
#                 elif event.key == SDLK_DOWN:
#                     self.ud_dir -= 1
#                     if not self.right and not self.left:
#                         self.i = 3
#                     elif self.right:
#                         self.i = 4
#                         self.attack_down_right = True
#                     elif self.left:
#                         self.i = 2
#                         self.attack_down_left = True
#                     self.down = True
#                     self.attack_down = True
#
#                 elif event.key == SDLK_ESCAPE:
#                     self.running = False
#
#             elif event.type == SDL_KEYUP:
#                 if event.key == SDLK_RIGHT:
#                     self.lr_dir -= 1
#                     if self.up:
#                         self.i = 7
#                     elif self.down:
#                         self.i = 3
#                     else:
#                         self.i = 13
#                     self.right = False
#                 elif event.key == SDLK_LEFT:
#                     self.lr_dir += 1
#                     if self.up:
#                         self.i = 7
#                     elif self.down:
#                         self.i = 3
#                     else:
#                         self.i = 9
#                     self.left = False
#                 elif event.key == SDLK_UP:
#                     self.ud_dir -= 1
#                     if self.right:
#                         self.i = 5
#                     elif self.left:
#                         self.i = 1
#                     else:
#                         self.i = 15
#                     self.up = False
#                 elif event.key == SDLK_DOWN:
#                     self.ud_dir += 1
#                     if self.right:
#                         self.i = 5
#                     elif self.left:
#                         self.i = 1
#                     else:
#                         self.i = 11
#                     self.down = False
#
#     def update(self):
#         self.frame = (self.frame + 1) % 8
#         self.x += self.lr_dir * 2
#         self.y += self.ud_dir * 2
#         if self.attack_right:
#             self.attacks_right = [[a[0] + self.attack_speed, a[1]] for a in self.attacks_right]
#         if self.attack_left:
#             self.attacks_left = [[a[0] - self.attack_speed, a[1]] for a in self.attacks_left]
#         if self.attack_up:
#             self.attacks_up = [[a[0], a[1] + self.attack_speed] for a in self.attacks_up]
#         if self.attack_down:
#             self.attacks_down = [[a[0], a[1] - self.attack_speed] for a in self.attacks_down]
#         if self.attack_up_right:
#             self.attacks_up_right = [[a[0] + 2 ** (1/2) / 2 * self.attack_speed,
#                                       a[1] + 2 ** (1/2) / 2 * self.attack_speed] for a in self.attacks_up_right]
#         if self.attack_up_left:
#             self.attacks_up_left = [[a[0] - 2 ** (1/2) / 2 * self.attack_speed,
#                                       a[1] + 2 ** (1/2) / 2 * self.attack_speed] for a in self.attacks_up_left]
#         if self.attack_down_left:
#             self.attacks_down_left = [[a[0] - 2 ** (1/2) / 2 * self.attack_speed,
#                                       a[1] - 2 ** (1/2) / 2 * self.attack_speed] for a in self.attacks_down_left]
#         if self.attack_down_right:
#             self.attacks_down_right = [[a[0] + 2 ** (1/2) / 2 * self.attack_speed,
#                                       a[1] - 2 ** (1/2) / 2 * self.attack_speed] for a in self.attacks_down_right]
#
#     def draw(self):
#         delay(0.02)
#         self.image.clip_draw(self.frame * 32, 32 * self.i, 32, 32, self.x, self.y)
#         for self.attack_x, self.attack_y in self.attacks_right:
#             self.attack_image.draw(self.attack_x, self.attack_y)
#         for self.attack_x, self.attack_y in self.attacks_left:
#             self.attack_image.draw(self.attack_x, self.attack_y)
#         for self.attack_x, self.attack_y in self.attacks_up:
#             self.attack_image.draw(self.attack_x, self.attack_y)
#         for self.attack_x, self.attack_y in self.attacks_down:
#             self.attack_image.draw(self.attack_x, self.attack_y)
#         for self.attack_x, self.attack_y in self.attacks_up_right:
#             self.attack_image.draw(self.attack_x, self.attack_y)
#         for self.attack_x, self.attack_y in self.attacks_up_left:
#             self.attack_image.draw(self.attack_x, self.attack_y)
#         for self.attack_x, self.attack_y in self.attacks_down_left:
#             self.attack_image.draw(self.attack_x, self.attack_y)
#         for self.attack_x, self.attack_y in self.attacks_down_right:
#             self.attack_image.draw(self.attack_x, self.attack_y)
