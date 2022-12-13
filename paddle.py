from turtle import Turtle

class Paddle(Turtle):   #[Logan] & [Jenna]
    def __init__(self, xPos, windowHeight):   #[Logan] & [Jenna]
        self.__distance = 15
        super().__init__(visible = False)
        #self.__paddle = Turtle(visible = False)

        self.speed(0)
        self.penup()
        self.setx(xPos)
        self.shape("square")
        self.setheading(90)
        self.shapesize(1, 6)
        self.color("grey")

        self.__halfHeight = abs(self.get_shapepoly()[0][1]) + 2

        #self.__top = 62
        #self.__bottom = 62 # need to find a generic way to determine these values

    def show(self): #[Logan]
        self.showturtle()

    def moveUp(self, topBorder):    #[Logan]
        if self.ycor() + self.__halfHeight == topBorder:
            return False

        elif self.ycor() + self.__halfHeight + self.__distance >= topBorder:
            self.forward(topBorder - self.ycor() - self.__halfHeight)
            return True

        elif self.ycor() + self.__halfHeight <= topBorder:
            self.forward(self.__distance)
            return True

    def moveDown(self, bottomBorder):   #[Logan]
        if self.ycor() - self.__halfHeight == bottomBorder:
            return False

        elif self.ycor() - self.__halfHeight - self.__distance <= bottomBorder:
            self.backward(self.ycor() - self.__halfHeight - bottomBorder)
            return True

        elif self.ycor() - self.__halfHeight >= bottomBorder:
            self.backward(self.__distance)
            return True
