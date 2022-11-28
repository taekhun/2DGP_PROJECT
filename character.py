from pico2d import *

import game_framework
import game_world
from star import Star
import gameover_state

#1 : 이벤트 정의
RD, LD, UD, DD, RU, LU, UU, DU, SPACE = range(9)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYDOWN, SDLK_UP): UD,
    (SDL_KEYDOWN, SDLK_DOWN): DD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYUP, SDLK_UP): UU,
    (SDL_KEYUP, SDLK_DOWN): DU,
    (SDL_KEYUP, SDLK_z): SPACE
}

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 10.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0) / 60.0
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class WalkingState:

    def enter(character, event):
        if event == RD:
            character.x_velocity += RUN_SPEED_PPS
        elif event == RU:
            character.x_velocity -= RUN_SPEED_PPS
        if event == LD:
            character.x_velocity -= RUN_SPEED_PPS
        elif event == LU:
            character.x_velocity += RUN_SPEED_PPS

        if event == UD:
            character.y_velocity += RUN_SPEED_PPS
        elif event == UU:
            character.y_velocity -= RUN_SPEED_PPS
        if event == DD:
            character.y_velocity -= RUN_SPEED_PPS
        elif event == DU:
            character.y_velocity += RUN_SPEED_PPS

    def exit(character, event):
        if SPACE == event:
            character.fire_star()
        pass

    def do(character):
        character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        character.x += character.x_velocity * game_framework.frame_time
        character.y += character.y_velocity * game_framework.frame_time
        character.x = clamp(0 + 10, character.x, 800 - 10)
        character.y = clamp(0 + 15, character.y, 600 - 15)
        if 520 < character.y < 600:
            character.x = clamp(365 + 10, character.x, 440 - 10)
        if 0 < character.x < 365 - 2:
            character.y = clamp(0 + 45, character.y, 520 - 15)
        if 0 < character.y < 40:
            character.x = clamp(365 + 10, character.x, 440 - 10)
        if 440 < character.x < 800:
            character.y = clamp(0 + 45, character.y, 520 - 15)

    def draw(character):
        if character.hit_flag >= 1:
            if character.x_velocity > 0:
                character.image.clip_draw(int(character.frame) * 32, 32 * 5, 32, 32, character.x, character.y)
                character.RL_dir = 1
                character.UD_dir = 0
                if character.y_velocity > 0:
                    character.image.clip_draw(int(character.frame) * 32, 32 * 6, 32, 32, character.x, character.y)
                    character.UD_dir = 1
                elif character.y_velocity < 0:
                    character.image.clip_draw(int(character.frame) * 32, 32 * 4, 32, 32, character.x, character.y)
                    character.UD_dir = -1

            elif character.x_velocity < 0:
                character.image.clip_draw(int(character.frame) * 32, 32, 32, 32, character.x, character.y)
                character.RL_dir = -1
                character.UD_dir = 0
                if character.y_velocity > 0:
                    character.image.clip_draw(int(character.frame) * 32, 0, 32, 32, character.x, character.y)
                    character.UD_dir = 1
                elif character.y_velocity < 0:
                    character.image.clip_draw(int(character.frame) * 32, 32 * 2, 32, 32, character.x, character.y)
                    character.UD_dir = -1

            else:
                # if boy x_velocity == 0
                if character.y_velocity > 0:
                    character.image.clip_draw(int(character.frame) * 32, 32 * 7, 32, 32, character.x, character.y)
                    character.UD_dir = 1
                    character.RL_dir = 0

                elif character.y_velocity < 0:
                    character.image.clip_draw(int(character.frame) * 32, 32 * 3, 32, 32, character.x, character.y)
                    character.UD_dir = -1
                    character.RL_dir = 0

                else:
                    # boy is idle
                    if character.UD_dir == 1:
                        character.image.clip_draw(int(character.frame) * 32, 32 * 15, 32, 32, character.x, character.y)
                    elif character.UD_dir == -1:
                        character.image.clip_draw(int(character.frame) * 32, 32 * 11, 32, 32, character.x, character.y)
                    elif character.RL_dir == -1:
                        character.image.clip_draw(int(character.frame) * 32, 32 * 9, 32, 32, character.x, character.y)
                    elif character.RL_dir == 1:
                        character.image.clip_draw(int(character.frame) * 32, 32 * 13, 32, 32, character.x, character.y)
        else:
            if character.x_velocity > 0:
                character.hit_image.clip_draw(int(character.frame) * 32, 32 * 5, 32, 32, character.x, character.y)
                character.RL_dir = 1
                character.UD_dir = 0
                if character.y_velocity > 0:
                    character.hit_image.clip_draw(int(character.frame) * 32, 32 * 6, 32, 32, character.x, character.y)
                    character.UD_dir = 1
                elif character.y_velocity < 0:
                    character.hit_image.clip_draw(int(character.frame) * 32, 32 * 4, 32, 32, character.x, character.y)
                    character.UD_dir = -1

            elif character.x_velocity < 0:
                character.hit_image.clip_draw(int(character.frame) * 32, 32, 32, 32, character.x, character.y)
                character.RL_dir = -1
                character.UD_dir = 0
                if character.y_velocity > 0:
                    character.hit_image.clip_draw(int(character.frame) * 32, 0, 32, 32, character.x, character.y)
                    character.UD_dir = 1
                elif character.y_velocity < 0:
                    character.hit_image.clip_draw(int(character.frame) * 32, 32 * 2, 32, 32, character.x, character.y)
                    character.UD_dir = -1

            else:
                # if boy x_velocity == 0
                if character.y_velocity > 0:
                    character.hit_image.clip_draw(int(character.frame) * 32, 32 * 7, 32, 32, character.x, character.y)
                    character.UD_dir = 1
                    character.RL_dir = 0

                elif character.y_velocity < 0:
                    character.hit_image.clip_draw(int(character.frame) * 32, 32 * 3, 32, 32, character.x, character.y)
                    character.UD_dir = -1
                    character.RL_dir = 0

                else:
                    # boy is idle
                    if character.UD_dir == 1:
                        character.hit_image.clip_draw(int(character.frame) * 32, 32 * 15, 32, 32, character.x, character.y)
                    elif character.UD_dir == -1:
                        character.hit_image.clip_draw(int(character.frame) * 32, 32 * 11, 32, 32, character.x, character.y)
                    elif character.RL_dir == -1:
                        character.hit_image.clip_draw(int(character.frame) * 32, 32 * 9, 32, 32, character.x, character.y)
                    elif character.RL_dir == 1:
                        character.hit_image.clip_draw(int(character.frame) * 32, 32 * 13, 32, 32, character.x, character.y)

#3. 상태 변환 구현
next_state_table = {
    WalkingState:  {RU: WalkingState,  LU: WalkingState,  RD: WalkingState,  LD: WalkingState,
                    UU: WalkingState, DU: WalkingState, UD: WalkingState, DD: WalkingState,
                    SPACE: WalkingState},
}

class Character:
    def __init__(self):
        self.x, self.y = 800 // 2, 600 // 2
        self.frame = 0
        self.RL_dir, self.UD_dir = 1, 0
        self.x_velocity, self.y_velocity = 0, 0
        self.image = load_image('./png/character.png')
        self.hit_image = load_image('./png/hit_character.png')
        self.event_que = []
        self.cur_state = WalkingState
        self.cur_state.enter(self, None)
        self.font = load_font('ENCR10B.TTF', 16)
        self.HP = 100
        self.hit_flag = 1


    def update(self):
        self.cur_state.do(self)

        self.hit_flag += game_framework.frame_time
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
        if self.HP <= 0:
            game_framework.push_state(gameover_state)


    def draw(self):
        self.cur_state.draw(self)
        # draw_rectangle(*self.get_bb())
        self.font.draw(self.x - 50, self.y + 30, f'(HP: {self.HP:.1f})', (255, 0, 0))


    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def fire_star(self):
        print('FIRE STAR')
        # 발사 시점에서 볼을 생성해줘야 된다.
        star = Star(self.x, self.y, (self.RL_dir ** 2 + self.UD_dir ** 2) ** 1/2)
        star.get_direction(self.RL_dir, self.UD_dir)
        game_world.add_object(star, 1)
        game_world.add_collision_group(star, None, 'star:enemies')

    def get_bb(self):
        return self.x - 13, self.y - 16, self.x + 10, self.y + 13

    def handle_collision(self, other, group):
        if group == 'character:enemies':
            #self.HP -= 0.01
            if self.hit_flag >= 1:
                self.hit_flag = 0
