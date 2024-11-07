import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from RainbowColorizer import hex_to_rgb,rgb_to_hex,RC

r,g,b = hex_to_rgb("#002FA7")
print(RC.color(f"#002FA7 --> [({r},{g},{b})]Klein Blue({r},{g},{b})"))
print(rgb_to_hex((255, 255, 0)))