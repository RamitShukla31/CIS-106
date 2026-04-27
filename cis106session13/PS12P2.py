#Last Name: Ramit Shukla  Date created: 4/26/2026

def DisplayNames(namelist, scorelist):
    print("Names and Scores:")
    for indexvalue in range(len(namelist)):
        print(f"{namelist[indexvalue]} - {scorelist[indexvalue]}")

def DisplayReverseNames(namelist, scorelist):
    print("Names and Scores in Reverse:")
    for indexvalue in range(len(namelist) - 1, -1, -1):
        print(f"{namelist[indexvalue]} - {scorelist[indexvalue]}")


namelist = [
    "Smith",
    "Johnson",
    "Williams",
    "Brown",
    "Jones",
    "Garcia",
    "Miller",
    "Davis",
    "Rodriguez",
    "Martinez"
]

scorelist = [
    85,
    90,
    78,
    92,
    88,
    76,
    95,
    89,
    84,
    91
]

DisplayNames(namelist, scorelist)
DisplayReverseNames(namelist, scorelist)

