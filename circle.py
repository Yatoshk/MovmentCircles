import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
R = 10
r = 3
x0 = 0
#t = 0


theta = np.linspace( 0 , 2 * np.pi , 360 )
fhi1 = np.linspace( np.pi/2 , 3*np.pi/2, 180 )

fhi2 = np.linspace( 3*np.pi/2 , np.pi/2, 180 )

fhi = []
fhi.extend(fhi1[x0:])
fhi.extend(fhi2[:len(fhi2)-x0])



A = R * np.cos( theta )
B = R * np.sin( theta )

Xc = (R - r)*np.sin(fhi) 
Yc = (R - r)*np.cos(fhi) 

a0 = r * np.cos( theta ) + Xc[0]
b0 = r * np.sin( theta ) + Yc[0]


fig, ax = plt.subplots(1)
ax.set_xlim([-R, R])
ax.set_ylim([-R, R])
ax.plot( A, B )
ax.plot( Xc, Yc )
line, = ax.plot(a0, b0)

def animate(i):
    line.set_xdata(r * np.cos( theta ) + Xc[i])
    line.set_ydata(r * np.sin( theta ) + Yc[i])  # update the data.
    return line,

ani = animation.FuncAnimation(
    fig, animate, interval=10, blit=True, save_count=len(fhi), repeat=True)
#ani.save('D:\\scatter.gif', writer='imagemagick', fps=30)
plt.show()


