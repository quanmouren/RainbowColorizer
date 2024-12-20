import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from RainbowColorizer import RC

print(RC.color("使用[]快速调用颜色"))
print(RC.color("[violet]前景色"))
print(RC.color("[blue]蓝色[red]红色[r]清除颜色"))
print(RC.color("使用[b]快速调用亮色"))
print(RC.color("[bgreen]亮绿色 [green]绿色"))
print(RC.color("使用[bg]快速调用背景色"))
print(RC.color("[bgred]红色[bgblue]蓝色"))
print("使用[(0,0,0)]自定义颜色")
print(RC.color("[(255,192,203)]粉色"))
print("使用[bg(0,0,0)]自定义背景色颜色")
print(RC.color("[bg(255,192,203)]粉色"))
print("混合使用多种颜色")
print(RC.color("[bg(255,192,203)][red]混合使用前景和背景色[r]"))