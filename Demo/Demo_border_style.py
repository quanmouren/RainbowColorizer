import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from RainbowColorizer import RC

print(RC.border("hView all border styles", "help",title="style"))
print(RC.border("•ิ.•ั", ["♠","♥","♣","♦","○","|"]))