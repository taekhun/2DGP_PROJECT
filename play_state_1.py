from pico2d import *
import time

import game_framework
import game_world
import menu_state

from stage import Stage
from stage_2 import Stage_2
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
    global character_1, stage, stage_2
    character_1 = Character()
    stage = Stage()
    stage_2 = Stage_2()
    game_world.add_object(stage, 0)
    game_world.add_object(character_1, 1)
    game_world.add_object(stage_2, 2)


def add_enemy():
    global enemy
    enemy = Enemy()
    # enemies.append(Enemy())
    game_world.add_object(enemy, 1)
    game_world.add_collision_group(character_1, enemy, 'character:enemies')
    game_world.add_collision_group(character_1.fire_star(), enemy, 'star:enemies')


# 종료
def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()

    for a, b, group in game_world.all_collision_pairs():
        if colide(a, b):
            print('COLLISION by ', group)
            a.handle_collision(b, group)
            b.handle_collision(a, group)

    global i_flag
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

def colide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def test_self():
    import play_state_1

    pico2d.open_canvas()
    game_framework.run(play_state_1)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
