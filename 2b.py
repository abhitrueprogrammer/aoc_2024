safe = 0
def findIndex( row):
    difference = []
    for i in range(1, len(row)):
        difference.append(row[i]- row[i-1])
    sign = difference[0] > 0
    # print(len(row), len(difference))
    for i,diff in enumerate(difference):
        if (diff > 0) != sign: 
            return i
        if abs(diff) < 1 or abs(diff) > 3:
            return i
    return -1

with open("input2") as f:
    for l in f:
        row = list(map(lambda x : int(x), l.split(" ")))
        print(row)
        for i in range(-1, len(row)):
            if(i == -1):
                temp_row = row
            else:
                temp_row = row[:i] + row[i+1:]
            print(temp_row)
            if(findIndex(temp_row) == -1):
                print("Safe")
                safe += 1
                break
        print("\n")

# subject add
