from pico2d import *
import game_framework

from stage import Stage
from character import Character

stage = None
character = None


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            character.handle_event(event)  # 소년한테 이벤트를 처리하도록 넘겨준다


# 초기화
def enter():
    global character, stage
    character = Character()
    stage = Stage()

# 종료
def exit():
    global character, stage
    del character
    del stage

def update():
    character.update()

def draw_world():
    stage.draw()
    character.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass




def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
