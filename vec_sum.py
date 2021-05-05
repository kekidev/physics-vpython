from vpython import *

a = vector(3,4,0)
b = vector(5,1,0)

a_arrow = arrow(pos=vector(0,0,0), axis=a, shaftwidth=0.2, color=color.blue)
b_arrow = arrow(pos=vector(0,0,0), axis=b, shaftwidth=0.2, color=color.green)

c = a + b
c_arrow = arrow(pos=vector(0,0,0), axis=c, shaftwidth=0.2, color=color.red)