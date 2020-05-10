import turtle as  t                     # 터틀 그래픽 모듈을 포함한다.
import random
 
def tree(length):
    angle = (random.randint(-20,20))
    if length > 5:                      # lengt가 5보다 크면 순환호출을 한다.
        t.forward(length)               # 거북이가 length 만큼 선을 그린다.
        t.right(20 + angle)             # 오른쪽으로 랜덤한 각도 만큼 회전한다.
        tree(length-15 *(random.random()+0.4))  # 랜덤한 값을 인수로 tree()를 호출한다.
        t.left(40 + (angle * 2))                # 왼쪽으로 랜덤한 각도 만큼 회전한다.
        tree(length-15 *(random.random()+0.4))  # 랜덤한 값을 인수로 tree()를 호출한다.
        t.right(20 + angle)                     # 오른쪽으로 랜덤한 각도 만큼 회전한다.
        t.backward(length)                      # length만큼 뒤로 간다. 제자리로 돌아온다.

t.left(90)
t.color("green")
t.speed(1)
tree(90)
