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


def checkForSymbol(r,c):
    for dr, dc in directions:
        if r+dr in range(rows) and c+dc in range(cols) and not mat[r+dr][c+dc].isdigit() and mat[r+dr][c+dc] != ".": return True
    return False
    

for r in range(rows):
    for c in range(cols):
        isValidNum = False
        num = ""
        while c in range(cols) and  mat[r][c].isdigit() and (r,c) not in visited:
            visited.add((r,c))
            if checkForSymbol(r,c):
                isValidNum = True
            num += mat[r][c]
            c += 1
        if isValidNum: result += int(num)
        
print("parts missing from the engine: ",result)



