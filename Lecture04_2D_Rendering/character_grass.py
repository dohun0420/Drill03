from pico2d import *

def run_rectangle():
    print('RECTANGLE')
    pass

def run_circle():
    print('CIRCLE')
    pass

open_canvas()

grass = load.image('grass.png')
boy = load.image('character.png')

while True:
    run_rectangle()
    run_circle()
    

close_canvas()
