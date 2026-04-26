import turtle

# Turtle screen
screen = turtle.Screen()
screen.bgcolor("skyblue")  # Separate background color

turtle = turtle.Turtle()
turtle.shape("turtle")    # Change turtle object shape
turtle.color("purple")    # Turtle's own color
turtle.speed(3)           # Sets drawing pace

# Draw the square
turtle.penup()
turtle.goto(-50, -50)     # Position turtle for the base
turtle.pendown()
turtle.pencolor("green")  # Outline of the square must be green

sides_drawn = 0
while sides_drawn < 4:
    turtle.forward(100)
    turtle.left(90)
    sides_drawn += 1

# Draw the triangle
# Move to the top of the square base
turtle.penup()
turtle.goto(-50, 50)
turtle.pendown()

turtle.fillcolor("green") # Triangle must be filled with green
turtle.begin_fill()

for _ in range(3):
    turtle.forward(100)
    turtle.left(120)

turtle.end_fill()

turtle.hideturtle()
print("Drawing complete. Close the window to exit.")
screen.mainloop() 