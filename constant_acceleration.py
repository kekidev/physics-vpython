from vpython import *

ball = sphere(radius=0.2)

ball.pos = vec(-2,0,0) ## m
ball.v = vec(0,0,0) ## m/s
ball.a = vec(0.35,0,0)
t = 0 ## s
dt = 0.01 ## s (delta time)

attach_arrow(ball, "v", shaftwidth=0.1, color=color.green)
attach_arrow(ball, "a", shaftwidth=0.05, color=color.red)
attach_trail(ball, type="points",pps=5)

# ball.v = vec(0.9,0.2,0)
while t < 4:
    rate(1/dt)
    ball.v = ball.v + ball.a * dt 
    ball.pos = ball.pos + ball.v * dt 
    
    t += dt 
