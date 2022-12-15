from turtle import Turtle

class Paddle(Turtle):   #[Logan] & [Jenna]
    def __init__(self, xPos, windowHeight):   #[Logan] & [Jenna]
        super().__init__(visible = False)

        self.__distance = 25
        self.__xPosition = xPos

        self.topCollision = self.ycor() + abs(self.get_shapepoly()[0][1])
        self.bottomCollision = self.ycor() - abs(self.get_shapepoly()[0][1])

        if self.xcor() < 0:
            self.sideCollision = self.xcor() + 10
        else:
            self.sideCollision = self.xcor() - 10

        self.speed(0)
        self.penup()
        self.setx(self.__xPosition)
        self.shape("square")
        self.setheading(90)
        self.shapesize(1, 6)
        self.color("grey")

        self.halfHeight = abs(self.get_shapepoly()[0][1]) + 2

    def show(self): #[Logan]
        self.showturtle()

    def moveUp(self, topBorder):    #[Logan]
        if self.ycor() + self.halfHeight == topBorder:
            return False

        if self.ycor() + self.halfHeight + self.__distance >= topBorder:
            self.forward(topBorder - self.ycor() - self.halfHeight)
            return True

        self.forward(self.__distance)
        return True

    def moveDown(self, bottomBorder):   #[Logan]
        if self.ycor() - self.halfHeight == bottomBorder:
            return False

        if self.ycor() - self.halfHeight - self.__distance <= bottomBorder:
            self.backward(self.ycor() - self.halfHeight - bottomBorder)
            return True

        self.backward(self.__distance)
        return True

    def reset(self):
        self.goto(self.__xPosition, 0)
