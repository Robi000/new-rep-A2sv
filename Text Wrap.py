import textwrap

def wrap(string, max_width):
    s = ""
    for i in range(len(string)):
        s += string[i]
        if (i+1)%max_width == 0:
            s += "\n"
        
    return s

if __name__ == '__main__':
