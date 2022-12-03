from pico2d import *
import game_framework
import play_state
import game_world

image = None
bgm = None

def enter():
    global image
    global bgm
    image = load_image('./png/title.png')
    bgm = load_music('./sound/title.mp3')
    bgm.set_volume(32)
    bgm.repeat_play()


def exit():
    global image
    del image


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_world.clear()
            game_framework.change_state(play_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
    pass


def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass
