
file = open("input.txt")
timeLine = file.readline().strip()
time = [value for value in timeLine.split(":")[1].split(" ") if value]

distanceLine = file.readline().strip()
distance = [distance for distance in distanceLine.split(":")[1].split(" ") if distance]

raceStartTime = int("".join(time))
recordDistance = int("".join(distance))


winCounter = 0 

for x in range(raceStartTime):
    if x * (raceStartTime-x) > recordDistance: winCounter += 1 


print("ways can you beat the record in this one much longer race: {}".format(winCounter))