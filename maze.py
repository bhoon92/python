import turtle as t 
import random


# (x,y) 위치에 미로 그리기
def mazePath(x,y):
    for i in range(2):
        t.penup()
        if i == 1:
            t.goto(x+100, y+100)
        else :
            t.goto(x,y)

        t.pendown()
        t.forward(300)
        t.right(90)
        t.forward(300)
        t.left(90)
        t.forward(300)

# 거북이를 왼쪽으로 회전하여 10만큼 전진
def turn_left():
    t.left(10)
    t.forward(10)

# 거북이를 오른쪽으로 회전하여 10만큼 전진
def turn_right():
    t.right(10)
    t.forward(10)


screen = t.Screen()
t.shape("turtle")
t.speed(5)

mazePath(-300, 200)
screen.onkey(turn_left, "Left")  #왼쪽 방향키
screen.onkey(turn_right, "Right")  #오른쪽 방향키

t.penup()
t.goto(-300, 250)
t.speed(1)
t.pendown()
screen.listen()
screen.mainloop()