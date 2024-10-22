import shutil
import re
def hue_to_rgb(hue, saturation=1, value=1):
    if saturation == 0:
        return int(value * 255), int(value * 255), int(value * 255)
    hue /= 60
    hue %= 6
    i = int(hue)
    f = hue - i
    p = value * (1 - saturation)
    q = value * (1 - saturation * f)
    t = value * (1 - saturation * (1 - f))
    if i == 0:r, g, b = value, t, p
    elif i == 1:r, g, b = q, value, p
    elif i == 2:r, g, b = p, value, t
    elif i == 3:r, g, b = p, q, value
    elif i == 4:r, g, b = t, p, value
    else:r, g, b = value, p, q
    return int(r * 255), int(g * 255), int(b * 255)

def interpolateColors(color1, color2, t):
    # Linear interpolation between two RGB colors
    r = int(color1[0] + (color2[0] - color1[0]) * t)
    g = int(color1[1] + (color2[1] - color1[1]) * t)
    b = int(color1[2] + (color2[2] - color1[2]) * t)
    return r,g,b

class RC():
    def RainbowColorizer(text, start_color=(255, 255, 0), end_color=(0, 255, 255)):
        lines = text.split('\n')
        num_lines = len(lines)
        max_length = max(len(line) for line in lines)
        result = ""
        for line_index, line in enumerate(lines):
            for char_index, char in enumerate(line.ljust(max_length)):
                diagonal_pos = line_index + char_index
                if max_length < 5: max_length = 5
                t = diagonal_pos / (num_lines + max_length - 2)
                r,g,b = interpolateColors(start_color,end_color,t)
                result += f"\033[38;2;{r};{g};{b}m{char}"
            result += "\033[0m\n"
        return result.rstrip('\n')
    
    def colors4(text, topLeftColor=(0, 255, 255), topRightColor=(64, 0, 255), bottomLeftColor=(128, 0, 255), bottomRightColor=(192, 0, 255)):
        lines = text.split('\n')
        num_lines = len(lines)
        max_length = max(len(line) for line in lines)
        result = ""
        for line_index, line in enumerate(lines):
            for char_index, char in enumerate(line.ljust(max_length)):
                norm_line_index = line_index / (num_lines - 1) if num_lines > 1 else 0
                norm_char_index = char_index / (max_length - 1) if max_length > 1 else 0
                top_color = interpolateColors(topLeftColor, topRightColor, norm_char_index)
                bottom_color = interpolateColors(bottomLeftColor, bottomRightColor, norm_char_index)
                final_color = interpolateColors(top_color, bottom_color, norm_line_index)
                result += f"\033[38;2;{final_color[0]};{final_color[1]};{final_color[2]}m{char}"
            result += "\033[0m\n"
        return result.rstrip('\n')

    def separator(filler="-", title=""):
        size = shutil.get_terminal_size()
        if title == "":
            a = (filler * (size.columns-1))[:(size.columns-1)]
        else:
            count = 0
            for char in title:
                if '\u4e00' <= char <= '\u9fff':count += 1
            a = (filler * 4)[:4] + f" {title} " + (filler * (size.columns - len(title) - 7))[:(size.columns - len(title) - 7 - count)]
        for index, char in enumerate(a):
            hue = int(360 * (index / size.columns))
            rgb = hue_to_rgb(hue)
            print(RC.RainbowColorizer(char, rgb, rgb), end='')
        print("")

    def color(text, endcolor="\033[0m"):
        text = text.replace("[r]", endcolor)
        def replacer(text, colornames, colorcode):
            for colorname in colornames:
                text = text.replace(f"[{colorname}]", colorcode)
            return text
        text = replacer(text, ["红色","红","red","rd"], "\033[31m")
        text = replacer(text, ["绿色","绿","green","gn"], "\033[32m")
        text = replacer(text, ["黄色","黄","yellow","ye"], "\033[33m")
        text = replacer(text, ["蓝色","蓝","blue","bu"], "\033[34m")
        text = replacer(text, ["紫色","紫","violet","vt"], "\033[35m")
        text = replacer(text, ["青色","青","cyan","cn"], "\033[36m")
        text = replacer(text, ["白色","白","white","wh"], "\033[37m")
        text = replacer(text, ["黑色","黑","black","bk"], "\033[30m")
        text = replacer(text, ["亮红色","亮红","bred","brd"], "\033[91m")
        text = replacer(text, ["亮绿色","亮绿","bgreen","bgn"], "\033[92m")
        text = replacer(text, ["亮黄色","亮黄","byellow","bye"], "\033[93m")
        text = replacer(text, ["亮蓝色","亮蓝","bblue","bbu"], "\033[94m")
        text = replacer(text, ["亮紫色","亮紫","bviolet","bvt"], "\033[95m")
        text = replacer(text, ["亮青色","亮青","bcyan","bcn"], "\033[96m")
        text = replacer(text, ["亮白色","亮白","bwhite","bwh"], "\033[97m")
        text = replacer(text, ["亮黑色","亮黑","bblack","bbk"], "\033[90m")
        text = replacer(text, ["背景红","背景红色","bgred","bgrd"], "\033[41m")
        text = replacer(text, ["背景绿","背景绿色","bggreen","bggn"], "\033[42m")
        text = replacer(text, ["背景黄","背景黄色","bgyellow","bgye"], "\033[43m")
        text = replacer(text, ["背景蓝","背景蓝色","bgblue","bgbu"], "\033[44m")
        text = replacer(text, ["背景紫","背景紫色","bgviolet","bgvt"], "\033[45m")
        text = replacer(text, ["背景青","背景青色","bgcyan","bgcn"], "\033[46m")
        text = replacer(text, ["背景白","背景白色","bgwhite","bgwh"], "\033[47m")
        text = replacer(text, ["背景黑","背景黑色","bgblack","bgbk"], "\033[40m")
        pattern = r"\[\((\d+),(\d+),(\d+)\)\]"
        matches = re.findall(pattern, text)
        for match in matches:
            r, g, b = map(int, match)
            text = text.replace(f"[({r},{g},{b})]", f"\033[38;2;{r};{g};{b}m")
        return text + "\033[0m"
    


if __name__ == "__main__":
    logo = r"""  _____       _       _                      _____      _            _              
 |  __ \     (_)     | |                    / ____|    | |          (_)             
 | |__) |__ _ _ _ __ | |__   _____      __ | |     ___ | | ___  _ __ _ _______ _ __ 
 |  _  // _` | | '_ \| '_ \ / _ \ \ /\ / / | |    / _ \| |/ _ \| '__| |_  / _ | '__|
 | | \ | (_| | | | | | |_) | (_) \ V  V /  | |___| (_) | | (_) | |  | |/ |  __| |   
 |_|  \_\__,_|_|_| |_|_.__/ \___/ \_/\_/    \_____\___/|_|\___/|_|  |_/___\___|_|"""
    print(RC.RainbowColorizer(logo))
    print(RC.RainbowColorizer("Welcome to Rainbow Colorizer"))
    RC.separator("/","title")
    print(RC.RainbowColorizer("Use ") + "\033[31m[red]ANSI\033[0m" + RC.RainbowColorizer(" escape sequences more easily"))
    text = """######\n######\n######"""
    print(RC.colors4(text))