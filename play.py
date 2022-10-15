from pico2d import *
import character
open_canvas()
ch = character.Character()

while ch.running:
    ch.handle_events()
    ch.update()
    clear_canvas()
    ch.draw()
    update_canvas()
    delay(0.02)

close_canvas()

