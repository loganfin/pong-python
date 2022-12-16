from turtle import Turtle

class Score(Turtle):    #[Logan]
    def __init__(self, xPos, yPos, player):
        '''keeps track of the score of each player'''
        super().__init__(visible = False)
        self.__score = 0
        self.__player = player
        self.speed(0)
        self.up()
        self.goto(xPos, yPos)
        self.drawScore()

    def getScore(self):
        '''returns score of player'''
        return self.__score

    def add(self):
        '''adds a point to a player'''
        self.__score += 1
        self.drawScore()
        pass

    def drawScore(self):
        '''updates score on screen'''
        self.clear()
        self.write(self.__player + ": " + str(self.__score), font=("Cambria", 20, "normal"))
