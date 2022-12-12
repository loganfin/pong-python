from turtle import Turtle

class Paddle:   #[Logan] & [Jenna]
    def __init__(self, xPos, windowHeight):   #[Logan] & [Jenna]
        self.__distance = 15
        self.__paddle = Turtle(visible = False)

        self.__paddle.speed(0)
        self.__paddle.penup()
        self.__paddle.setx(xPos)
        self.__paddle.shape("square")
        self.__paddle.setheading(90)
        self.__paddle.shapesize(1, 6)
        self.__paddle.color("grey")

        self.__halfHeight = abs(self.__paddle.get_shapepoly()[0][1]) + 2

        #self.__top = 62
        #self.__bottom = 62 # need to find a generic way to determine these values

    def show(self): #[Logan]
        self.__paddle.showturtle()

    def moveUp(self, topBorder):    #[Logan]
        if self.__paddle.ycor() + self.__halfHeight == topBorder:
            pass

        elif self.__paddle.ycor() + self.__halfHeight + self.__distance >= topBorder:
            self.__paddle.forward(topBorder - self.__paddle.ycor() - self.__halfHeight)

        elif self.__paddle.ycor() + self.__halfHeight <= topBorder:
            self.__paddle.forward(self.__distance)
            return True

    def moveDown(self, bottomBorder):   #[Logan]
        if self.__paddle.ycor() - self.__halfHeight == bottomBorder:
            pass
        elif self.__paddle.ycor() - self.__halfHeight - self.__distance <= bottomBorder:
            self.__paddle.backward(self.__paddle.ycor() - self.__halfHeight - bottomBorder)
        elif self.__paddle.ycor() - self.__halfHeight >= bottomBorder:
            self.__paddle.backward(self.__distance)
            return True
