import turtle
import random
import time

delay = 0.1
score = 0
highest_score = 0

# Snake body
bodies = []

# Getting a canvas
s = turtle.Screen()
s.title("SNAKE GAME BY SOHAIL")
s.bgcolor("gray")
s.setup(width=600, height=600)

# Create snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("#e8d9b6")  # Light brown color for snake head
head.fillcolor("#cda061")  # Dark brown color for snake head
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Create snake body
for _ in range(3):  # Start with a snake of length 3
    body = turtle.Turtle()
    body.speed(0)
    body.shape("circle")
    body.color("#e8d9b6")  # Light brown color for snake body
    body.fillcolor("#cda061")  # Dark brown color for snake body
    body.penup()
    bodies.append(body)

# Position the snake body segments
for i in range(len(bodies)):
    bodies[i].goto(0, -20 * i)

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.fillcolor("green")
food.penup()
food.goto(0, 200)

# Score board
sb = turtle.Turtle()
sb.shape("square")
sb.fillcolor("black")
sb.penup()
sb.ht()
sb.goto(-250, -250)
sb.write("Score: 0 | Highest Score: 0")

def move_up():
    if head.direction != "down":
        head.direction = "up"

def move_down():
    if head.direction != "up":
        head.direction = "down"

def move_left():
    if head.direction != "right":
        head.direction = "left"

def move_right():
    if head.direction != "left":
        head.direction = "right"

def move_stop():
    head.direction = "stop"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Handling keys
s.listen()
s.onkey(move_up, "w")
s.onkey(move_down, "s")
s.onkey(move_right, "d")
s.onkey(move_left, "a")
s.onkey(move_stop, "space")

# Main loop
while True:
    s.update()  # Update the screen

    # Check collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        for body in bodies:
            body.goto(1000, 1000)
        bodies.clear()
        score = 0
        sb.clear()
        sb.write("Score: {} | Highest Score: {}".format(score, highest_score))
    
    # Check collision with food
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        # Add body to snake
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("circle")
        new_body.color("#e8d9b6")  # Light brown color for new body segment
        new_body.fillcolor("#cda061")  # Dark brown color for new body segment
        new_body.penup()
        bodies.append(new_body)

        # Update score
        score += 10
        if score > highest_score:
            highest_score = score
        sb.clear()
        sb.write("Score: {} | Highest Score: {}".format(score, highest_score))

    # Move the snake
    for index in range(len(bodies) - 1, 0, -1):
        x = bodies[index - 1].xcor()
        y = bodies[index - 1].ycor()
        bodies[index].goto(x, y)

    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)

    move()

    # Check collision with body
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for b in bodies:
                b.goto(1000, 1000)
            bodies.clear()
            score = 0
            sb.clear()
            sb.write("Score: {} | Highest Score: {}".format(score, highest_score))

    time.sleep(delay)

turtle.mainloop()
