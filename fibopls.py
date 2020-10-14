import turtle
def squarededupdup(t, h, p) :
    if p != 0:
      t.up()
      t.forward(h/2)
      t.down()
      t.left(90)
      t.forward(h/2)
      for r in range (3):
          t.left(90)
          t.forward(h)
      t.left(90)
      t.forward(h/2)
      t.left(90)
      t.up()
      t.forward(h/2)
      squarededupdup(t, h/2, p-1)
    
    
    
def squarx(t, h, p):
    if p!=0:
        t.forward(h)
        t.right(90)
        t.forward(h)
        t.right(90)
        t.forward(h)
        t.right(90)
        t.forward(h)
        t.right(90)
        t.right(+10)
        squarx(t, h-3, p-1)

t = turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Fibonacci en pls")
t.color("#d79a10", "black")
t.speed(0)
squarx(t, 200, 70)
#squarededupdup(t, 300, 5)