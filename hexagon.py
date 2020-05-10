import turtle as t


t.speed(2)

def draw_hexagon():
    for d in range (6):
        t.forward(100)
        t.left(360/6)
        
for i in range (6):
    draw_hexagon()
    t.forward(100)
    t.right(60)