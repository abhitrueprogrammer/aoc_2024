safe = 0
with open("input2") as f:
    for l in f:
        row = list(map(lambda x : int(x), l.split(" ")))
        difference = []
        for i in range(1, len(row)):
            difference.append(row[i]- row[i-1])
        sign = difference[0] > 0
        
        for diff in difference:
            if (diff > 0) != sign: 
                print("UNsafe increasing + decreasing: ", difference)
                break
            if abs(diff) < 1 or abs(diff) > 3:
                print("difference < 1 or > 3: ", difference)
                break
        else:
            safe += 1
print(safe)