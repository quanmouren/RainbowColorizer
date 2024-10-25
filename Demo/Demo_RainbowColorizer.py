from RainbowColorizer import hue_to_rgb,RC
import time

logo = r"""  _____       _       _                      _____      _            _              
 |  __ \     (_)     | |                    / ____|    | |          (_)             
 | |__) |__ _ _ _ __ | |__   _____      __ | |     ___ | | ___  _ __ _ _______ _ __ 
 |  _  // _` | | '_ \| '_ \ / _ \ \ /\ / / | |    / _ \| |/ _ \| '__| |_  / _ | '__|
 | | \ | (_| | | | | | |_) | (_) \ V  V /  | |___| (_) | | (_) | |  | |/ |  __| |   
 |_|  \_\__,_|_|_| |_|_.__/ \___/ \_/\_/    \_____\___/|_|\___/|_|  |_/___\___|_|"""
print(RC.RainbowColorizer("Welcome to Rainbow Colorizer"))
print(RC.RainbowColorizer(logo))
print(RC.RainbowColorizer("Easier custom transition colors",(14,190,255),(255,66,179)))  # 更简单的自定义过度颜色
print("\x1b[A\x1b[A\x1b[A\r\x1b[A\x1b[A\x1b[A\x1b[A\x1b[A\r\x1b[?25l")
for i in range(0, 360, 5):
    r,g,b = hue_to_rgb(i)
    r1,g1,b1 = hue_to_rgb(i+80)
    print(RC.RainbowColorizer(logo,(r,g,b),(r1,g1,b1)),end='\x1b[A\x1b[A\x1b[A\x1b[A\x1b[A\r\x1b[?25l')
    time.sleep(0.05)
print("\n\n\n\n\n\n\n\x1b[?25h")