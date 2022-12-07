import turtle

class Paddle:
    #self.__player1Pos = (-10, 0)
    #self.__player2Pos = (10, 0)

    def __init__(self, player):
        '''
        if player == 1:
            self.__xPos, self.__yPos = self.__player1Pos
        else:
            self.__xPos, self.__yPos = self.__player2Pos
        '''

        self.__paddle = turtle.Turtle()

        self.__paddle.hideturtle()
        self.__paddle.shape("square")
        self.__paddle.setheading(90)
        self.__paddle.shapesize(1, 6)
        self.__paddle.color("grey")
        self.__paddle.speed(0)
        self.__paddle.penup()
        self.__paddle.showturtle()

        self.__distance = 20

    def moveUp(self):
        self.__paddle.forward(self.__distance)

    def moveDown(self):
        self.__paddle.backward(self.__distance)
