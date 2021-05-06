from vpython import *

# Generate ball
ball = sphere(radius=0.2)

# Initial setting
ball.pos = vec(-2,0,0) ## m
ball.v = vec(0.8,0,0) ## m/s
t = 0 ## s
dt = 1 ## s (delta time)

a = box(pos = vec(-3,0,0),size = vec(1,0.5,0.5), color = color.yellow)

# Attach arrow to the ball
attach_arrow(ball, "v", shaftwidth=0.1, color=color.green)
 
t = 0
dt = 0.01   

ball.v = vec(0.9,0.2,0)
a.v = vec(1,0,0)
while t < 4:
    rate(1/dt)
    ball.pos = ball.pos + ball.v * dt 
    a.pos = a.pos + a.v * dt


    t += dt 
