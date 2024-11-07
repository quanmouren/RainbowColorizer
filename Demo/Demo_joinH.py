import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from RainbowColorizer import RC

a = """AAAAAAAAAA
AAAAAAAA
AAAAAA
AAAAA
AAAAA
AAAAAA
AAAAAAAA
AAAAAAAAAAA"""
b = """BBBBBBBBBB
BBBBBBBB
BBBBBBB
BBBBBBB
BBBBBBB
BBBBBBBB
BBBBBBBBB
BBBBBBBBBBB"""
print(RC.joinH(a, b))