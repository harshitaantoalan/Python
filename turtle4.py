import turtle

# Create screen
screen = turtle.Screen()
screen.title("Fun with Shapes")
screen.bgcolor("lightblue")

# Create turtle
t = turtle.Turtle()
t.speed(3)
t.pensize(3)

# ---------------- TRIANGLE ----------------
t.penup()
t.goto(-250, 100)
t.pendown()

t.color("black", "yellow")
t.begin_fill()

for i in range(3):
    t.forward(100)
    t.left(120)

t.end_fill()

# Label
t.penup()
t.goto(-230, 70)
t.write("Equilateral Triangle")


t.penup()
t.goto(-50, 100)
t.pendown()

t.color("black", "green")
t.begin_fill()

for i in range(2):
    t.forward(140)
    t.right(90)
    t.forward(80)
    t.right(90)

t.end_fill()


t.penup()
t.goto(-20, 0)



t.penup()
t.goto(180, 100)
t.pendown()

t.color("black", "orange")
t.begin_fill()

for i in range(6):
    t.forward(70)
    t.right(60)

t.end_fill()


t.penup()
t.goto(190, 20)



t.hideturtle()


turtle.done()