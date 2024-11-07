import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from RainbowColorizer import RC

a = """The gentle breeze, like a melody of the ages,
whisks away the worries and cares of the world,
leaving only the essence of pure bliss and tranquility."""
print(RC.RainbowColorizer(RC.right(a)))  # 文本右对齐