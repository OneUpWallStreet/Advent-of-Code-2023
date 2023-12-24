from collections import defaultdict
import json
file = open("input.txt")


instructions = list(file.readline().strip())

for i, ch in enumerate(instructions):
    if ch == "L": instructions[i] = 0
    else: instructions[i] = 1


def fetchNextInstructions(index: int):
    if index+1 < len(instructions): return index+1
    else: return 0

graph = defaultdict(list)

# Create Graph
for line in file.readlines():
    line = line.strip()
    if not line: continue

    root, paths = line.split("=")
    root, paths = root.strip(), paths.strip()[1:len(paths)-2].split(",")
    paths[1] = paths[1][1:]
    graph[root].append(paths)


cur = "AAA"
steps = index = 0


while True:

    instruction = instructions[index]
    cur = graph[cur][0][instruction]
    steps += 1
    index = fetchNextInstructions(index)

    if cur == "ZZZ": break



print("steps required to reach ZZZ: ", steps)
