from vpython import *

# Vectors
r = vector(3,4,5)

# shaftwidth = width of the arrow
# r_arrow =  arrow(pos=vector(0,0,0), axis=r, shaftwidth=0.2)

# Axes
x_axis = arrow(axis=vector(10,0,0), color=color.red, shaftwidth=0.1)
y_axis = arrow(axis=vector(0,10,0), color=color.green, shaftwidth=0.1)
z_axis = arrow(axis=vector(0,0,10), color=color.blue, shaftwidth=0.1)

r_mag = mag(r)
r_hat = norm(r)

r_hat_arrow = arrow(axis=r_hat, color=color.cyan, shaftwidth=0.2)