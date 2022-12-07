import turtle

from paddle import Paddle

class GameWindow:
    def __init__(self):
        self.__width = 800
        self.__height = 500

        self.__window = turtle.Screen()
        self.__window.setup(self.__width, self.__height)

        self.__player1 = Paddle(1)
        self.__player2 = Paddle(2)

        self.__window.onkey(self.p1Up, 'w')
        self.__window.onkey(self.p1Down, 's')
        self.__window.onkey(self.p2Up, "Up")
        self.__window.onkey(self.p2Down, "Down")

        self.__window.listen()

    def getWidth():
        return self.__width

    def getHeight():
        return self.__height

    def p1Up(self):
        self.__player1.moveUp()

    def p1Down(self):
        self.__player1.moveDown()

    def p2Up(self):
        self.__player2.moveUp()

    def p2Down(self):
        self.__player2.moveDown()

    def mainloop(self):
        self.__window.mainloop()
