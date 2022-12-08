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

        self.__player1 = Paddle(-self.__width/3)
        self.__player2 = Paddle(self.__width/3)
        self.__player1.show()
        self.__player2.show()

        self.__wKey = KeyEvent('w')
        self.__sKey = KeyEvent('s')
        self.__upKey = KeyEvent('Up')
        self.__downKey = KeyEvent('Down')

        self.__square = Square()

    def move(self):
        if self.__wKey.down and not self.__sKey.down:
            self.__player1.moveUp()

        if self.__sKey.down and not self.__wKey.down:
            self.__player1.moveDown()

        if self.__upKey.down and not self.__downKey.down:
            self.__player2.moveUp()

        if self.__downKey.down and not self.__upKey.down:
            self.__player2.moveDown()

        self.__window.ontimer(self.move, 10)

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def mainloop(self):
        self.move()
        self.__window.listen()
        self.__window.mainloop()
