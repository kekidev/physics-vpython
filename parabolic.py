from vpython import *

ball = sphere(radius=0.2)
ground = box(pos=vec(0,-4,0), size=vec(15,0.01,5))

ball.pos = vec(-2,0,0) 
ball.v = vec(1,1,0)  
ball.a = vec(0,-0.5,0)

t = 0 
dt = 0.01   
 
attach_arrow(ball, "v", shaftwidth=0.1, color=color.green)
attach_arrow(ball, "a", shaftwidth=0.05, color=color.red)
attach_trail(ball, type="points",pps=5)
 
while ball.pos.y > ground.pos.y: 
    rate(1/dt)
    ball.v = ball.v + ball.a * dt 
    ball.pos = ball.pos + ball.v * dt 
    t = t + dt 

motion_graph = graph(title="position time",xtitle="t",ytitle="y")
g_bally = gcurve()


