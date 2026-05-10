import turtle as t
t.speed(0)
class Petal:
    def __init__(self, color, d):
        self.color = color
        self.d = d
    def draw(self):
        t.color(self.color)
        t.begin_fill()
        for i in range(8):
            t.circle(self.d//2, 90)
            t.left(90)
            t.circle(self.d//2, 90)
            t.right(45)
        t.end_fill()
        t.color('yellow')
        t.dot(self.d//2)
class Leaf:
    def __init__(self, d, direct):
        self.d = d
        self.dir = direct
    def draw(self):
        if self.dir == 'l':
            t.color('green')
            t.begin_fill()
            t.circle(self.d//2, 90)
            t.left(90)
            t.circle(self.d // 2, 90)
            t.end_fill()
            t.left(90)
        else:
            t.right(90)
            t.color('green')
            t.begin_fill()
            t.circle(self.d // 2, 90)
            t.left(90)
            t.circle(self.d // 2, 90)
            t.end_fill()
            t.left(180)
class Steam:
    def __init__(self, gradus, direct, length):
        self.g = gradus
        self.d = direct
        self.l = length
    def draw(self):
        t.color('green')
        t.begin_fill()
        if self.d == 'l':
            t.left(self.g)
            t.forward(self.l)
            t.right(self.g)
        else:
            t.right(self.g)
            t.forward(self.l)
            t.left(self.g)
class Flower:
    def __init__(self, steam, leaf, petal):
        self.s = steam
        self.l = leaf
        self.p = petal
    def draw(self):
        self.s.draw()
        self.l.draw()
        self.s.draw()
        self.p.draw()

t.left(90)
for i in range(0, 46, 10):
    t.penup()
    t.setpos(0, 0)
    t.pendown()
    s = Steam(i, "r", 100)
    p = Petal('red', 100)
    l = Leaf(100, "r")
    f = Flower(s, l, p)
    f.draw()
for i in range(0, 46, 10):
    t.penup()
    t.setpos(0, 0)
    t.pendown()
    s = Steam(i, "l", 100)
    p = Petal('red', 100)
    l = Leaf(100, "l")
    f = Flower(s, l, p)
    f.draw()
t.mainloop()