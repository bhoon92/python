import turtle as t

def drawBar(height):
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(str(height), font=('Times New Roman', 16, 'bold'))
    t.right(90)
    
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()


data = [120, 56, 309, 220, 156, 23, 93]
t.color("blue")
t.fillcolor("pink")
t.pensize(3)

for d in data:
    drawBar(d)