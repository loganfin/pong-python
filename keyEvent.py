import turtle

class KeyEvent: #[Logan]
    def __init__(self, key):
        self.__key = key
        self.pressed = False

        turtle.onkeypress(self.press, self.__key)
        turtle.onkeyrelease(self.release, self.__key)

    def press(self):
        self.pressed = True

    def release(self):
        self.pressed = False
