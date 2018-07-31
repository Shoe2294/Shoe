#https://github.com/kidscancode/intro-python-code/blob/master/bouncing%20balls.py


from Tkinter import *
import time
import random

WIDTH = 1000
HEIGHT = 1000

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="black")
tk.title("Drawing")
canvas.pack()

colors = ['red', 'green', 'blue', 'orange', 'yellow', 'cyan', 'magenta',
          'dodgerblue', 'turquoise', 'grey', 'gold', 'pink']

class Ball:
    def __init__(self):
        self.size = random.randrange(30, 60)
        color = random.choice(colors)
        self.shape = canvas.create_oval(self.size*2, self.size*2, self.size, self.size, fill=color)
        self.speedx = random.randrange(0, 50)
        self.speedy = random.randrange(0, 50)

    def update(self):
        canvas.move(self.shape, self.speedx, self.speedy)
        pos = canvas.coords(self.shape)
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.speedx *= -1
        if pos[2] >= WIDTH and pos[0] <= 0 and self.shape == 'blue':
            ball_list.append(Ball())
            tk.update()
            time.sleep(0.01)
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.speedy *= -1

ball_list = []
for i in range(6):
    ball_list.append(Ball())
while True:
    for ball in ball_list:
        ball.update()
    tk.update()
    time.sleep(0.01)