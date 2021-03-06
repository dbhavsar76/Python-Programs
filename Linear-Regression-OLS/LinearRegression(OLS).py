from p5 import *

data = []
m = 1
b = 0

def setup():
	size(400,400)
	title('Linear Regression with Ordinary Least Squares')
	ellipse_mode('CENTER')

def mouse_clicked():
    global data
    x = remap(mouse_x, (0, width), (0, 1))
    y = remap(mouse_y, (height, 0), (0, 1))
    point = Vector(x, y)
    data.append(point)
    print(str(x)+', '+str(y), sep = '')

def linearRegression():
    global data, m, b
    xsum = 0
    ysum = 0
    for i in range(len(data)):
        xsum += data[i].x
        ysum += data[i].y

    xmean = xsum / len(data)
    ymean = ysum / len(data)

    num = 0
    den = 0
    for i in range(len(data)):
        num += (data[i].x - xmean) * (data[i].y - ymean)
        den += (data[i].x - xmean) * (data[i].x - xmean)

    m = num / den
    b = ymean - m * xmean

def drawLine():
    global m, b
    x1 = 0
    y1 = m * x1 + b
    x2 = 1
    y2 = m * x2 + b

    x1 = remap(x1, (0, 1), (0, width))
    y1 = remap(y1, (0, 1), (height, 0))
    x2 = remap(x2, (0, 1), (0, width))
    y2 = remap(y2, (0, 1), (height, 0))

    stroke(255)
    line((x1, y1), (x2, y2))

def draw():
    global data
    background(0)
    for i in range(len(data)):
        x = remap(data[i].x, (0, 1), (0, width))
        y = remap(data[i].y, (0, 1), (height, 0))
        stroke(255)
        circle((x, y), 6)
    if len(data) > 1:
        linearRegression()
        drawLine()

run()
