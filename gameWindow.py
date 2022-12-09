'''
Logan created KeyEvent class.
'''

from turtle import Turtle
from turtle import Screen

from paddle import Paddle
from square import Square
from keyEvent import KeyEvent

class GameWindow:   #[Logan] & [Jenna]
    def __init__(self): #[Logan] & [Jenna]
        self.__width = 700
        self.__height = 550
        self.__margin = 25

        self.__window = Screen()
        self.__window.setup(self.__width, self.__height)

        '''
        self.__leftBorder = (-self.__width / 2) + 10
        self.__rightBorder = (self.__width / 2) - 20
        self.__topBorder = (self.__height / 2) - 10
        self.__bottomBorder = (-self.__height / 2) + 20
        '''
        self.__leftBorder = (-self.__width / 2) + self.__margin
        self.__rightBorder = (self.__width / 2) - self.__margin
        self.__topBorder = (self.__height / 2) - self.__margin
        self.__bottomBorder = (-self.__height / 2) + self.__margin
        self.drawCourt()

        self.__wKey = KeyEvent('w')
        self.__sKey = KeyEvent('s')
        self.__upKey = KeyEvent('Up')
        self.__downKey = KeyEvent('Down')

        self.__player1 = Paddle(-self.__width / 2.5, self.__height)
        self.__player2 = Paddle(self.__width / 2.5, self.__height)
        self.__player1.show()
        self.__player2.show()

        self.__square = Square()

    def drawCourt(self):    #[Logan]
        self.__court = Turtle(visible=False)
        self.__court.speed(0)
        self.__court.pensize(3)

        self.__court.penup()
        self.__court.goto(self.__leftBorder, self.__topBorder)
        self.__court.pendown()

        self.__court.goto(self.__leftBorder, self.__bottomBorder)
        self.__court.goto(self.__rightBorder, self.__bottomBorder)
        self.__court.goto(self.__rightBorder, self.__topBorder)
        self.__court.goto(self.__leftBorder, self.__topBorder)

        self.__court.penup()
        self.__court.goto(((self.__rightBorder - self.__leftBorder) / 2) + self.__leftBorder, self.__topBorder)
        self.__court.setheading(270)
        self.__court.pensize(1)

        self.__court.pendown()
        self.__court.goto(((self.__rightBorder - self.__leftBorder) / 2) + self.__leftBorder, self.__bottomBorder)

    def move(self): #[Logan]
        if self.__wKey.pressed and not self.__sKey.pressed:
            self.__player1.moveUp(self.__topBorder)

        if self.__sKey.pressed and not self.__wKey.pressed:
            self.__player1.moveDown(self.__bottomBorder)

        if self.__upKey.pressed and not self.__downKey.pressed:
            self.__player2.moveUp(self.__topBorder)

        if self.__downKey.pressed and not self.__upKey.pressed:
            self.__player2.moveDown(self.__bottomBorder)

        self.__window.ontimer(self.move, 10)

    def mainloop(self): #[Logan] & [Jenna]
        self.move()
        self.__window.listen()
        self.__window.mainloop()
