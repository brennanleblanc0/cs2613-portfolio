filename = input("Input the file name:\n")
fileIn = open(filename)
valid = []

for e in fileIn:
    val = float(e)
    if (val <= 100 and val >= 0):
        valid.append(val)

avg = 0
for e in valid:
    avg += e
avg /= len(valid)

aboveAvg = 0
occur = [0, 0, 0, 0, 0]

for e in valid:
    if (e >= 80 and e <= 100):
        occur[0] += 1
    elif (e >= 65 and e < 80):
        occur[1] += 1
    elif (e >= 55 and e < 65):
        occur[2] += 1
    elif (e >= 50 and e < 55):
        occur[3] += 1
    else:
        occur[4] += 1

    if (e > avg):
        aboveAvg += 1

print(f"A\t{occur[0]}")
print(f"B\t{occur[1]}")
print(f"C\t{occur[2]}")
print(f"D\t{occur[3]}")
print(f"F\t{occur[4]}")
print(f"# Valid Grades above Average: {aboveAvg}")