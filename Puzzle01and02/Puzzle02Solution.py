theInput = open("puzzle1input.txt", "r")
lines = theInput.readlines()
topThree = [-1, -1, -1]
currentCount = 0
for line in lines:
    if line != "\n":
        currentCount += int(line)
    else:
        for i in range(3):
            if topThree[i] < currentCount:
                currentCount, topThree[i] = topThree[i], currentCount
        currentCount = 0
print("Amount carried by the 3 most-prepared elves:", sum(topThree))