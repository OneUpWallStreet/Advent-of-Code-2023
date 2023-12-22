
file = open("input.txt")
timeLine = file.readline().strip()
time = [int(value) for value in timeLine.split(":")[1].split(" ") if value]

distanceLine = file.readline().strip()
distance = [int(distance) for distance in distanceLine.split(":")[1].split(" ") if distance]

result = 1


for index in range(len(time)):

    raceStartTime = time[index]
    recordDistance = distance[index] 
    winCounter = 0 
    
    for x in range(raceStartTime):
        if x * (raceStartTime-x) > recordDistance: winCounter += 1 

    result *= winCounter

print("the number of ways you could beat the record in each race: {}".format(result))