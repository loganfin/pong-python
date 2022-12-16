from turtle import Turtle

class Score(Turtle):
    def __init__(self, xPos, yPos, player):
        super().__init__(visible = False)
        self.__score = 0
        self.__player = player
        self.speed(0)
        self.up()
        self.goto(xPos, yPos)
        self.drawScore()

    def add(self):
        self.__score += 1
        self.drawScore()
        pass

    def drawScore(self):
        self.clear()
        self.write(self.__player + ": " + str(self.__score), font=("Cambria", 20, "normal"))
