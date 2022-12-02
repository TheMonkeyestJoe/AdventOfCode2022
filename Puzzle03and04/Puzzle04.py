valueDict = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
resultDict = {"A X": 3, "A Y": 6, "A Z": 0, "B X": 0, "B Y": 3, "B Z": 6, "C X": 6, "C Y": 0, "C Z": 3}
loseDict = {"A": "Z", "B": "X", "C": "Y"}
winDict = {"A": "Y", "B": "Z", "C": "X"}
drawdict = {"A": "X", "B": "Y", "C": "Z"}
dictDict = {"X": loseDict, "Y": drawdict, "Z": winDict}

theInput = open("Puzzle03input.txt", "r")
inputLines = theInput.readlines()
totalScore = 0
for line in inputLines:
    optimalChoice = dictDict[line[2]][line[0]]
    print(line, optimalChoice)
    totalScore += valueDict[optimalChoice] + resultDict[line[0] + " " + optimalChoice]

print("Total score following the finished strategy guide:", totalScore)
theInput.close()