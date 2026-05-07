import turtle

turtle.Screen().bgcolor("Orange")

sc = turtle.Screen()
sc.setup(400,300)

turtle.title("Welcome to Turtle Window")
board = turtle.Turtle()
for i in  range(4):
    board.forward(100)
    board.left(90)
    i=i+1
turtle.Screen().bgcolor("Orange")
board=turtle.Turtle()

board.forward(100)
board.left(120)
board.forward(100)

board.left(120)
board.forward(100)

board.penup()
board.right(150)
board.forward(50)

board.pendown()
board.right(90)
board.forward(100)

board.right(120)
board.forward(100)

board.right(120)
board.forward(100)
turtle.done()