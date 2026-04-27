#Last Name: Ramit Shukla  Date created: 4/26/2026

def LoadData(filenamevalue):
    namelist = []
    scorelist = []

    fileobject = open(filenamevalue, "r")

    for linevalue in fileobject:
        parts = linevalue.strip().split(",")

        if len(parts) == 2:
            namelist.append(parts[0].strip())
            scorelist.append(int(parts[1].strip()))

    fileobject.close()
    return namelist, scorelist


def DisplayNames(namelist, scorelist):
    print("Names and Scores:")
    for indexvalue in range(len(namelist)):
        print(f"{namelist[indexvalue]} - {scorelist[indexvalue]}")


def FindHighest(namelist, scorelist):
    highvar = 0
    highindex = 0

    for indexvalue in range(len(scorelist)):
        if scorelist[indexvalue] > highvar:
            highvar = scorelist[indexvalue]
            highindex = indexvalue

    print(f"Highest Score: {namelist[highindex]} - {highvar}")


def FindLowest(namelist, scorelist):
    lowvar = 999999
    lowindex = 0

    for indexvalue in range(len(scorelist)):
        if scorelist[indexvalue] < lowvar:
            lowvar = scorelist[indexvalue]
            lowindex = indexvalue

    print(f"Lowest Score: {namelist[lowindex]} - {lowvar}")


filenamevalue = input("Enter filename: ")

namelist, scorelist = LoadData(filenamevalue)

if len(namelist) == 0:
    print("No valid data found. Use format: Lastname,Score")
else:
    DisplayNames(namelist, scorelist)
    FindHighest(namelist, scorelist)
    FindLowest(namelist, scorelist)