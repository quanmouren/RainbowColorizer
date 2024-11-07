import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from RainbowColorizer import RC

RC.separator("/*-+","title")  # 分割线支持任意数量的半角字符 The separator line supports any number of half-width characters
RC.separator("/","标题支持中文")  # 标题支持半角字符和中文 Titles support half-width characters and Chinese characters
RC.separator("ABC")  # 单一分割线 separator line