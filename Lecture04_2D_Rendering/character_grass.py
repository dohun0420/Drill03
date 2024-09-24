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
    for x in range(0, 750, 10):
        draw_boy(x, 550)

def run_right():
    for y in range(0, 550, 10):
        draw_boy(750, 550 -y)

def run_bottom():
    for x in range(0, 750, 10):
        draw_boy(750 - x, 0)
        
def run_left():
    for y in range(0, 550, 10):
        draw_boy(0, y)

def run_tri_bot():
    for x in range (0, 750, 10):
        draw_boy(x, 0)
        
def run_tri_right():
    for a in range(0, 600, 10):
        x = 800 - 2/3 * a
        y = a
        draw_boy(x, y)
            
def run_tri_left():
    for b in range(0, 600, 10):
        x = 400 - 2/3 * b
        y = 600 - b
        draw_boy(x, y)

def run_rectangle():
    run_top()
    run_right()
    run_bottom()
    run_left()

def run_circle():
    r, cx, cy = 300, 800 // 2, 600 // 2
    for d in range(0, 360):
        x = r * math.cos(math.radians(d)) + cx
        y = r * math.sin(math.radians(d)) + cy
        draw_boy(x, y)

def run_triangle():
    run_tri_bot()
    run_tri_right()
    run_tri_left()

while True:
    run_rectangle()
    run_circle()
    run_triangle()

    

close_canvas()
