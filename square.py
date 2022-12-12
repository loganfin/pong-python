import turtle

class Square(turtle.Turtle):   #[Jenna]
    def __init__(self):
        super().__init__(visible = False)
        self.speed(0)
        self.shape("square")
        self.color("grey")
        self.speed("slowest")
        self.penup()
        self.showturtle()

        self.__halfHeight = abs(self.get_shapepoly()[0][1]) + 2
        self.dx = 10
        self.dy = 10
        self.__distance = 10

    def move(self, top, bottom, left, right):
        #for i in range(10):
        if self.ycor() + self.__halfHeight > top:
            self.sety(top - self.__halfHeight)
            self.dy *= -1

        if self.ycor() - self.__halfHeight < bottom:
            self.sety(bottom + self.__halfHeight)
            self.dy *= -1

        if self.xcor() + self.__halfHeight > right:
            self.setx(right - self.__halfHeight)
            self.ht()
            self.goto(0, 0)
            self.st()
            self.dx *= -1

        if self.xcor() - self.__halfHeight < left:
            self.setx(left + self.__halfHeight)
            self.ht()
            self.goto(0, 0)
            self.st()
            self.dx *= -1

        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)
