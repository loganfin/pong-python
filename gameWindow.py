import turtle

from paddle import Paddle
from square import Square

class WatchedKey:
    def __init__(self, key):
        self.key = key
        self.down = False
        turtle.onkeypress(self.press, key)
        turtle.onkeyrelease(self.release, key)

    def press(self):
        self.down = True

    def release(self):
        self.down = False

class GameWindow:
    def __init__(self):
        self.__width = 700
        self.__height = 500

        self.__window = turtle.Screen()
        self.__window.setup(self.__width, self.__height)

        self.__player1 = Paddle(-self.__width/3)
        self.__player2 = Paddle(self.__width/3)
        self.__square = Square()
        #self.drawCourt()
        self.__player1.show()
        self.__player2.show()
        self.move()
        #self.__player2.setX(self.__width - self.__width/100)

    #def drawCourt():

    def move(self):
        self.w_key = WatchedKey('w')
        self.s_key = WatchedKey('s')
        self.up_key = WatchedKey('Up')
        self.down_key = WatchedKey('Down')


        while (True):
            if self.w_key.down == True:
                self.__player1.moveUp()
            if self.s_key.down:
                self.__player1.moveDown()
            if self.up_key.down == True:
                self.__player2.moveUp()
            if self.down_key.down:
                self.__player2.moveDown()
            self.__window.update()
            self.__window.listen()
        #print(self.w_key.down)

        self.__window.ontimer(self.move, 10)
        #self.__window.onclick(print_state)
        self.__window.update()
        self.__window.listen()
        #self.__window.onkeypress(self.p1Up, 'w')
        #self.__window.onkeypress(self.p1Down, 's')
        #self.__window.onkeyrelease(None, "w")
        #self.__window.onkeyrelease(None, "s")

        #self.__window.onkeypress(self.p2Up, 'Up')
        #self.__window.onkeypress(self.p2Down, 'Down')
        #self.__window.onkeyrelease(None, "Up")
        #self.__window.onkeyrelease(None, "Down")
        #self.__window.onkeyrelease(self.__player2.moveUp, "Up")
        #self.__window.onkeyrelease(self.__player2.moveDown, "Down")

        #self.__window.update()
        #self.__window.listen()

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def p1Up(self):
        self.__player1.moveUp()
        self.__window.ontimer(self.p1Up, 10)

    def p1Down(self):
        self.__player1.moveDown()
        self.__window.ontimer(self.p1Down, 10)

    def p2Up(self):
        self.__player2.moveUp()
        self.__window.ontimer(self.p2Up, 10)

    def p2Down(self):
        self.__player2.moveDown()
        self.__window.ontimer(self.p2Down, 10)

    def mainloop(self):
        self.__window.mainloop()


