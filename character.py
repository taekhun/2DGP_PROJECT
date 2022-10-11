from pico2d import *
open_canvas()
character = load_image('character.png')

i = 13
right = False
up = False
down = False

def handle_events():
    global running
    global x
    global lr_dir
    global ud_dir
    global i
    global right
    global up
    global down
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                lr_dir += 1
                if not up and not down:
                    i = 5
                if up:
                    i = 6
                if down:
                    i = 4
                right = True
            elif event.key == SDLK_LEFT:
                lr_dir -= 1
                i = 1
            elif event.key == SDLK_UP:
                ud_dir += 1
                if not right:
                    i = 7
                elif right:
                    i = 6
                up = True
            elif event.key == SDLK_DOWN:
                ud_dir -= 1
                if not right:
                    i = 3
                elif right:
                    i = 4
                down = True
            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                lr_dir -= 1
                if up:
                    i = 7
                elif down:
                    i = 3
                else:
                    i = 13
                right = False
            elif event.key == SDLK_LEFT:
                lr_dir += 1
                i = 9
            elif event.key == SDLK_UP:
                ud_dir -= 1
                if right:
                    i = 5
                else:
                    i = 15
                up = False
            elif event.key == SDLK_DOWN:
                ud_dir += 1
                if right:
                    i = 5
                else:
                    i = 11
                down = False


running = True
x = 800 // 2
y = 32
frame = 0
lr_dir = 0  # 좌우
ud_dir = 0  # 상하

while running:
    clear_canvas()
    character.clip_draw(frame * 32, 32 * i, 32, 32, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x += lr_dir * 1
    y += ud_dir * 1
    delay(0.01)

close_canvas()

