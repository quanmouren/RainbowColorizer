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

if __name__ == "__main__":
    logo = r"""  _____       _       _                      _____      _            _              
 |  __ \     (_)     | |                    / ____|    | |          (_)             
 | |__) |__ _ _ _ __ | |__   _____      __ | |     ___ | | ___  _ __ _ _______ _ __ 
 |  _  // _` | | '_ \| '_ \ / _ \ \ /\ / / | |    / _ \| |/ _ \| '__| |_  / _ | '__|
 | | \ | (_| | | | | | |_) | (_) \ V  V /  | |___| (_) | | (_) | |  | |/ |  __| |   
 |_|  \_\__,_|_|_| |_|_.__/ \___/ \_/\_/    \_____\___/|_|\___/|_|  |_/___\___|_|"""
    print(RainbowColorizer(logo))
    print(RainbowColorizer("Welcome to Rainbow Colorizer"))
