from pico2d import *
open_canvas()
character = load_image('grave.png')


frame = 0
for x in range(0, 800, 5):
    clear_canvas()
    character.clip_draw(0, 0, 32, 32, 400, 50)
    update_canvas()
    frame = (frame + 1) % 1
    delay(0.05)
    get_events()

close_canvas()

