from pico2d import *
import time

import game_framework
import game_world
import menu_state

from stage import Stage
from stage_2 import Stage_2
from character import Character
from enemy import Enemy
from turtle_attack import EnemyAttack
from item import Item

import server

character = None
i_flag = 0
i_flag_2 = 0
i_flag_3 = 0
bgm = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.push_state(menu_state)
        else:
            server.character.handle_event(event)


# 초기화
def enter():
    global stage, stage_2, bgm
    server.character = Character()
    stage = Stage()
    stage_2 = Stage_2()
    game_world.add_object(stage, 0)
    game_world.add_object(server.character, 1)
    game_world.add_object(stage_2, 2)
    bgm = load_music('./sound/play.mp3')
    bgm.set_volume(32)
    bgm.repeat_play()

def add_enemy():
    server.enemy = Enemy()
    game_world.add_object(server.enemy, 1)
    game_world.add_collision_group(server.character, server.enemy, 'character:enemies')
    game_world.add_collision_group(None, server.enemy, 'star:enemies')

def add_enemy_attack():
    server.turtle_attack = EnemyAttack()
    game_world.add_object(server.turtle_attack, 1)
    game_world.add_collision_group(server.character, server.turtle_attack, 'character:enemies_attack')

def add_item():
    global item
    item = Item()
    game_world.add_object(item, 1)
    game_world.add_collision_group(server.character, item, 'character:item')

# 종료
def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()

    for a, b, group in game_world.all_collision_pairs():
        if colide(a, b):
            # print('COLLISION by ', group)
            a.handle_collision(b, group)
            b.handle_collision(a, group)

    global i_flag
    global i_flag_2
    global i_flag_3

    i_flag += 1
    if i_flag == 100:
        add_enemy()
        i_flag = 0

    i_flag_2 += 1
    if i_flag_2 == 1000:
        add_enemy_attack()
        i_flag_2 = 0

    i_flag_3 += 1
    if i_flag_3 == 5000:
        add_item()
        i_flag_3 = 0

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
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
