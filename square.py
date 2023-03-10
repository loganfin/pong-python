from turtle import Turtle

class Square(Turtle):   #[Jenna] & [Logan]
    def __init__(self): #[Jenna] & [Logan]
        '''initialize attributes of moving square'''
        super().__init__(visible = False)
        self.speed(0)
        self.shape("square")
        self.color("grey")
        self.speed("slowest")
        self.setheading(180)
        self.penup()
        self.showturtle()

        self.__halfHeight = abs(self.get_shapepoly()[0][1]) + 5
        self.dx = 10
        self.dy = 0
        self.__distance = 10

    def move(self, top, bottom, left, right, leftPaddle, rightPaddle):  #[Jenna] & [Logan]
        '''
        defines squares movements depending on what the square collides with
        returns True and 0 if game is over
        returns False if game is not over and 1 if player 1 wins or 2 if player 2 wins
        '''
        gameover = False

            #collision with top boundary
        if self.ycor() + self.__halfHeight > top:
            self.sety(top - self.__halfHeight)
            self.dy *= -1
            return gameover, 0

            #collision with bottom boundary
        if self.ycor() - self.__halfHeight < bottom:
            self.sety(bottom + self.__halfHeight)
            self.dy *= -1
            return gameover, 0

            #collision with side of right paddle
        if self.xcor() + self.__halfHeight > rightPaddle.xcor() - 10:
            if self.ycor() < rightPaddle.ycor() + rightPaddle.halfHeight and\
                    self.ycor() > rightPaddle.ycor() - rightPaddle.halfHeight and\
                    self.xcor() < rightPaddle.xcor() - 10:

                self.color(rightPaddle.color()[0])
                self.setx(rightPaddle.xcor() - 10 - self.__halfHeight)
                self.dx *= -1

                if self.ycor() >= rightPaddle.ycor():
                    self.dy = 10
                else:
                    self.dy = -10
                return gameover, 0

            #collision with side of left paddle
        if self.xcor() - self.__halfHeight < leftPaddle.xcor() + 10:
            if self.ycor() < leftPaddle.ycor() + leftPaddle.halfHeight and\
                    self.ycor() > leftPaddle.ycor() - leftPaddle.halfHeight and\
                    self.xcor() > leftPaddle.xcor() + 10:

                self.color(leftPaddle.color()[0])
                self.setx(leftPaddle.xcor() + 10 + self.__halfHeight)
                self.dx *= -1

                if self.ycor() >= leftPaddle.ycor():
                    self.dy = 10
                else:
                    self.dy = -10
                return gameover, 0

            #collision with right boundary
        if self.xcor() + self.__halfHeight > right:
            self.setx(right - self.__halfHeight)
            self.reset()
            self.dx *= -1
            gameover = True
            return gameover, 1

            #collision with left boundary
        if self.xcor() - self.__halfHeight < left:
            self.setx(left + self.__halfHeight)
            self.reset()
            self.dx *= -1
            gameover = True
            return gameover, 2

        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)
        return gameover, 0

    def show(self): #[Logan]
        '''shows square object'''
        self.showturtle()

    def reset(self):    #[Logan] & [Jenna]
        '''resets square object to be at the origin'''
        self.hideturtle()
        self.goto(0, 0)
        self.dy = 0
        self.showturtle()
