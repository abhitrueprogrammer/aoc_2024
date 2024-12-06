def main():
    d = {}
    with open('input', 'r') as f:
        for l in f: 
            a, b = map(lambda x: int(x), l.split())
            if( a not in d):
                d[a] = [0, 0]
            if b not in d:
                d[b] = [0, 0]
            if a in d: 
                d[a][0] = 1
            if b in d:
                d[b][1] += 1
    sum = 0
    for key in d:
        if(d[key][0] != 0):
            sum += key * d[key][1]
    print(sum)

main()