import os

# Get path to data.txt

workDir = os.path.dirname(__file__)
path = f"{workDir}\data.txt"

# Open the file, and read each individual line, organizing it into a list

readMeFile = open(path, "r")
myList = readMeFile.readlines()

# Get the values as strings from the list
# tD = totalDamage
# rS1 = reloadSpeed
# ttf = time to fire

tD = myList[7][12:]
rS = myList[8][12:]
rC = myList[9][12:]
ttf = myList[10][4:]

# To calulate true DPS, we just take tD2 (totalDamage2) and factor in the reload speed + time to spire

calculation = (float(ttf) + (float(rS) * int(rC)))
calculation2 = (int(tD) / calculation)

print(tD2, rS2, rC2, ttf2)
print(calculation2)
