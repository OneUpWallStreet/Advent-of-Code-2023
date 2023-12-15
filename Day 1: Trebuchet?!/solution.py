
# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet

# In this example, the calibration values of these four lines are 12, 38, 15, and 77. 
# Adding these together produces 142.


file = open("input.txt")
result = 0

for line in file.readlines():

    l = 0
    r = len(line) - 1
    num = ""
    while not line[l].isnumeric():
        l += 1
    num += line[l]

    while not line[r].isnumeric():
        r -= 1
    num += line[r]

    result += int(num)



print("sum of all of the calibration values: ",  result)