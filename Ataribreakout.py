import turtle
import winsound
lives = 3

s = turtle.Screen()
s.title("Atari Breakout in Python by Raj Pandya")
s.bgcolor("black")
s.setup(1000,400)
s.tracer(0)

#Base
bottom = turtle.Turtle()
bottom.speed(0)
bottom.shape("square")
bottom.color("white")
bottom.penup()
bottom.shapesize(stretch_wid=1, stretch_len=15)
bottom.goto(0, -150)

#Text
text = turtle.Turtle()
text.speed(0)
text.color("white")
text.penup()
text.hideturtle
text.goto(-470, -180)
text.write(f"You have {lives} lives left", font=("Courier", 14, "normal"))

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.goto(0, -100)
ball.dx = 0.44
ball.dy = 0.38


#bricks 

#First Row
b1visible = True
brick1 = turtle.Turtle()
brick1.speed(0)
brick1.shape("square")
brick1.color("green")
brick1.penup()
brick1.shapesize(stretch_wid=1.5, stretch_len=6.5)
brick1.goto(-425, +170)

b2visible = True
brick2 = turtle.Turtle()
brick2.speed(0)
brick2.shape("square")
brick2.color("blue")
brick2.penup()
brick2.shapesize(stretch_wid=1.5, stretch_len=10)
brick2.goto(-250, +170)

b3visible = True
brick3 = turtle.Turtle()
brick3.speed(0)
brick3.shape("square")
brick3.color("red")
brick3.penup()
brick3.shapesize(stretch_wid=1.5, stretch_len=12)
brick3.goto(-10, +170)

b4visible = True
brick4 = turtle.Turtle()
brick4.speed(0)
brick4.shape("square")
brick4.color("yellow")
brick4.penup()
brick4.shapesize(stretch_wid=1.5, stretch_len=8)
brick4.goto(205, +170)

b5visible = True
brick5 = turtle.Turtle()
brick5.speed(0)
brick5.shape("square")
brick5.color("purple")
brick5.penup()
brick5.shapesize(stretch_wid=1.5, stretch_len=9)
brick5.goto(390, +170)

#Second Row
b6visible = True
brick6 = turtle.Turtle()
brick6.speed(0)
brick6.shape("square")
brick6.color("purple")
brick6.penup()
brick6.shapesize(stretch_wid=1.5, stretch_len=9)
brick6.goto(-400, +130)

b7visible = True
brick7 = turtle.Turtle()
brick7.speed(0)
brick7.shape("square")
brick7.color("yellow")
brick7.penup()
brick7.shapesize(stretch_wid=1.5, stretch_len=7)
brick7.goto(-225, +130)

b8visible = True
brick8 = turtle.Turtle()
brick8.speed(0)
brick8.shape("square")
brick8.color("green")
brick8.penup()
brick8.shapesize(stretch_wid=1.5, stretch_len=10)
brick8.goto(-40, +130)

b9visible = True
brick9 = turtle.Turtle()
brick9.speed(0)
brick9.shape("square")
brick9.color("red")
brick9.penup()
brick9.shapesize(stretch_wid=1.5, stretch_len=6)
brick9.goto(135, +130)

b10visible = True
brick10 = turtle.Turtle()
brick10.speed(0)
brick10.shape("square")
brick10.color("orange")
brick10.penup()
brick10.shapesize(stretch_wid=1.5, stretch_len=13.5)
brick10.goto(345, +130)

#Movement
def bottom_left():
    x = bottom.xcor()
    if x-160>=-490:
        x-=15
    bottom.setx(x)
def bottom_right():
    x = bottom.xcor()
    if x+160<=490:
        x+=15
    bottom.setx(x)


#keyboard Input

s.listen()
s.onkeypress(bottom_left, "a")
s.onkeypress(bottom_right, "d")

while True:
    s.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if b1visible is False:
        brick1.hideturtle()
    if b2visible is False:
        brick2.hideturtle()
    if b3visible is False:
        brick3.hideturtle()
    if b4visible is False:
        brick4.hideturtle()
    if b5visible is False:
        brick5.hideturtle()
    if b6visible is False:
        brick6.hideturtle()
    if b7visible is False:
        brick7.hideturtle()
    if b8visible is False:
        brick8.hideturtle()
    if b9visible is False:
        brick9.hideturtle()
    if b10visible is False:
        brick10.hideturtle()

    #Border
    if ball.xcor()>490:
        ball.setx(490)
        ball.dx *=-1
    if ball.xcor()<-490:
        ball.setx(-490)
        ball.dx *=-1
    if ball.ycor()>190:
        ball.sety(190)
        ball.dy *=-1
    if ball.ycor()<-190:
        ball.goto(0, -100)
        ball.dy *= -1
        lives-=1
        text.clear()
        text.write(f"You have {lives} lives left", font=("Courier", 14, "normal"))
    #Collision of the Paddle and ball
    if ball.ycor() <= bottom.ycor()  and ball.xcor()>bottom.xcor()-160 and ball.xcor()<bottom.xcor()+160:
        ball.sety(bottom.ycor())
        ball.dy *= -1
        winsound.PlaySound("ping_pong_8bit_peeeeeep.wav", winsound.SND_ASYNC)

    #Collision of the Bricks

    #Brick 1:
    if ball.xcor() >brick1.xcor()-65 and ball.xcor()<brick1.xcor()+65 and ball.ycor()> brick1.ycor()-15 and ball.ycor()<brick1.ycor()+15 and b1visible is True:
        ball.dy *= -1
        b1visible = False
        winsound.PlaySound("ping_pong_8bit_peeeeeep.wav", winsound.SND_ASYNC)
    #Brick 2: 
    if ball.xcor() >brick2.xcor()-100 and ball.xcor()<brick2.xcor()+100 and ball.ycor()> brick2.ycor()-15 and ball.ycor()<brick2.ycor()+15 and b2visible is True:
        ball.dy *= -1
        b2visible = False
        winsound.PlaySound("ping_pong_8bit_peeeeeep.wav", winsound.SND_ASYNC)

    #Brick 3: 
    if ball.xcor() >brick3.xcor()-120 and ball.xcor()<brick3.xcor()+120 and ball.ycor()> brick3.ycor()-15 and ball.ycor()<brick3.ycor()+15 and b3visible is True:
        ball.dy *= -1
        b3visible = False
        winsound.PlaySound("ping_pong_8bit_peeeeeep.wav", winsound.SND_ASYNC)

    #Brick 4: 
    if ball.xcor() >brick4.xcor()-80 and ball.xcor()<brick4.xcor()+80 and ball.ycor()> brick4.ycor()-15 and ball.ycor()<brick4.ycor()+15 and b4visible is True:
        ball.dy *= -1
        b4visible = False
        winsound.PlaySound("ping_pong_8bit_peeeeeep.wav", winsound.SND_ASYNC)

    #Brick 5: 
    if ball.xcor() >brick5.xcor()-90 and ball.xcor()<brick5.xcor()+90 and ball.ycor()> brick5.ycor()-15 and ball.ycor()<brick5.ycor()+15 and b5visible is True:
        ball.dy *= -1
        b5visible = False
        winsound.PlaySound("ping_pong_8bit_peeeeeep.wav", winsound.SND_ASYNC)

    #Brick 6: 
    if ball.xcor() >brick6.xcor()-90 and ball.xcor()<brick6.xcor()+90 and ball.ycor()> brick6.ycor()-15 and ball.ycor()<brick6.ycor()+15 and b6visible is True:
        ball.dy *= -1
        b6visible = False
        winsound.PlaySound("ping_pong_8bit_peeeeeep.wav", winsound.SND_ASYNC)

    #Brick 7: 
    if ball.xcor() >brick7.xcor()-70 and ball.xcor()<brick7.xcor()+70 and ball.ycor()> brick7.ycor()-15 and ball.ycor()<brick7.ycor()+15 and b7visible is True:
        ball.dy *= -1
        b7visible = False
        winsound.PlaySound("ping_pong_8bit_peeeeeep.wav", winsound.SND_ASYNC)

    #Brick 8: 
    if ball.xcor() >brick8.xcor()-100 and ball.xcor()<brick8.xcor()+100 and ball.ycor()> brick8.ycor()-15 and ball.ycor()<brick8.ycor()+15 and b8visible is True:
        ball.dy *= -1
        b8visible = False
        winsound.PlaySound("ping_pong_8bit_peeeeeep.wav", winsound.SND_ASYNC)

    #Brick 9: 
    if ball.xcor() >brick9.xcor()-60 and ball.xcor()<brick9.xcor()+60 and ball.ycor()> brick9.ycor()-15 and ball.ycor()<brick9.ycor()+15 and b9visible is True:
        ball.dy *= -1
        b9visible = False
        winsound.PlaySound("ping_pong_8bit_peeeeeep.wav", winsound.SND_ASYNC)

    #Brick 10:
    if ball.xcor() >= brick10.xcor()-135 and ball.xcor()<=brick10.xcor()+135 and ball.ycor()> brick10.ycor()-15 and ball.ycor()<brick10.ycor()+15 and b10visible is True:
        ball.dy *= -1
        b10visible = False
        winsound.PlaySound("ping_pong_8bit_peeeeeep.wav", winsound.SND_ASYNC)

    #Lose
    if lives == 0:
        text.clear()
        text.goto(-100, 0)
        text.write("You Lost", font=("Courier", 40, "normal"))
        ball.dy = 0
        ball.dx = 0
        winsound.PlaySound("ping_pong_8bit_peeeeeep.wav", winsound.SND_ASYNC)
    elif b1visible is False and b2visible is False and b3visible is False  and b4visible is False and b5visible is False and b6visible is False and b7visible is False and b8visible is False and b9visible is False and b10visible is False:
        text.clear()
        text.goto(-100, 0)
        text.write("You Win", font=("Courier", 40, "normal"))
        ball.dy = 0
        ball.dx = 0
        winsound.PlaySound("ping_pong_8bit_peeeeeep.wav", winsound.SND_ASYNC)

