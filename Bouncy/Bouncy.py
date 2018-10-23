from p5 import *

class Ball:

    def __init__(self):
        self.pos = Vector(random_uniform(width), random_uniform(height))
        self.vel = Vector(random_uniform(-3, 3), random_uniform(-3, 3))
        #self.acc = Vector(0, 2)
        self.rad = floor(random_uniform(10, 50))
        self.col = Color(random_uniform(255), 255, 225)
        self.m = self.rad * 0.1

    def update(self):
        # if self.vel.y < -40:
        #     self.acc.y += 0.3
        # else:
        #     self.acc.y = 2
        # self.acc.x = remap(self.pos.x, (0, width), (1, -1))    
        # self.vel += self.acc
        self.pos += self.vel

    def checkBoundaryCollision(self):
        if self.pos.y + self.rad > height:
            self.pos.y = height - self.rad
            self.vel.y *= -1
        elif self.pos.y - self.rad < 0:
            self.pos.y = self.rad
            self.vel.y *= -1
        elif self.pos.x + self.rad > width:
            self.pos.x = width - self.rad
            self.vel.x *= -1
        elif self.pos.x - self.rad < 0:
            self.pos.x = self.rad
            self.vel.x *= -1

    def checkCollision(self, other):
        distVect = other.pos - self.pos
        distMag = distVect.magnitude
        minDist = self.rad + other.rad

        if distMag < minDist:
            distCorrection = (minDist - distMag)/2
            d = distVect.copy()
            d.normalize()
            correctionVect = d * distCorrection
            other.pos += correctionVect
            self.pos -= correctionVect

            theta = distVect.angle
            sine = sin(theta)
            cosine = cos(theta)

            bT1 = Vector(0,0)
            bT2 = Vector(1,1)
            bTemp = [bT1, bT2]
            bTemp[1].x  = cosine * distVect.x + sine * distVect.y
            bTemp[1].y  = cosine * distVect.y - sine * distVect.x

            vT1 = Vector(0.15,0.15)
            vT2 = Vector(0.1,1.1)
            vTemp = [vT1, vT2]
            vTemp[0].x = cosine * self.vel.x + sine * self.vel.y
            vTemp[0].y = cosine * self.vel.y - sine * self.vel.x
            vTemp[1].x = cosine * other.vel.x + sine * other.vel.y
            vTemp[1].y = cosine * other.vel.y - sine * other.vel.x

            vF1 = Vector(0.25,1.25)
            vF2 = Vector(0.2,1.2)
            vFinal = [vF1, vF2]
            vFinal[0].x = ((self.m - other.m) * vTemp[0].x + 2 * other.m * vTemp[1].x) / (self.m + other.m)
            vFinal[0].y = vTemp[0].y
            vFinal[1].x = ((other.m - self.m) * vTemp[1].x + 2 * self.m * vTemp[0].x) / (self.m + other.m)
            vFinal[1].y = vTemp[1].y

            bTemp[0].x += vFinal[0].x
            bTemp[1].x += vFinal[1].x

            bF1 = Vector(0.3, 1.3)
            bF2 = Vector(0.4, 1.4)
            bFinal = [bF1, bF2]
            bFinal[0].x = cosine * bTemp[0].x - sine * bTemp[0].y
            bFinal[0].y = cosine * bTemp[0].y + sine * bTemp[0].x
            bFinal[1].x = cosine * bTemp[1].x - sine * bTemp[1].y
            bFinal[1].y = cosine * bTemp[1].y + sine * bTemp[1].x

            other.pos.x = self.pos.x + bFinal[1].x
            other.pos.y = self.pos.y + bFinal[1].y
            self.pos += bFinal[0]

            self.vel.x = cosine * vFinal[0].x - sine * vFinal[0].y;
            self.vel.y = cosine * vFinal[0].y + sine * vFinal[0].x;
            other.vel.x = cosine * vFinal[1].x - sine * vFinal[1].y;
            other.vel.y = cosine * vFinal[1].y + sine * vFinal[1].x

    def render(self):
        fill(self.col)
        stroke(self.col)
        circle((self.pos.x, self.pos.y), self.rad*2)

balls =[]

def setup():
    size(640, 360)
    title('Bouncy')
    color_mode('HSB')
    ellipse_mode('CENTER')
    no_stroke()
    for i in range(8):
        balls.append(Ball())

def draw():
    background(0)
    for i in range(len(balls)):
        balls[i].update()
        balls[i].render()
        balls[i].checkBoundaryCollision()
        for j in range(len(balls)):
            if i is not j:
                balls[i].checkCollision(balls[j])
               
    #print(frame_rate)

run()
