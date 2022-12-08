import turtle

class Paddle:
    def __init__(self, xPos):
        self.__distance = 20
        self.__paddle = turtle.Turtle(visible = False)

        self.__paddle.speed(0)
        self.__paddle.penup()
        self.__paddle.setx(xPos)
        self.__paddle.shape("square")
        self.__paddle.setheading(90)
        self.__paddle.shapesize(1, 6)
        self.__paddle.color("grey")
        self.__bottom = 63 # need to find a generic way to determine these values
        self.__top = 63

    def show(self):
        self.__paddle.showturtle()

    def moveUp(self, topBorder):
        if self.__paddle.ycor() + self.__top == topBorder:
            pass
        elif self.__paddle.ycor() + self.__top + self.__distance >= topBorder:
            self.__paddle.forward(topBorder - self.__paddle.ycor() - self.__top)
        elif self.__paddle.ycor() + self.__top <= topBorder:
            self.__paddle.forward(self.__distance)


    def moveDown(self, bottomBorder):
        if self.__paddle.ycor() - self.__bottom == bottomBorder:
            pass
        elif self.__paddle.ycor() - self.__bottom - self.__distance <= bottomBorder:
            self.__paddle.backward(self.__paddle.ycor() - self.__bottom - bottomBorder)
        elif self.__paddle.ycor() - self.__bottom  >= bottomBorder:
            self.__paddle.backward(self.__distance)
