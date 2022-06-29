import matplotlib.pyplot as plt
import numpy as np
size = 6
speed = 0.01
inner_angle = (size-2)*180/size
outer_angle = 180 - inner_angle
current_angle = 0
pts = [(0, 0)]
plt.axis((-3, 3, -1, 3))
for i in range(size-1):
    angle = np.pi*current_angle/180
    current_angle += outer_angle
    x, y = pts[-1]
    x += np.cos(angle)
    y += np.sin(angle)
    pts.append((x, y))
difference = 1
while difference > speed:
    for i, pt in enumerate(pts):
        x, y = pt
        x_next, y_next = pts[(i+1)%len(pts)]
        x, y = x + (x_next - x)*speed, y + (y_next - y)*speed
        difference = np.sqrt((x_next - x)**2 + (y_next - y)**2)
        pts[i] = (x, y)
        plt.scatter(x, y, s=0.5)
plt.show()
