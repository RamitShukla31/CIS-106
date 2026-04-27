#Last Name: Ramit Shukla  Date created: 4/26/2026

def DisplayNames(namelist):
    print("Names:")
    for namevalue in namelist:
        print(namevalue)

def DisplayReverseNames(namelist):
    print("Names in Reverse:")
    for indexvalue in range(len(namelist) - 1, -1, -1):
        print(namelist[indexvalue])


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

DisplayNames(namelist)
DisplayReverseNames(namelist)
