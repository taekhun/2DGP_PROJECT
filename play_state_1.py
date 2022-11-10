from pico2d import *
import time

import game_framework
import game_world
import menu_state

from stage import Stage
from character_1 import Character
from enemy import Enemy

character_1 = None
stage = None
enemies = []
i_flag = 0

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.push_state(menu_state)
        else:
            character_1.handle_event(event)


# 초기화
def enter():
    global character_1, stage
    character_1 = Character()
    stage = Stage()
    game_world.add_object(stage, 0)
    game_world.add_object(character_1, 1)
    global enemies
    game_world.add_objects(enemies, 1)

def add_enemy():
    enemy = Enemy()
    game_world.add_object(enemy, 1)
# 종료
def exit():
    game_world.clear()

def update():
    global i_flag
    for game_object in game_world.all_objects():
        game_object.update()
    i_flag += 1
    if i_flag == 100:
        add_enemy()
        i_flag = 0



def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()


def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def pause():
    pass


def resume():
    pass


def test_self():
    import play_state_1

    pico2d.open_canvas()
    game_framework.run(play_state_1)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
