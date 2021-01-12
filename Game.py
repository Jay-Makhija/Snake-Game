import turtle
import time
import random
delay = 0.1
score = 0
high_score = 0
jm = turtle.Screen()
jm.title("The Snake Game by Jay Makhija")
jm.bgcolor("light blue")
jm.setup(width=700, height=700)
jm.tracer(0)
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(-250,-150)
head.direction = "stop"
food= turtle.Turtle()
food.speed(0.5)
food.shape("circle")
food.color("green")
food.penup()
food.goto(0,250)
segments = []
sc = turtle.Turtle()
sc.speed(0)
sc.shape("square")
sc.color("black")
sc.penup()
sc.hideturtle()
sc.goto(0,-260)
sc.write("Current Score: 0 High Score: 0", align = "center", font=("arial", 30, "normal"))
def go_up():
 if head.direction != "down":
    head.direction = "up"
def go_down():
 if head.direction != "up":
    head.direction = "down"
def go_left():
 if head.direction != "right":
    head.direction = "left"
def go_right():
 if head.direction != "left":
    head.direction = "right"
def move():
 if head.direction == "up":
    y = head.ycor()
    head.sety(y+20)
 if head.direction == "down":
    y = head.ycor()
    head.sety(y-20)
 if head.direction == "left":
    x = head.xcor()
    head.setx(x-20)
 if head.direction == "right":
    x = head.xcor()
    head.setx(x+20)
jm.listen()
jm.onkeypress(go_up, "w")
jm.onkeypress(go_down, "s")
jm.onkeypress(go_left, "a")
jm.onkeypress(go_right, "d")
while True:
    jm.update()
    if head.xcor()>320 or head.xcor()<-320 or head.ycor()>320 or head.ycor()<-320:
        time.sleep(1)
        head.goto(-250,-150)
        head.direction = "stop"
        for segment in segments:
            segment.goto(1000,1000) 
        segments.clear()
        score = 0
        delay = 0.1
        sc.clear()
        sc.write("Current Score: {} High Score: {}".format(score, high_score), align="center", font=("arial", 30, "normal"))
    if head.distance(food) <20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("yellow")
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.0001
        score += 1
        if score > high_score:
            high_score = score
        sc.clear()
        sc.write("Current Score: {} High Score: {}".format(score,high_score), align="center", font=("arial", 30, "normal")) 
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    move()
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            score = 0
            delay = 0.1 
            sc.clear()
            sc.write("Current Score: {} High Score: {}".format(score,high_score), align="center", font=("arial", 30, "normal"))
    time.sleep(delay)
jm.mainloop() 
