result = 0

file = open("input.txt")

red, green, blue = 12, 13, 14

LIMITS = {
    "red": 12, 
    "green": 13,
    "blue": 14
}

for line in file.readlines():
    line = line.strip()
    label, game = line.split(":")
    isValid = True
    rounds = game.split(";")
    index  = 0
    while index < len(rounds) and isValid:
        curRound = rounds[index]
        subRound = curRound.split(",")
        for single in subRound:
            cubeData = single.split(" ")
            if LIMITS[cubeData[2]] < int(cubeData[1]):
                isValid = False
                break
        
        index += 1
    
    if isValid: result += int(label.split(" ")[1])

print("Valid Cube Games wid Elf:  ", result)


