import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from RainbowColorizer import printr

print = printr()
print("RainbowColorizer", 1234567890,1==1,1==3,None,"C:\\Users\\user\\Desktop", {1:1,2:2},(0,20,40,60,80),[1,1,1,1])

print.TrueColor = "[(0,191,255)]"
print.FalseColor = "[brd]"
print.NoneColor = "[(221,160,221)]"
print.pathColor = [(255, 255, 0), (255, 255, 80)]
print.dictColor = [(255, 102, 0), (255, 178, 0)]
print.tupleColor = [(0, 0, 255), (0, 191, 255)]
print.listColor = [(255, 235, 59), (124, 252, 0)]
print.intColor = [(255, 0, 0), (218, 112, 214)]
print.infoColor = [(0, 255, 0), (0, 255, 0)]
print("RainbowColorizer", 1234567890,1==1,1==3,None,"C:\\Users\\user\\Desktop", {1:1,2:2},(0,20,40,60,80),[1,1,1,1])

print.on_bool = False
print.on_None = False
print.on_path = False
print.on_dict = False
print.on_tuple = False
print.on_list = False
print.on_int = False
print.on_info = False
print("RainbowColorizer", 1234567890,1==1,1==3,None,"C:\\Users\\user\\Desktop", {1:1,2:2},(0,20,40,60,80),[1,1,1,1])

print = printr("title")
print.style_1()
print("RainbowColorizer", 1234567890,1==1,1==3,None,"C:\\Users\\user\\Desktop", {1:1,2:2},(0,20,40,60,80),[1,1,1,1])