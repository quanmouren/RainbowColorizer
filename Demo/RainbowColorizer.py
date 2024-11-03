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

def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    rgb = tuple(int(hex_code[i:i+2], 16) for i in (0, 2 ,4))
    return rgb

def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

def interpolateColors(color1, color2, t):
    r = int(color1[0] + (color2[0] - color1[0]) * t)
    g = int(color1[1] + (color2[1] - color1[1]) * t)
    b = int(color1[2] + (color2[2] - color1[2]) * t)
    return r,g,b

def statisticsHWC(text):
    count = 0
    for char in text:
        if '\u4e00' <= char <= '\u9fff' or '\u3000' <= char <= '\u303F':
            count += 1
    return count

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
            count = statisticsHWC(title)
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
        pattern = r'\[bg\((\d+),(\d+),(\d+)\)\]'
        matches = re.findall(pattern, text)
        for match in matches:
            r, g, b = map(int, match)
            text = text.replace(f"[bg({r},{g},{b})]", f"\033[48;2;{r};{g};{b}m")
        return text + "\033[0m"
    
    def border(text, filler=["┌", "┐", "└", "┘", "─", "│"], RCdef=RainbowColorizer,**kwargs):
        """
        bug:在计算颜色时忽略了全角字符长度问题,导致染色错位
        """
        lines = text.split("\n")
        if not isinstance(filler, list):
            if filler == "help" or filler == "?":
                for i in range(1,7):
                    _help = f"mode:{i}"
                    print(RC.border(_help,i))
                filler = ["┌", "┐", "└", "┘", "─", "│"]
            elif filler == 1:filler = ["┌", "┐", "└", "┘", "─", "│"]
            elif filler == 2:filler = ["╔", "╗", "╚", "╝", "═", "║"]
            elif filler == 3:filler = ["┏", "┓", "┗", "┛", "━", "┃"]
            elif filler == 4:filler = ["╭", "╮", "╰", "╯", "─", "│"]
            elif filler == 5:filler = ["┍", "┑", "┕", "┙", "━", "│"]
            elif filler == 6:filler = ["┎", "┒", "┖", "┚", "─", "┃"]
            else:filler = [filler, filler, filler, filler, filler, filler]
        max_width = max(len(line)+statisticsHWC(line) for line in lines)
        if kwargs.get("title"):
            a = f"{filler[0]}{kwargs.get("title")}{filler[4] * (max_width-((statisticsHWC(kwargs.get("title")))+len(kwargs.get("title"))))}{filler[1]}"
        else:
            a = f"{filler[0]}{filler[4] * (max_width)}{filler[1]}"
        for line in lines:
            a += f"\n{filler[5]}{line}{(max_width-(len(line)+statisticsHWC(line)))*" "}{filler[5]}"
        a += f"\n{filler[2]}{filler[4] * (max_width)}{filler[3]}"
        if RCdef == RC.RainbowColorizer:
            if kwargs.get("color1") and kwargs.get("color2"):
                return RCdef(a,kwargs.get("color1"),kwargs.get("color2"))
            else:
                return RCdef(a)
        elif RCdef == RC.colors4:
            if kwargs.get("color1") and kwargs.get("color2") and kwargs.get("color3") and kwargs.get("color4"):
                return RCdef(a,kwargs.get("color1"),kwargs.get("color2"),kwargs.get("color3"),kwargs.get("color4"))
            else:
                return RCdef(a)
        else:
            return RC.RainbowColorizer(a)
        
    def r(text):
        return re.sub(r'\033\[[\d;]*m', '', text)
    
    def right(text):
        lines = text.split("\n")
        max_width = max(len(line) + statisticsHWC(line) for line in lines)
        a_lines = []
        for line in lines:
            a_lines.append(f"{(max_width - (len(line) + statisticsHWC(line))) * ' '}{line}")
        return '\n'.join(a_lines)

    def joinH(text1, text2):
        text1 = RC.r(text1)
        text2 = RC.r(text2)
        lines1 = text1.split('\n')
        lines2 = text2.split('\n')
        max_height = max(len(lines1), len(lines2))
        def buQiHang(lines, max_width):
            a_lines = []
            for line in lines:
                line_width = len(line) + statisticsHWC(line)
                padding = ' ' * (max_width - line_width)
                a_lines.append(line + padding)
            return a_lines
        max_width1 = max(len(line) + statisticsHWC(line) for line in lines1)
        max_width2 = max(len(line) + statisticsHWC(line) for line in lines2)
        max_width = max(max_width1, max_width2)
        aligned_lines1 = buQiHang(lines1, max_width)
        aligned_lines2 = buQiHang(lines2, max_width)
        if len(aligned_lines1) < max_height:
            aligned_lines1.extend([' ' * max_width] * (max_height - len(aligned_lines1)))
        if len(aligned_lines2) < max_height:
            aligned_lines2.extend([' ' * max_width] * (max_height - len(aligned_lines2)))
        tlines = [f"{line1}{line2}" for line1, line2 in zip(aligned_lines1, aligned_lines2)]
        return '\n'.join(tlines)
    
    def logo():
        logo = r""" _____       _       _                      _____      _            _              
|  __ \     (_)     | |                    / ____|    | |          (_)             
| |__) |__ _ _ _ __ | |__   _____      __ | |     ___ | | ___  _ __ _ _______ _ __ 
|  _  // _` | | '_ \| '_ \ / _ \ \ /\ / / | |    / _ \| |/ _ \| '__| |_  / _ | '__|
| | \ | (_| | | | | | |_) | (_) \ V  V /  | |___| (_) | | (_) | |  | |/ |  __| |   
|_|  \_\__,_|_|_| |_|_.__/ \___/ \_/\_/    \_____\___/|_|\___/|_|  |_/___\___|_|"""
        print(RC.RainbowColorizer(logo))

def printr(*args, **kwargs):
    lines = []
    for arg in args:
        if isinstance(arg, str):
            lines.append(RC.RainbowColorizer(arg))
        elif arg is None:
            lines.append(RC.color("[bbu]None"))
        elif isinstance(arg, dict):
            lines.append(RC.RainbowColorizer(rf"{str(arg)}",(161,141,209),(251,194,235)))
        elif isinstance(arg, tuple):
            lines.append(RC.RainbowColorizer(rf"{str(arg)}",(248,54,0),(249,212,35)))
        elif isinstance(arg, list):
            lines.append(RC.RainbowColorizer(rf"{str(arg)}",(32,226,215),(209,254,125)))
        elif isinstance(arg, bool):
            if arg:
                lines.append(RC.color("[bgn]True"))
            else:
                lines.append(RC.color("[brd]False"))
        elif isinstance(arg, (int, float)):
            lines.append(RC.RainbowColorizer(rf"{str(arg)}",(0,122,223),(73,90,255))) 
        else:
            lines.append(arg)
    text = ' '.join(str(line) for line in lines)
    print(text, **kwargs)




if __name__ == "__main__":
    RC.logo()