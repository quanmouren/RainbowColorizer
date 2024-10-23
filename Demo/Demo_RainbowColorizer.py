from RainbowColorizer import hue_to_rgb,RC
import time

logo = r"""  _____       _       _                      _____      _            _              
 |  __ \     (_)     | |                    / ____|    | |          (_)             
 | |__) |__ _ _ _ __ | |__   _____      __ | |     ___ | | ___  _ __ _ _______ _ __ 
 |  _  // _` | | '_ \| '_ \ / _ \ \ /\ / / | |    / _ \| |/ _ \| '__| |_  / _ | '__|
 | | \ | (_| | | | | | |_) | (_) \ V  V /  | |___| (_) | | (_) | |  | |/ |  __| |   
 |_|  \_\__,_|_|_| |_|_.__/ \___/ \_/\_/    \_____\___/|_|\___/|_|  |_/___\___|_|"""
print(RC.RainbowColorizer(logo))
print(RC.RainbowColorizer("Welcome to Rainbow Colorizer"))
print(RC.RainbowColorizer("Easier custom transition colors",(14,190,255),(255,66,179)))  # 更简单的自定义过度颜色
for i in range(3601):
    r,g,b = hue_to_rgb(i)
    r1,g1,b1 = hue_to_rgb(i+80)
    print(RC.RainbowColorizer("Rainbow Colorizer",(r,g,b),(r1,g1,b1)),end='\r')

    time.sleep(0.01)
print()