import turtle

window = turtle.Screen()
pointer = turtle.Turtle()

# Set the pointer to a turtle
pointer.shape("turtle")


# Function to draw rectangles and triangles
def draw(sides, angle):
    for side in sides:
        pointer.forward(side)
        pointer.right(angle)


# Function to draw the eyes
def draw_eyes():
    pointer.begin_fill()
    pointer.circle(50)
    pointer.end_fill()
    pointer.fillcolor("white")
    pointer.begin_fill()
    pointer.circle(35)
    pointer.end_fill()
    pointer.fillcolor("black")


# Function to move the pointer without drawing on the screen
def move(x, y):
    pointer.penup()
    pointer.goto(x, y)
    pointer.pendown()


# Draw a Hexagon
for i in range(6):
    draw([100, 100, 100], 120)
    pointer.right(60)

pointer.clear()

# Draw Face

# Move to co-ordinates (-125, 125) to center face on screen and draw a rectangle
move(-125, 125)
draw([250, 250, 250, 250], 90)

# Draw a pair of ears
draw_eyes()
move(125, 125)
draw_eyes()

# Draw a pair of black eyes
move(60, 50)
pointer.begin_fill()
pointer.circle(20)
move(-60, 50)
pointer.circle(20)
pointer.end_fill()

# Draw a red nose
move(0, 0)
pointer.color("#FF0000")
pointer.begin_fill()
draw([20, 20, 20], -120)
pointer.end_fill()
window.colormode(255)
pointer.color((0, 0, 0))

# Put a smile on the face
move(-40, -50)
pointer.right(90)
pointer.circle(50, 180)

# Hide the pointer
pointer.hideturtle()

# Wait for user to close the window
window.mainloop()
