import math
import random


class Ball:

    __balls = []

    def __init__(self, canvas, x, y, r, angle, color, tag):
        self.__canvas = canvas
        self.__x = x
        self.__y = y
        self.__r = r
        self.__tag = tag
        self.__x_direction = 1
        self.__y_direction = math.tan(math.radians(angle))
        self.__id = canvas.create_oval(
            x - r,
            y - r,
            x + r,
            y + r,
            fill=color,
            outline=color,
            tag=tag
        )

    def get_canvas(self):
        return self.__canvas

    def get_tag(self):
        return self.__tag

    def draw(self):
        if self.__x >= self.__canvas.winfo_width() - self.__r or self.__x < self.__r:
            self.__x_direction *= -1
        if self.__y >= self.__canvas.winfo_height() - self.__r or self.__y < self.__r:
            self.__y_direction *= -1
        self.__x += self.__x_direction
        self.__y += self.__y_direction
        self.__canvas.move(self.__id, self.__x_direction, self.__y_direction)

    @classmethod
    def remove(cls):
        if Ball.__balls:
            ball = Ball.__balls.pop()
            ball.get_canvas().delete(ball.get_tag())
            del ball
            print('Ball in pool', len(Ball.__balls))

    @classmethod
    def add(cls, my_canvas):
        size = random.randint(0, 75)
        angle = random.randint(0, 90)
        color = "#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        ball = Ball(
            my_canvas,
            size,
            size,
            size,
            angle,
            color,
            color
        )
        Ball.__balls.append(ball)
        print('Ball in pool', len(Ball.__balls))

    @staticmethod
    def get_balls():
        return Ball.__balls
