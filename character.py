from pico2d import *
open_canvas()
idle_character = load_image('idle_character.png')
move_character = load_image('run_character.png')


def handle_events():
    global running
    global x
    global dir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1


running = True
x = 800 // 2
frame = 0
dir = 0


while running:
    clear_canvas()
    move_character.clip_draw(frame * 32, 160, 32, 32, x, 32)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x += dir * 5
    delay(0.01)

close_canvas()

