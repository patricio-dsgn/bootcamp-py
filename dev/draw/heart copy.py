import turtle as t

t.speed(0.1000)
t.bgcolor('black')
t.pensize(32)
def func():
    for i in range(200):
        t.right(1)
        t.forward(1)
t.color('red', 'pink')
t.begin_fill()
t.left(140)
t.forward(111.65)
func()
t.left(120)
func()
t.forward(111.65)
t.end_fill()
t.hideturtle()
t.done()