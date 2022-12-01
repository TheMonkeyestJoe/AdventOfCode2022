theInput = open("puzzle1input.txt", "r")
lines = theInput.readlines()
theMax = -1
currentCount = 0
for line in lines:
    if line != "\n":
        currentCount += int(line)
    else:
        theMax = max(theMax, currentCount)
        currentCount = 0
print("Amount carried by the most-prepared elf:", theMax)