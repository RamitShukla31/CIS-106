#Last Name: Ramit Shukla  Date created: 4/26/2026

def LoadData(filenamevalue):
    namelist = []
    averagelist = []

    fileobject = open(filenamevalue, "r")

    for linevalue in fileobject:
        parts = linevalue.strip().split(",")

        if len(parts) == 2:
            namelist.append(parts[0].strip())
            averagelist.append(float(parts[1].strip()))

    fileobject.close()
    return namelist, averagelist


def DisplayPlayers(namelist, averagelist):
    print("Players and Batting Averages:")
    for indexvalue in range(len(namelist)):
        print(f"{namelist[indexvalue]} - {averagelist[indexvalue]:.3f}")


def SearchPlayer(namelist, averagelist, searchname):
    foundflag = False

    for indexvalue in range(len(namelist)):
        if namelist[indexvalue].lower() == searchname.lower():
            print(f"{namelist[indexvalue]} - {averagelist[indexvalue]:.3f}")
            foundflag = True
            break

    if foundflag == False:
        print("Name not found")


filenamevalue = input("Enter filename: ")

namelist, averagelist = LoadData(filenamevalue)

DisplayPlayers(namelist, averagelist)

userinput = input("Enter last name to search (or 'exit' to quit): ")

while userinput.lower() != "exit":
    SearchPlayer(namelist, averagelist, userinput)
    userinput = input("Enter last name to search (or 'exit' to quit): ")