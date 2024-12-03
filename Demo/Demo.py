import sys
import os
import random
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from RainbowColorizer import RC,hue_to_rgb,hex_to_rgb,rgb_to_hex,printr
RC.logo()
hex=rgb_to_hex((random.randint(100, 255),random.randint(100, 255),random.randint(100, 255)))
i = random.randint(1, 365)
r,g,b=hue_to_rgb(i)
r1,g1,b1=hex_to_rgb(hex)
r2,g2,b2=(random.randint(50, 255),random.randint(50, 255),random.randint(50, 255))
text = f"""{RC.color(f"[青色]r[r],[青色]g[r],[青色]b[r]=[黄色]hue_to_rgb([绿色]{i}[黄色])")}
{RC.color(f"[黄]hex_to_rgb(([(199,146,65)]\"{hex}\"[黄色]))")}
{RC.color(f"[黄]rgb_to_hex([绿]{r2}[r],[绿]{g2}[r],[绿]{b2}[r][黄])")}"""
text1 = f""" --> {RC.color(f"[({r},{g},{b})]{hue_to_rgb(i)}")}
 --> {RC.color(f"[({r1},{g1},{b1})]{hex_to_rgb(hex)}")}
 --> {RC.color(f"[({r2},{g2},{b2})]{rgb_to_hex((r2, g2, b2))}")}"""
text = RC.joinH(RC.right(text),text1)
a = RC.border(text,RCdef=RC.colors4,retain=True,title="hue & rgb & hex")
a = f"""{a}
{RC.separator(title="separator",MAX=46,pr=False)}
{RC.separator("*",MAX=23,pr=False)}|{RC.separator("ABC",MAX=23,pr=False)}"""
b = RC.border(f"{RC.colors4(('●'*18+"\n")*9+'●'*18,topLeftColor=(255,0,0),topRightColor=(0,0,255),bottomRightColor=(255,0,0))}",RCdef=RC.colors4,retain=True,title="colors4")
c = RC.border(f"{RC.RainbowColorizer(('●'*18+"\n")*9+'●'*18)}",retain=True,title="RainbowColorizer")
b = RC.joinH(b,c)
a = RC.joinH(a,b)
print(a)