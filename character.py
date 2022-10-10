from pico2d import *
open_canvas()
idle_character = load_image('idle_character.png')
move_character = load_image('run_character.png')
i = 0

def handle_events():
    global running
    global x
    global lr_dir
    global ud_dir
    global i
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                lr_dir += 1
                i = 5
            elif event.key == SDLK_LEFT:
                lr_dir -= 1
                i = 2
            elif event.key == SDLK_UP:
                ud_dir += 1
                i = 7
            elif event.key == SDLK_DOWN:
                ud_dir -= 1
                i = 3
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                lr_dir -= 1
            elif event.key == SDLK_LEFT:
                lr_dir += 1
            elif event.key == SDLK_UP:
                ud_dir -= 1
            elif event.key == SDLK_DOWN:
                ud_dir += 1

running = True
x = 800 // 2
y = 32
frame = 0
lr_dir = 0  # 좌우
ud_dir = 0  # 상하

while running:
    clear_canvas()
    move_character.clip_draw(frame * 32, 32 * i, 32, 32, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x += lr_dir * 5
    y += ud_dir * 5
    delay(0.01)

close_canvas()
