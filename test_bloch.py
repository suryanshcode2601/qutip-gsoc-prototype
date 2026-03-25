import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider
from qutip import Bloch, basis

fig = plt.figure(figsize=(7,7))
plt.subplots_adjust(bottom=0.25, right=0.75)

ax = fig.add_subplot(111, projection='3d')

b = Bloch()
b.fig = fig
b.axes = ax

state = basis(2,0)

def draw_state():
    b.clear()
    b.add_states(state)
    b.render()
    fig.canvas.draw_idle()

draw_state()

# STATE FUNCTIONS

def set_zero(event):
    global state
    state = basis(2,0)
    draw_state()

def set_one(event):
    global state
    state = basis(2,1)
    draw_state()

def set_plus(event):
    global state
    state = (basis(2,0)+basis(2,1)).unit()
    draw_state()

def set_minus(event):
    global state
    state = (basis(2,0)-basis(2,1)).unit()
    draw_state()

# BUTTONS 

ax0 = plt.axes([0.15,0.1,0.1,0.06])
ax1 = plt.axes([0.27,0.1,0.1,0.06])
axp = plt.axes([0.39,0.1,0.1,0.06])
axm = plt.axes([0.51,0.1,0.1,0.06])

b0 = Button(ax0,"|0>")
b1 = Button(ax1,"|1>")
bp = Button(axp,"|+>")
bm = Button(axm,"|->")

b0.on_clicked(set_zero)
b1.on_clicked(set_one)
bp.on_clicked(set_plus)
bm.on_clicked(set_minus)

# SLIDERS 

ax_az = plt.axes([0.80,0.45,0.15,0.03])
ax_el = plt.axes([0.80,0.38,0.15,0.03])

az = Slider(ax_az,"Azimuth",0,360,valinit=45)
el = Slider(ax_el,"Elevation",-90,90,valinit=30)

def rotate(val):
    ax.view_init(el.val, az.val)
    fig.canvas.draw_idle()

az.on_changed(rotate)
el.on_changed(rotate)

plt.show()