import tkinter as tk
from grafik.ball import Ball


def add_ball(event=None):
    Ball.add(my_canvas)


def remove_ball(event=None):
    Ball.remove()


def refresh():
    [ball.draw() for ball in Ball.get_balls()]
    my_canvas.after(25, refresh)


window = tk.Tk()
window.bind("<Button-1>", add_ball)
window.bind("<Button-3>", remove_ball)

label = tk.Label(window, text="Gravity")
my_canvas = tk.Canvas(window, height=1500, width=1500, bg="#FFFFFF")

[Ball.add(my_canvas) for i in range(3)]
[my_canvas.after(25, refresh) for ball in Ball.get_balls()]

label.pack()
my_canvas.pack()

window.mainloop()
