file = open("input.txt")

mat = []

for line in file.readlines():
    line = line.strip()
    row = []
    for ch in line: row.append(ch)
    mat.append(row)

visited = set()
rows, cols = len(mat), len(mat[0])
directions = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
result = 0
numVisited = set()

def findNumber(r,c):
    num = ""
    arr = mat[r]
    p1, p2 = c, c + 1
    # Check Left Side of Num
    while p1 >= 0 and arr[p1].isdigit():
        num = arr[p1] + num
        numVisited.add((r,p1))
        p1 -= 1
    
    while p2 < len(arr) and arr[p2].isdigit():
        num += arr[p2]
        numVisited.add((r,p2))
        p2 += 1
    
    return num


def fetchGear(r,c):
    for dr, dc in directions:
        if r+dr in range(rows) and c+dc in range(cols) and mat[r+dr][c+dc].isdigit() and (r+dr,c+dc) not in numVisited:
            return findNumber(r+dr,c+dc)            


for r in range(rows):
    for c in range(cols):
        if mat[r][c] == "*" and (r,c) not in visited:
            visited.add((r,c))
            gear1, gear2 = fetchGear(r,c), fetchGear(r,c)
            if gear1 != None and gear2 != None: result += int(gear1)*int(gear2)

print("gear ratio of every gear: ",result)