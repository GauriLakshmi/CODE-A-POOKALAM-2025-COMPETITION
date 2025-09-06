

import turtle as t
from math import sin, cos, radians

# ---------- tweakables ----------
OUTER_PETALS   = 16    
OUTER_PETAL_R  = 90      
OUTER_RING_R   = 260     
ARC_RING_COUNT = 2       
ARC_RING_RADII = [190, 140]   
ARC_COUNTS     = [24, 18]     
ARC_SMALL_R    = [35, 28]     
INNER_HEX_R    = 85      
SPOKE_LEN      = 24      

OUTER_CIRCLE_R = 320    
# --------------------------------

t.setup(width=900, height=900)
t.bgcolor("white")
t.colormode(255)
t.speed(0)
t.hideturtle()
t.pensize(2)


def jump(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_circle_filled(r, color):
    jump(0, -r)
    t.setheading(0)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()


def draw_outer_petals(petals=OUTER_PETALS, baseR=OUTER_RING_R, cr=OUTER_PETAL_R, color="orange"):
    step = 360 / petals
    t.fillcolor(color)
    for a in range(petals):
        ang = a * step
        t.setheading(ang)
        jump(0, 0)
        t.forward(baseR)
        t.begin_fill()
        t.setheading(ang - 90)
        t.circle(cr, 60)
        t.left(120)
        t.circle(cr, 60)
        t.end_fill()


def draw_arc_ring(centerR, n_arcs, small_r, inward=True, color="yellow"):
    step = 360 / n_arcs
    t.fillcolor(color)
    for i in range(n_arcs):
        a = i * step
        t.setheading(a)
        jump(0, 0)
        t.forward(centerR)
        t.begin_fill()
        if inward:
            t.setheading(a + 90)
            t.circle(small_r, 180)
        else:
            t.setheading(a - 90)
            t.circle(-small_r, 180)
        t.end_fill()


def polygon_points(n, radius):
    pts = []
    for k in range(n):
        ang = radians(90 - 360 * k / n)  
        pts.append((radius * cos(ang), radius * sin(ang)))
    return pts

def draw_inner_star(r=INNER_HEX_R, spoke=SPOKE_LEN, color="lightblue", square_color="orange"):
    pts = polygon_points(6, r)

    
    t.fillcolor(color)
    t.begin_fill()
    jump(*pts[0])
    for i in range(6):
        t.goto(*pts[(i+1) % 6])
    t.end_fill()

    
    for i in range(6):
        p1 = pts[i]
        p2 = pts[(i+1) % 6]
        mx, my = ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)  
        ang = t.towards(p2[0], p2[1])

        jump(mx, my)
        t.setheading(ang + 90)

        t.fillcolor(square_color)
        t.begin_fill()
        t.forward(spoke/2)
        t.right(90)
        t.forward(spoke)
        t.right(90)
        t.forward(spoke)
        t.right(90)
        t.forward(spoke)
        t.right(90)
        t.forward(spoke/2)
        t.end_fill()


draw_circle_filled(OUTER_CIRCLE_R, "orange")  

draw_outer_petals(color="red")

draw_arc_ring(ARC_RING_RADII[0], ARC_COUNTS[0], ARC_SMALL_R[0], inward=True, color="yellow")
draw_arc_ring(ARC_RING_RADII[1], ARC_COUNTS[1], ARC_SMALL_R[1], inward=True, color="green")

draw_inner_star(color="royalblue", square_color="lightblue")

draw_circle_filled(30, "yellow")
t.done()

