from RainbowColorizer import RC

a = """标题\n------\nAAAAAA\nAAAAAA"""
b = """ 标题\n ------\n BBBBBB\n BBBBBB"""

ya = RC.border(RC.joinH(a, b))
yb= RC.border(RC.joinH(a, b))
yc = RC.border(RC.joinH(ya, yb))
print(RC.border(RC.joinH(yc, yc)))