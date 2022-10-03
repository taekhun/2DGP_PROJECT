from pico2d import *
open_canvas()
character = load_image('turtle_1.png')


frame = 0
for x in range(0, 800, 5):
    clear_canvas()
    character.clip_draw(frame * 50, 0, 50, 148, x, 74)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)
    get_events()


close_canvas()

