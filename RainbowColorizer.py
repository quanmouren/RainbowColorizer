import shutil
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
                r = int(start_color[0] + (end_color[0] - start_color[0]) * t)
                g = int(start_color[1] + (end_color[1] - start_color[1]) * t)
                b = int(start_color[2] + (end_color[2] - start_color[2]) * t)
                result += f"\033[38;2;{r};{g};{b}m{char}"
            result += "\033[0m\n"
        return result.rstrip('\n')

    def separator(filler="-", title=""):
        size = shutil.get_terminal_size()
        if title == "":
            a = (filler * (size.columns-1))
        else:
            count = 0
            for char in title:
                if '\u4e00' <= char <= '\u9fff':
                    count += 1
            a = (filler * 4)[:4] + f" {title} " + (filler * (size.columns - len(title) - 7))[:(size.columns - len(title) - 7 - count)]
        for index, char in enumerate(a):
            hue = int(360 * (index / size.columns))
            rgb = hue_to_rgb(hue)
            print(RC.RainbowColorizer(char, rgb, rgb), end='')
        print("")


if __name__ == "__main__":
    logo = r"""  _____       _       _                      _____      _            _              
 |  __ \     (_)     | |                    / ____|    | |          (_)             
 | |__) |__ _ _ _ __ | |__   _____      __ | |     ___ | | ___  _ __ _ _______ _ __ 
 |  _  // _` | | '_ \| '_ \ / _ \ \ /\ / / | |    / _ \| |/ _ \| '__| |_  / _ | '__|
 | | \ | (_| | | | | | |_) | (_) \ V  V /  | |___| (_) | | (_) | |  | |/ |  __| |   
 |_|  \_\__,_|_|_| |_|_.__/ \___/ \_/\_/    \_____\___/|_|\___/|_|  |_/___\___|_|"""
    print(RC.RainbowColorizer(logo))
    print(RC.RainbowColorizer("Welcome to Rainbow Colorizer"))
    RC.separator("/","title标题")

