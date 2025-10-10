import turtle
import os

# Set up the screen
wn = turtle.Screen()
wn.title("Brick Breaker Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, -200)
ball.dx = 0.3
ball.dy = 0.3

# Bricks
bricks = []

for y in range(3):
    for x in range(-250, 300, 50):
        brick = turtle.Turtle()
        brick.speed(0)
        brick.shape("square")
        brick.color("green")
        brick.shapesize(stretch_wid=1, stretch_len=2)
        brick.penup()
        brick.goto(x, 250 - y*30)
        bricks.append(brick)

# Paddle movement
def paddle_right():
    x = paddle.xcor()
    x += 20
    if x < 250:
        paddle.setx(x)

def paddle_left():
    x = paddle.xcor()
    x -= 20
    if x > -250:
        paddle.setx(x)

wn.listen()
wn.onkeypress(paddle_right, "Right")
wn.onkeypress(paddle_left, "Left")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.xcor() > 290:
        ball.setx(290)
        ball.dx *= -1

    if ball.xcor() < -290:
        ball.setx(-290)
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.goto(0, -200)
        ball.dy *= -1

    # Paddle collision
    if (ball.ycor() > -260 and ball.ycor() < -240) and (ball.xcor() > paddle.xcor() - 50 and ball.xcor() < paddle.xcor() + 50):
        ball.sety(-240)
        ball.dy *= -1

    # Brick collision
    for brick in bricks:
        if (ball.ycor() + 10 > brick.ycor() - 10 and ball.ycor() - 10 < brick.ycor() + 10) and (ball.xcor() + 20 > brick.xcor() - 20 and ball.xcor() - 20 < brick.xcor() + 20):
            ball.dy *= -1
            brick.goto(1000, 1000)  # Hide brick
            bricks.remove(brick)
