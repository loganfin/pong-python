import turtle

from gameWindow import GameWindow

class Square:
    def __init__(self):
        self.__square = turtle.Turtle()

        self.__square.hideturtle()
        self.__square.shape("square")
        self.__square.setheading(90)
        self.__square.shapesize(1, 6)
        self.__square.color("grey")
        self.__square.speed("slowest")
        self.__square.penup()
        self.__square.showturtle()

        self.__distance = 0

    def move(self):
        #while self.__square.xcor() < self.__screenXBound and self.__square.ycor() < self.__screenYBound:
        for i in range(10):
            self.__square.up(self.__distance)
