import matplotlib.pyplot as plt
import numpy as np
from random import randint
size = 6
speed = 0.01
inner_angle = (size-2)*180/size
outer_angle = 180 - inner_angle
current_angle = 0
pts = [(0, 0)]
def get_color(): return '#%06X' % randint(0, 0xFFFFFF)
colors = [get_color()]
for i in range(size-1):
    angle = np.pi*current_angle/180
    current_angle += outer_angle
    x, y = pts[-1]
    x += np.cos(angle)
    y += np.sin(angle)
    pts.append((x, y))
    colors.append(get_color())
    plt.plot([pts[-2][0], pts[-1][0]], [pts[-2][1], pts[-1][1]], linewidth=0.3, color='black')
plt.plot([pts[-1][0], pts[0][0]], [pts[-1][1], pts[-0][1]], linewidth=0.3, color='black')
difference = 1
while difference > speed:
    for i, pt in enumerate(pts):
        x, y = pt
        x_next, y_next = pts[(i+1)%len(pts)]
        x, y = x + (x_next - x)*speed, y + (y_next - y)*speed
        difference = np.sqrt((x_next - x)**2 + (y_next - y)**2)
        pts[i] = (x, y)
        plt.scatter(x, y, s=0.5, color=colors[i])
plt.show()
