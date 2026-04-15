#Last Name: Ramit Shukla  Date created: 4/14/2026

def GetInput():
    return input("Enter comma-separated values: ")

def ParseValues(textvalue):
    valueslist = textvalue.split(",")
    cleanedlist = []
    for item in valueslist:
        cleanedlist.append(item.strip())
    return cleanedlist

def DisplayOutput(valueslist):
    print("Items:")
    for item in valueslist:
        print(item)

textvalue = GetInput()
valueslist = ParseValues(textvalue)
DisplayOutput(valueslist)