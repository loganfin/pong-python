from gameWindow import GameWindow
from square import Square
from paddle import Paddle

def pong(): #[Jenna]
    '''creates a window object and calls mainloop function'''
    window = GameWindow()
    window.mainloop()

pong()
