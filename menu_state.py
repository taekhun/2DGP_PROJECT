from pico2d import *
import game_framework
import game_world
import play_state_1
import title_state

image = None

def enter():
    global image
    image = load_image('menu.png')


def exit():
    global image
    del image


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.pop_state()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
    pass


def draw():
    clear_canvas()
    play_state_1.draw_world()
    image.draw(400, 300)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass
