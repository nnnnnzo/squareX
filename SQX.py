import turtle
def squarx(t, h, p):
    if p!=0:
        for e in range (4):
            t.forward(h)
            t.right(90)
        t.right(+10)
        squarx(t, h-3, p-1)

t = turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("SquareX: Fibonacci en pls")
t.color("#d79a10", "black")
t.speed(0)
squarx(t, 200, 70)
