import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
R=4
t=(-2*np.pi,2*np.pi,0.1)
x=R*(t-np.sin(t))
y=R*(1-np.cos(t))
fig,ax=plt.subplots()
anim_objects,=plt.plot([],[],'o')
xdata,ydata=[],[]
ax.set_xlim(-40,40)
ax.set_ylim(0,10)
def update(frame):
    xdata.append(R*(frame-np.sin(frame)))
    ydata.append(R*(1-np.cos(frame)))
    anim_objects.set_data(xdata,ydata)
ani=FuncAnimation(fig,update,frames=np.arange(-2*np.pi,2*np.pi,0.1),interval=300)
plt.plot(x,y)
ani.save('ani.gif')