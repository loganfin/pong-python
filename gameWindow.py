import turtle

from paddle import Paddle

class GameWindow:
    def __init__(self):
        self.__width = 800
        self.__height = 500

        self.__window = turtle.Screen()
        self.__window.setup(self.__width, self.__height)

        self.__player1 = Paddle(-self.__width/3)
        self.__player2 = Paddle(self.__width/3)
        self.__player1.show()
        self.__player2.show()
        #self.__player2.setX(self.__width - self.__width/100)

        self.__window.onkey(self.__player1.moveUp, 'w')
        self.__window.onkey(self.__player1.moveDown, 's')
        self.__window.onkey(self.__player2.moveUp, "Up")
        self.__window.onkey(self.__player2.moveDown, "Down")

        self.__window.listen()

    def getWidth():
        return self.__width

    def getHeight():
        return self.__height

    def mainloop(self):
        self.__window.mainloop()
