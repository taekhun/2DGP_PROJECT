from pico2d import *
open_canvas()
character = load_image('special_attack.png')


frame = 0
for x in range(0, 800, 5):
    clear_canvas()
    character.clip_draw(frame * 16, 0, 16, 15, 30, 31)
    update_canvas()
    frame = (frame + 1) % 1
    delay(0.05)
    get_events()

close_canvas()

