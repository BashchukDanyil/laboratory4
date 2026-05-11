import turtle as t
t.speed(0)
class Figure:
    def __init__(self, x, y, color, d):
        self.x = x
        self.y = y
        self.color = color
        self.d = d
    def move(self):
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
    def draw(self):
        t.pencolor(self.color)
        t.fillcolor(self.color)
    def delate(self):
        t.pencolor("white")
        t.fillcolor("white")

class Petal(Figure):
    def __init__(self, color, d, x = 0, y = 0):
        super().__init__(x, y, color, d)
        self.flag = False
    def draw(self):
        if not(self.flag):
            super().draw()
            t.begin_fill()
            for i in range(8):
                t.circle(self.d//2, 90)
                t.left(90)
                t.circle(self.d//2, 90)
                t.right(45)
            t.end_fill()
            self.flag = True
            self.x = t.xcor()
            self.y = t.ycor()
        else:
            self.delate()
            super().draw()
            t.begin_fill()
            for i in range(8):
                t.circle(self.d // 2, 90)
                t.left(90)
                t.circle(self.d // 2, 90)
                t.right(45)
            t.end_fill()
            self.flag = True
            self.x = t.xcor()
            self.y = t.ycor()
    def delate(self):
        if self.flag:
            x = t.xcor()
            y = t.ycor()
            a = t.heading()
            t.right(a - 90)
            super().move()
            super().delate()
            t.begin_fill()
            for i in range(8):
                t.circle(self.d//2, 90)
                t.left(90)
                t.circle(self.d//2, 90)
                t.right(45)
            t.end_fill()
            t.penup()
            t.goto(x, y)
            t.pendown()
            t.left(a - 90)
            self.flag = False
        else:
            pass
class CentralDot(Figure):
    def __init__(self, color, d, x = 0, y = 0):
        super().__init__(x, y, color, d)
        self.flag = False
    def draw(self):
        if not(self.flag):
            super().draw()
            t.dot(self.d // 2)
            self.flag = True
            self.x = t.xcor()
            self.y = t.ycor()
        else:
            self.delate()
            super().draw()
            t.dot(self.d // 2)
            self.x = t.xcor()
            self.y = t.ycor()
    def delate(self):
        if self.flag:
            x = t.xcor()
            y = t.ycor()
            a = t.heading()
            t.right(a - 90)
            super().move()
            super().delate()
            t.dot(self.d // 2)
            t.penup()
            t.goto(x, y)
            t.pendown()
            t.left(a - 90)
            self.flag = False
        else:
            pass
class Leaf(Figure):
    def __init__(self, color, d, direct, x = 0, y = 0):
        if isinstance(color, Leaf):
            super().__init__(x, y, color.color, color.d)
            self.dir = direct
        else:
            super().__init__(x, y, color, d)
            self.dir = direct
        self.flag = False
    def draw(self):
        if not(self.flag):
            super().draw()
            if self.dir == 'l':
                t.begin_fill()
                t.circle(self.d//2, 90)
                t.left(90)
                t.circle(self.d // 2, 90)
                t.end_fill()
                t.left(90)
            else:
                t.right(90)
                t.begin_fill()
                t.circle(self.d // 2, 90)
                t.left(90)
                t.circle(self.d // 2, 90)
                t.end_fill()
                t.left(180)
            self.flag = True
            self.x = t.xcor()
            self.y = t.ycor()
        else:
            self.delate()
            super().draw()
            if self.dir == 'l':
                t.begin_fill()
                t.circle(self.d // 2, 90)
                t.left(90)
                t.circle(self.d // 2, 90)
                t.end_fill()
                t.left(90)
            else:
                t.right(90)
                t.begin_fill()
                t.circle(self.d // 2, 90)
                t.left(90)
                t.circle(self.d // 2, 90)
                t.end_fill()
                t.left(180)
            self.x = t.xcor()
            self.y = t.ycor()
    def delate(self):
        if self.flag:
            x = t.xcor()
            y = t.ycor()
            a = t.heading()
            t.right(a - 90)
            super().move()
            super().delate()
            if self.dir == 'l':
                t.begin_fill()
                t.circle(self.d//2, 90)
                t.left(90)
                t.circle(self.d // 2, 90)
                t.end_fill()
                t.left(90)
            else:
                t.right(90)
                t.begin_fill()
                t.circle(self.d // 2, 90)
                t.left(90)
                t.circle(self.d // 2, 90)
                t.end_fill()
                t.left(180)
            t.penup()
            t.goto(x, y)
            t.pendown()
            t.left(a - 90)
            self.flag = False
        else:
            pass
class Steam(Figure):
    def __init__(self, color, gradus = 0, direct = "r", length = 0, x = 0, y = 0):
        if isinstance(color, Steam):
            super().__init__(x, y, color.color, color.d)
            self.g = color.g
            self.dir = color.dir
        else:
            super().__init__(x, y, color, length)
            self.g = gradus
            self.dir = direct
        self.flag = False
    def draw(self):
        if not(self.flag):
            super().draw()
            self.x = t.xcor()
            self.y = t.ycor()
            if self.dir == 'l':
                t.left(self.g)
                t.forward(self.d)
                t.right(self.g)
            else:
                t.right(self.g)
                t.forward(self.d)
                t.left(self.g)
            self.flag = True
        else:
            self.delate()
            self.x = t.xcor()
            self.y = t.ycor()
            super().draw()
            if self.dir == 'l':
                t.left(self.g)
                t.forward(self.d)
                t.right(self.g)
            else:
                t.right(self.g)
                t.forward(self.d)
                t.left(self.g)
    def delate(self):
        if self.flag:
            x = t.xcor()
            y = t.ycor()
            a = t.heading()
            t.right(a - 90)
            super().move()
            super().delate()
            if self.dir == 'l':
                t.left(self.g)
                t.forward(self.d)
                t.right(self.g)
            else:
                t.right(self.g)
                t.forward(self.d)
                t.left(self.g)
            t.penup()
            t.goto(x, y)
            t.pendown()
            t.left(a - 90)
            self.flag = False
        else:
            pass
class Flower:
    def __init__(self, steam, leaf, petal, centraldot):
        self.s = steam
        self.l = leaf
        self.p = petal
        self.c = centraldot
        self.cup = []
    def draw(self):
        self.s.move()
        self.s.draw()
        s_new = Steam(self.s)
        self.l.draw()
        s_new.draw()
        self.cup.append(s_new)
        self.p.draw()
        self.c.draw()
    def delate(self):
        self.s.move()
        self.s.delate()
        s_new = self.cup[0]
        self.l.delate()
        s_new.delate()
        self.p.delate()
        self.c.delate()

t.left(90)
A = []
for i in range(0, 46, 10):
    s = Steam("green", i, "r", 100, 100, 100)
    p = Petal('red', 100)
    l = Leaf('green',100, "r")
    c = CentralDot('yellow', 100)
    f = Flower(s, l, p, c)
    A.append(f)
    f.draw()
for i in range(0, 46, 10):
    s = Steam("green", i, "l", 100, 100, 100)
    p = Petal('red', 100)
    l = Leaf('green', 100, "l")
    c = CentralDot('yellow', 100)
    f = Flower(s, l, p, c)
    A.append(f)
    f.draw()
for f in A:
    f.delate()
t.mainloop()