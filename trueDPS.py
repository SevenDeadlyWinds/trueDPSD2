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

tD1 = myList[7]
rS1 = myList[8]
rC1 = myList[9]
ttf1 = myList[10]

# Get the values by themselves

tD2 = tD1[12:]
rS2 = rS1[12:]
rC2 = rC1[12:]
ttf2 = ttf1[4:]

# To calulate true DPS, we just take tD2 (totalDamage2) and factor in the reload speed + time to spire

calculation = (float(ttf2) + (float(rS2) * int(rC2)))
calculation2 = (int(tD2) / calculation)

print(tD2, rS2, rC2, ttf2)
print(calculation2)
