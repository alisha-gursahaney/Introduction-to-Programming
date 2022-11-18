import turtle
Toby = turtle.Turtle()
Toby.shape("turtle")
Toby.speed(0)
Toby.home()
Toby.color("HotPink")
side = 20
for i in range(1, 110):
    Toby.forward(side)
    Toby.left(120)
    side = side + 5
    Toby.left(5)
Toby.home()
Toby.color("CornflowerBlue")
side2 = 20
Toby.left(10)
for i in range(1, 110):
    Toby.forward(side2)
    Toby.left(120)
    side2 = side2 +5
    Toby.left(5)
Toby.home()
Toby.color("MediumSlateBlue")
side3 = 20
Toby.left(20)
for i in range(1, 110):
    Toby.forward(side3)
    Toby.left(120)
    side3 = side3 +5
    Toby.left(5)
Toby.home()
turtle.done()
