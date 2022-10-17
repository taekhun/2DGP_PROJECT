from pico2d import *
import character
open_canvas()
stage_1 = load_image('stage1.png')
ch = character.Character()

while ch.running:
    ch.handle_events()
    ch.update()
    clear_canvas()
    stage_1.draw(400, 300)
    ch.draw()
    update_canvas()
    delay(0.02)

close_canvas()
