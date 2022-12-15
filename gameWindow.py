'''
Logan created KeyEvent class.
'''

import turtle

from paddle import Paddle
from square import Square
from keyEvent import KeyEvent

class GameWindow:   #[Logan] & [Jenna]
    def __init__(self): #[Logan] & [Jenna]
        self.__width = 700
        self.__height = 550
        self.__margin = 25

        self.__window = turtle.Screen()
        self.__window.setup(self.__width, self.__height)

        self.__leftBorder = (-self.__width / 2) + self.__margin
        self.__rightBorder = (self.__width / 2) - self.__margin
        self.__topBorder = (self.__height / 2) - self.__margin
        self.__bottomBorder = (-self.__height / 2) + self.__margin
        self.drawCourt()

        self.__wKey = KeyEvent('w')
        self.__sKey = KeyEvent('s')
        self.__upKey = KeyEvent('Up')
        self.__downKey = KeyEvent('Down')
        self.__escKey = KeyEvent('Escape')

        self.__player1 = Paddle(-self.__width / 2.5, self.__height)
        self.__player2 = Paddle(self.__width / 2.5, self.__height)
        self.__player1.show()
        self.__player2.show()

        self.__square = Square()
        self.__square.show()

    def drawCourt(self):    #[Logan] & [Jenna]
        self.__court = turtle.Turtle(visible=False)
        self.__court.speed(0)
        self.__court.pensize(3)

            #draw outer border
        self.__court.penup()
        self.__court.goto(self.__leftBorder, self.__topBorder)
        self.__court.pendown()

        self.__court.goto(self.__leftBorder, self.__bottomBorder)
        self.__court.goto(self.__rightBorder, self.__bottomBorder)
        self.__court.goto(self.__rightBorder, self.__topBorder)
        self.__court.goto(self.__leftBorder, self.__topBorder)

            #draw middle line
        self.__court.penup()
        self.__court.goto(((self.__rightBorder - self.__leftBorder) / 2) + self.__leftBorder,
                            self.__topBorder)
        self.__court.setheading(270)
        self.__court.pensize(1)

        self.__court.pendown()
        self.__court.goto(((self.__rightBorder - self.__leftBorder) / 2) + self.__leftBorder,
                            self.__bottomBorder)

    def move(self): #[Logan]
        gameover = False
        time = 40   #in milliseconds

        gameover = self.__square.move(self.__topBorder, self.__bottomBorder,
                                        self.__leftBorder, self.__rightBorder,
                                        self.__player1, self.__player2)

        if gameover:
            self.__player1.reset()
            self.__player2.reset()

        if self.__escKey.pressed:
            self.quit()

        if self.__wKey.pressed and not self.__sKey.pressed:
            moved = self.__player1.moveUp(self.__topBorder)
            if moved:
                time -= 20

        if self.__sKey.pressed and not self.__wKey.pressed:
            moved = self.__player1.moveDown(self.__bottomBorder)
            if moved:
                time -= 20

        if self.__upKey.pressed and not self.__downKey.pressed:
            moved = self.__player2.moveUp(self.__topBorder)
            if moved:
                time -= 20

        if self.__downKey.pressed and not self.__upKey.pressed:
            moved = self.__player2.moveDown(self.__bottomBorder)
            if moved:
                time -= 20

        self.__window.ontimer(self.move, time)

    def quit(self):
        turtle.bye()

    def mainloop(self): #[Logan] & [Jenna]
        self.move()
        self.__window.listen()
        self.__window.mainloop()
