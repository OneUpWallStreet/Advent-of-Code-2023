
file = open("input.txt")
result = 0
gameNumber = 0
hm = [1]*206


for line in file.readlines():
    line = line.strip()
    game = line.split(":")[1]

    winning, elfs = game.split("|")[0].split(" "), game.split("|")[1].split(" ")

    hs = set()

    for winVal in winning:
        if winVal.isdigit(): hs.add(int(winVal))
    
    matchCount = 0

    for elfVal in elfs:
        if elfVal.isdigit() and int(elfVal) in hs:  matchCount += 1

    multiplier = hm[gameNumber]

    for i in range(gameNumber+1,min(gameNumber + matchCount + 1,206)): hm[i] += multiplier

    result += multiplier

    gameNumber += 1


print("Points worth for the elf: ",result)
