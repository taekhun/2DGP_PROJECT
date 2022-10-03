from pico2d import *
open_canvas()
character = load_image('turtle_attack.png')


frame = 0
for x in range(0, 800, 5):
    clear_canvas()
    character.clip_draw(frame * 100, 0, 100, 100, x, 60)
    update_canvas()
    frame = (frame + 1) % 3
    delay(0.05)
    get_events()


close_canvas()

