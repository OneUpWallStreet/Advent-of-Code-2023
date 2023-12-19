file = open("input.txt")
result = 0


for line in file.readlines():
    line = line.strip()

    game = line.split(":")[1]

    winning, elfs = game.split("|")[0].split(" "), game.split("|")[1].split(" ")

    hs = set()

    for winVal in winning:
        if winVal.isdigit(): hs.add(int(winVal))
    
    matchCount = 0

    for elfVal in elfs:
        if elfVal.isdigit() and int(elfVal) in hs: 
            if matchCount == 0: matchCount += 1
            else: matchCount *= 2

    result += matchCount
    

print("Points worth for the elf: ",result)


