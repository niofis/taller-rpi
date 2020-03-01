from brachiograph import BrachioGraph
import math

# Uncomment the definition you want to use.

# This is an example BrachioGraph definition. If you build a plotter as
# described in the "Get started" section of the documentation, this definition
# is likely to work well. However, you should work out your own servo
# angle/pulse-width values as described in "Improve the plotter calibration".


# angles in degrees and corresponding pulse-widths for the two arm servos

servo_1_angle_pws1 = [
    [-162, 2470],
    [-144, 2250],
    [-126, 2050],
    [-108, 1860],
    [ -90, 1690],
    [ -72, 1530],
    [ -54, 1350],
    [ -36, 1190],
    [ -18, 1010],
    [   0,  840],
    [  18,  640],
]

servo_2_angle_pws2 = [
    [  0,  660],
    [ 18,  840],
    [ 36, 1030],
    [ 54, 1180],
    [ 72, 1340],
    [ 90, 1490],
    [108, 1640],
    [126, 1830],
    [144, 2000],
    [162, 2200],
    [180, 2410],
]

bounds = (1, 4, 10, 13)

bg = BrachioGraph(
    # the lengths of the arms
    inner_arm=8,
    outer_arm=9,
    # the drawing area
    #bounds=(-8, 4, 10, 13),
    bounds=bounds,
    #bounds=(-5,0, 10, 10),
    # angles in degrees and corresponding pulse-widths for the two arm servos
    #servo_1_angle_pws=servo_1_angle_pws1,
    #servo_2_angle_pws=servo_2_angle_pws2,
    # pulse-widths for pen up/down
    pw_down=1800,
    pw_up=900,
    servo_1_centre=1460,
    servo_2_centre=1530,
    hysteresis_correction_1=5,
    hysteresis_correction_2=-25
)

#bg.box()
#bg.test_pattern()
#bg.plot_file("./images/africa.json")
#bg.plot_file("./images/kirby-solid.json")
#bg.plot_file("./images/gumball.json")
#bg.plot_file("./images/dog.json")
#bg.plot_file("./images/letter_a.json")
#bg.grid_lines(interpolate=400, both=True)
#bg.draw_line(start=(1,4), end=(10,13))

def rst(x, y):
    minx, miny, maxx, maxy = bounds
    w = maxx - minx
    h = maxy - miny
    return (minx + x * w, miny + y * h)

def line(x1,y1,x2,y2):
    xx = x2-x1
    yy = y2-y1
    dist = math.sqrt(xx * xx + yy * yy)
    steps = math.ceil(dist * 150);
    #start = rst(x1, y1)
    #end = rst(x2, y2)
    #bg.draw_line(start=start, end=end)
    #return 0

    dx = xx / steps
    dy = yy / steps

    xy(x1,y1, False)

    for i in range(0,steps):
        x1 = x1 + dx
        y1 = y1 + dy
        xy(x1, y1,True)

    xy(x1, y1, False)

def xy(x,y,draw):
    xp, yp = rst(x, y)
    bg.xy(xp,yp,draw=draw, interpolate=1)

def circle(x, y, radius, segments=360):
    u = radius
    v = 0
    step = math.pi * 2 / segments
    rads = step
    xy(u+x, v+y, False)
    for i in range(0, segments):
        up = u * math.cos(rads) - v * math.sin(rads)
        vp = v * math.cos(rads) + u * math.sin(rads)
        xy(u+x, v+y, True)
        xy(up+x, vp+y, True)
        u = up
        v = vp
    xy(u+x,v+y,False)


def smiley():
    circle(0.5,0.5,0.5)
    circle(0.25,0.25,0.1, segments=25)
    circle(0.75,0.25,0.1, segments=25)
    line(0.25,0.75,0.75,0.75)

def labyrinth():
    step = 0.1
    curr = step
    while curr <= 0.5:
        circle(0.5, 0.5, curr, segments=4)
        curr = curr + step

def tictactoe():
    line(0.33,0.0,0.33,1.0)
    line(0.66,0.0,0.66,1.0)
    line(0.0,0.33,1.0,0.33)
    line(0.0,0.66,1.0,0.66)

def home():
    bg.park()

#labyrinth()
#line(0,0,1,1)
#line(0,1,1,0)
#smiley()
#bg.park()


# A "naively" calibrated plotter definition. We assume the default 10ms
# pulse-width difference = 1 degree of motor movement. If the arms appear to
# move in the wrong directions, try reversing the value of servo_1_degree_ms
# and/or servo_2_degree_ms.

# naive_bg = BrachioGraph(
#     # the lengths of the arms
#     inner_arm=8,
#     outer_arm=8,
#     # the drawing area
#     bounds=(-6, 4, 6, 12),
#     # relationship between servo angles and pulse-widths
#     servo_1_degree_ms=-10,
#     servo_2_degree_ms=10,
#     # pulse-widths for pen up/down
#     pw_down=1200,
#     pw_up=1850,
# )
