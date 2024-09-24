from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

def draw_boy(x, y):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.01)
    
def run_top():
    for x in range(0, 800, 10):
        draw_boy(x, 550)

def run_right():
    pass
def run_bottom():
    pass
def run_left():
    pass

def run_rectangle():
    print('RECTANGLE')
    run_top()
    run_right()
    run_bottom()
    run_left()
    pass

def run_circle():
    print('CIRCLE')

    r, cx, cy = 300, 800 // 2, 600 // 2
    for d in range(0, 360):
        x = r * math.cos(math.radians(d)) + cx
        y = r * math.sin(math.radians(d)) + cy
        draw_boy(x, y)

while True:
    run_rectangle()
    run_circle()
    break
    

close_canvas()
