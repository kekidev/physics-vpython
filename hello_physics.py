from numpy import square
from vpython import *

# Radius - 반지름
myBall = sphere(color=color.red, radius=2)

myBox = box(pos=vec(5,0,0), color = color.blue, size=vec(0.5,4,1))

myBall.color = color.green
myBox.pos.x = 10
