from collections import defaultdict

file = open("input.txt")

data = []
seedRanges = file.readline().strip().split(":")[1].split(" ")[1:]

lines = file.readlines()
index = 0 
result = float('inf')
seeds = []


def insertData(name: str, values: list):
    cur = []
    for value in values:
        destStart, sourceStart, offset = int(value[0]), int(value[1]), int(value[2])
        cur.append([destStart,sourceStart,offset])
    data.append(cur)

while index < len(lines):
    line = lines[index].strip()
    if line == "\n":
        index += 1
        continue
    values = []
    while index < len(lines) and lines[index] != "\n":
        values.append(lines[index].strip().split(" "))
        index += 1

    if len(values) != 0: insertData(values[0][0],values[1:])

    index += 1


l, r = 0, 1

while r < len(seedRanges):
    print('On Range: {} -> {}'.format(seedRanges[l], int(seedRanges[l]) + int(seedRanges[r])))
    for seed in range(int(seedRanges[l]),int(seedRanges[l]) + int(seedRanges[r])): seeds.append(seed)
    l += 2
    r += 2


for seed in seeds:
    cur = int(seed)
    for hashmap in data:
        for ranges in hashmap:
            destStart, sourceStart, rLength = ranges[0], ranges[1], ranges[2]
            if cur >= sourceStart and cur < sourceStart + rLength:
                cur = destStart + (cur-sourceStart)
                break
    result = min(result,cur)

print("lowest location number that corresponds to any of the initial seeds: ",result)
