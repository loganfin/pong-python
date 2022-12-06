import turtle

from paddle import Paddle

class GameWindow:
    def __init__(self):
        self.__width = 800
        self.__height = 500

        self.__window = turtle.Screen()
        self.__window.setup(self.__width, self.__height)

        self.__player1 = Paddle(1)

        self.__window.onkey(self.forward, "Up")
        self.__window.onkey(self.backward, "Down")

        self.__window.listen()

    def get_width():
        return self.__width

    def get_height():
        return self.__height

    def forward(self):
        self.__player1.forward()

    def backward(self):
        self.__player1.backward()

    def mainloop(self):
        self.__window.mainloop()
