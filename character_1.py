from pico2d import *
import game_world
from star import Star

#1 : 이벤트 정의
RD, LD, UD, DD, RU, LU, UU, DU, SPACE = range(9)
event_name = ['RD', 'LD', 'RU', 'LU', 'RU', 'LU', 'UU', 'DU', 'SPACE']

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYDOWN, SDLK_UP): UD,
    (SDL_KEYDOWN, SDLK_DOWN): DD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYUP, SDLK_UP): UU,
    (SDL_KEYUP, SDLK_DOWN): DU,
    (SDL_KEYUP, SDLK_SPACE): SPACE
}


#2 : 상태의 정의
class IDLE:
    @staticmethod
    def enter(self, event):
        print('ENTER IDLE')
        self.RL_dir = 0
        self.UD_dir = 0

    @staticmethod
    def exit(self, event):
        print('EXIT IDLE')
        if SPACE == event:
            self.fire_star()

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8

    @staticmethod
    def draw(self):
        if self.RL_face_dir == 1:
            self.image.clip_draw(self.frame * 32, 32 * 13, 32, 32, self.x, self.y)
        elif self.RL_face_dir == -1:
            self.image.clip_draw(self.frame * 32, 32 * 9, 32, 32, self.x, self.y)
        elif self.UD_face_dir == 1:
            self.image.clip_draw(self.frame * 32, 32 * 15, 32, 32, self.x, self.y)
        elif self.UD_face_dir == -1:
            self.image.clip_draw(self.frame * 32, 32 * 11, 32, 32, self.x, self.y)


class RUN:
    def enter(self, event):
        print('ENTER RUN')
        if event == RD:
            self.RL_dir += 1
        elif event == LD:
            self.RL_dir -= 1
        elif event == UD:
            self.UD_dir += 1
        elif event == DD:
            self.UD_dir -= 1
        elif event == RU:
            if self.L_BOOL == True:
                self.RL_dir -= 1
            elif self.U_BOOL == True:
                self.UD_dir += 1
            elif self.D_BOOL == True:
                self.UD_dir -= 1
        elif event == LU:
            if self.R_BOOL == True:
                self.RL_dir += 1
            elif self.U_BOOL == True:
                self.UD_dir += 1
            elif self.D_BOOL == True:
                self.UD_dir -= 1
        elif event == UU:
            if self.D_BOOL == True:
                self.UD_dir -= 1
            elif self.R_BOOL == True:
                self.RL_dir += 1
            elif self.L_BOOL == True:
                self.RL_dir -= 1
        elif event == DU:
            if self.U_BOOL == True:
                self.UD_dir += 1
            elif self.R_BOOL == True:
                self.RL_dir += 1
            elif self.L_BOOL == True:
                self.RL_dir -= 1

    def exit(self, event):
        print('EXIT RUN')
        self.RL_face_dir = self.RL_dir
        self.UD_face_dir = self.UD_dir
        if SPACE == event:
            self.fire_star()

    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.RL_dir
        self.y += self.UD_dir
        self.x = clamp(0, self.x, 800)
        self.y = clamp(0, self.y, 600)

    def draw(self):
        if self.RL_dir == -1:
            self.image.clip_draw(self.frame*32, 32 * 1, 32, 32, self.x, self.y)
        elif self.RL_dir == 1:
            self.image.clip_draw(self.frame*32, 32 * 4, 32, 32, self.x, self.y)
        elif self.UD_dir == -1:
            self.image.clip_draw(self.frame * 32, 32 * 3, 32, 32, self.x, self.y)
        elif self.UD_dir == 1:
            self.image.clip_draw(self.frame * 32, 32 * 7, 32, 32, self.x, self.y)


#3. 상태 변환 구현
next_state = {
    IDLE:  {RU: RUN,  LU: RUN,  RD: RUN,  LD: RUN, UU: RUN, DU: RUN, UD: RUN, DD: RUN, SPACE: IDLE},
    RUN:   {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, UU: IDLE, DU: IDLE, UD: IDLE, DD: IDLE, SPACE: RUN}
}


class Character:
    def __init__(self):
        self.x, self.y = 800 // 2, 90
        self.frame = 0
        self.RL_dir, self.UD_dir, self.RL_face_dir, self.UD_face_dir = 0, 0, 1, 1
        self.U_BOOL, self.D_BOOL, self.R_BOOL, self.L_BOOL, = False, False, False, False
        self.image = load_image('character.png')

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print('ERROR:', self.cur_state.__name__, '  ', event_name[event])
            self.cur_state.enter(self, event)

            if event == RD:
                self.R_BOOL = True
                self.L_BOOL = False
            elif event == LD:
                self.L_BOOL = True
                self.R_BOOL = False
            elif event == UD:
                self.U_BOOL = True
                self.D_BOOL = False
            elif event == DD:
                self.D_BOOL = True
                self.U_BOOL = False
            elif event == RU:
                self.L_BOOL = True
                self.R_BOOL = False
            elif event == LU:
                self.R_BOOL = True
                self.L_BOOL = False
            elif event == UU:
                self.D_BOOL = True
                self.U_BOOL = False
            elif event == DU:
                self.U_BOOL = True
                self.D_BOOL = False

    def draw(self):
        self.cur_state.draw(self)
        debug_print('PPPP')
        debug_print(f'RL_Face Dir: {self.RL_face_dir}, UD_Face Dir: {self.UD_face_dir},'
                    f'RL_Dir: {self.RL_dir}, UD_Dir: {self.UD_dir}')

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def fire_star(self):
        print('FIRE STAR')
        # 발사 시점에서 볼을 생성해줘야 된다.
        star = Star(self.x, self.y, (self.RL_face_dir * 2 + self.UD_face_dir * 2) / 2)
        star.get_direction(self.RL_face_dir, self.UD_face_dir)
        game_world.add_object(star, 1)
