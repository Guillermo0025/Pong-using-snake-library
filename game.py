import turtle


'''INITIALIZING SCREEN'''
wn = turtle.Screen()
#defines graphic windows as a drawing playground
wn.title("Pign Pogn :o")
wn.bgcolor("black")
#setting up the size of the window
wn.setup(width=900, height=700)
#sets delay for update drawing
wn.tracer(0)

'''SCORING'''
score_a = 0
score_b = 0

'''CREATING PADDLE A'''
#creating a turtle object
paddle_a = turtle.Turtle()
#setting speed of line drawing and turtle drwaing at the 
#maximum possible speed
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
#pen up is useful if we dont want to leave a trace of the
#previous movements, meaning that this way the pen is up and
#it will not leave any trace
paddle_a.penup()
#starting possition
paddle_a.goto(-400, 0)
#the default size is 20px, so we are multiplying 20*5
#on the width part, and we are multiplying the lenght
#by 1
paddle_a.shapesize(stretch_wid = 6, stretch_len = 1)

'''CREATING PADDLE B'''
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(400, 0)
paddle_b.shapesize(stretch_wid = 6, stretch_len = 1)


'''CREATING BALL'''
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
#d means delta or change, this will set the ball speed
#it will be the speed on pixels, e.g: 2 pixels per second
ball.dx = 0.25
ball.dy = 0.25

'''PEN FOR THE SCORE'''
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(f"Player A: 0 Player B: 0", align="center", font=("Courier",24,"normal"))



'''getting paddle a upwards'''
def paddle_a_up():
    #ycor() returns y coordinate
    y = paddle_a.ycor()  
    y += 20    
    #setting the new position for paddle a
    paddle_a.sety(y)

'''getting paddle a downwards'''
def paddle_a_down():
    #ycor() returns y coordinate
    y = paddle_a.ycor()  
    y -= 20    
    #setting the new position for paddle a
    paddle_a.sety(y)

'''getting paddle b upwards'''
def paddle_b_up():
    #ycor() returns y coordinate
    y = paddle_b.ycor()  
    y += 20    
    #setting the new position for paddle a
    paddle_b.sety(y)

'''getting paddle b upwards'''
def paddle_b_down():
    #ycor() returns y coordinate
    y = paddle_b.ycor()  
    y -= 20    
    #setting the new position for paddle a
    paddle_b.sety(y)


'''KEYBOARD BINDING'''
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")



while True:    
    wn.update()

    #MOVE THE BALL
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #checking borders
    if ball.ycor() > 340:
        ball.sety(340)
        #we are reversing the direction
        ball.dy *= -1
    
    if ball.ycor() < -340:
        ball.sety(-340)
        ball.dy *= -1

    if ball.xcor() > 450:
        #we are returning the ball to the center
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier",24,"normal"))
    
    if ball.xcor() < -450:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier",24,"normal"))
    
    #BALL COLITION WITH PADDLES
    if (ball.xcor() > 400 and ball.xcor() < 450) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(400)
        ball.dx *= -1
    if (ball.xcor() < -400 and ball.xcor() > -450) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-400)
        ball.dx *= -1
    


    
    
 