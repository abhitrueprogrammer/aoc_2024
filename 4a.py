import re
def mul():
    with open("input4", 'r') as f:
        count = 0
        for line in f.readlines():
            count += line.count("XMAS")
        print("suM:", count)
mul()