'''
Logan created KeyEvent class.
'''
import turtle

from paddle import Paddle
from square import Square
from keyevent import KeyEvent

class GameWindow:
    def __init__(self):
        self.__width = 700
        self.__height = 500
        self.__window = turtle.Screen()
        self.__window.setup(self.__width, self.__height)

        self.__leftBorder = (-self.__width / 2) + 10
        self.__rightBorder = (self.__width / 2) - 20
        self.__topBorder = (self.__height / 2) - 10
        self.__bottomBorder = (-self.__height / 2) + 20
        self.drawCourt()

        self.__wKey = KeyEvent('w')
        self.__sKey = KeyEvent('s')
        self.__upKey = KeyEvent('Up')
        self.__downKey = KeyEvent('Down')

        self.__player1 = Paddle(-self.__width/2.5)
        self.__player2 = Paddle(self.__width/2.5)
        self.__player1.show()
        self.__player2.show()

        self.__square = Square()

    def drawCourt(self):
        self.__court = turtle.Turtle(visible=False)
        self.__court.speed(0)
        self.__court.pensize(5)
        self.__court.penup()
        self.__court.goto(self.__leftBorder, self.__topBorder)
        self.__court.pendown()
        self.__court.goto(self.__leftBorder, self.__bottomBorder)
        self.__court.goto(self.__rightBorder, self.__bottomBorder)
        self.__court.goto(self.__rightBorder, self.__topBorder)
        self.__court.goto(self.__leftBorder, self.__topBorder)

    def move(self):
        ms = 10
        if self.__wKey.down and not self.__sKey.down:
            self.__player1.moveUp(self.__topBorder)
            ms -= 5

        if self.__sKey.down and not self.__wKey.down:
            self.__player1.moveDown(self.__bottomBorder)
            ms -= 5

        if self.__upKey.down and not self.__downKey.down:
            self.__player2.moveUp(self.__topBorder)
            ms -= 5

        if self.__downKey.down and not self.__upKey.down:
            self.__player2.moveDown(self.__bottomBorder)
            ms -= 5

        print(ms)
        self.__window.ontimer(self.move, ms)

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def mainloop(self):
        self.move()
        self.__window.listen()
        self.__window.mainloop()
