import re
def mul():
    stri = ""
    do = True
    mul = 0
    with open("input3", 'r') as f:
        for line in f.readlines():
            for letter in line:
                stri += letter
                if("don't()" in stri):
                    print("Dont' found")
                    do = False
                    stri = stri.replace("don't", "")
                if("do()" in stri):
                    do = True
                    stri = stri.replace("do", "")
                match = re.findall(r"mul\(\d+,\d+\)", stri)
                if(match):
                    if(do):
                        match[0] = match[0].replace("mul(", "")
                        match[0] = match[0].replace(")", "")
                        a,b = map(int, match[0].split(","))
                        mul += a*b
                    stri = re.sub(r"mul\(\d+,\d+\)", "", stri)
    print(mul)
mul()