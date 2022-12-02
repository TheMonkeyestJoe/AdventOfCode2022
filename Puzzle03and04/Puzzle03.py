valueDict = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
resultDict = {"A X": 3, "A Y": 6, "A Z": 0, "B X": 0, "B Y": 3, "B Z": 6, "C X": 6, "C Y": 0, "C Z": 3}

theInput = open("Puzzle03input.txt", "r")
inputLines = theInput.readlines()
totalScore = 0
for line in inputLines:
    totalScore += valueDict[line[2]] + resultDict[line[0:3]]

print("Total score following the strategy guide:", totalScore)
theInput.close()