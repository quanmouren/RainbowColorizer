from RainbowColorizer import hue_to_rgb,RC
import time

for i in range(3601):
    r,g,b = hue_to_rgb(i)
    print(f"{RC.color(f'[({r},{g},{b})]hue:{i},rgb:({r}, {g}, {b})[r]   ')}",end='\r')
    time.sleep(0.01)
print()