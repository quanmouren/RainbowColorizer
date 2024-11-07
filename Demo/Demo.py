import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from RainbowColorizer import hue_to_rgb,RC

logo = r"""  _____       _       _                      _____      _            _              
|  __ \     (_)     | |                    / ____|    | |          (_)             
| |__) |__ _ _ _ __ | |__   _____      __ | |     ___ | | ___  _ __ _ _______ _ __ 
|  _  // _` | | '_ \| '_ \ / _ \ \ /\ / / | |    / _ \| |/ _ \| '__| |_  / _ | '__|
| | \ | (_| | | | | | |_) | (_) \ V  V /  | |___| (_) | | (_) | |  | |/ |  __| |   
|_|  \_\__,_|_|_| |_|_.__/ \___/ \_/\_/    \_____\___/|_|\___/|_|  |_/___\___|_|"""
print(RC.RainbowColorizer(logo))
print(RC.RainbowColorizer("Welcome to Rainbow Colorizer"))
RC.separator("/","Better looking dividing lines")
print(RC.RainbowColorizer("Use ") + "\033[31m[red]ANSI\033[0m" + RC.RainbowColorizer(" escape sequences more easily"))
text = """##################\nCooler  four-color \ngradient rendering 
function\n##################"""
print(RC.colors4(text))
print(RC.color("[bg(255,192,203)][red]Simpler background color dyeing[r]"))