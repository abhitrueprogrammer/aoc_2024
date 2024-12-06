
import re
def mul():
    with open("input3", 'r') as f:
        mul = 0
        for line in f.readlines():
            don = re.findall(r"don't", line)
            do = re.findall(r'do', line)
            matches = re.findall(r"mul\(\d+,\d+\)", line)
            for match in matches:
                match = match.replace("mul(", "")
                match = match.replace(")", "")
                a,b = map(int, match.split(","))
                mul += a*b
        print("suM:", mul)
mul()