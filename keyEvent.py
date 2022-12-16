import turtle

class KeyEvent: #[Logan]
    def __init__(self, key):
        '''
        creates a key event object
        registers whether or not a particular key was pressed
        '''
        self.__key = key
        self.pressed = False

        turtle.onkeypress(self.press, self.__key)
        turtle.onkeyrelease(self.release, self.__key)

    def press(self):
        '''registers that the key was pressed'''
        self.pressed = True

    def release(self):
        '''registers that the key was released'''
        self.pressed = False
