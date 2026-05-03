#Last Name: Ramit Shukla  Date created: 5/3/2026

itemcount = int(input("Enter number of items in the list: "))

numberlist = []

for indexvalue in range(itemcount):
    numbervalue = int(input("Enter an integer: "))
    numberlist.append(numbervalue)

print("Original list:")
print(numberlist)

numberlist.insert(1, 99)
print("List after inserting 99 at position 1:")
print(numberlist)

numberindex = numberlist.index(99)
numberlist[numberindex] = 100
print("List after replacing 99 with 100:")
print(numberlist)

secondlist = [500, 600, 700, 800, 900]
print("Second list:")
print(secondlist)

numberlist.extend(secondlist)
print("First list after extending with second list:")
print(numberlist)

numberlist.remove(800)
print("First list after removing 800:")
print(numberlist)

numberlist.pop(2)
print("First list after removing third item:")
print(numberlist)

gradeslist = ["A", "B", "C", "A", "A", "C"]

gradecount = gradeslist.count("A")
print("Number of A grades:")
print(gradecount)

gradeindex = gradeslist.index("B")
print("Index of first B grade:")
print(gradeindex)

if "F" in gradeslist:
    print("F is in the list")
else:
    print("F is not in the list")

secondlist.clear()
print("Second list after clearing:")
print(secondlist)

del secondlist
print(secondlist)

playerslist = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]

playerslist.sort()
print("Sorted players list:")
print(playerslist)

players2list = playerslist.copy()
print("Players2 list:")
print(players2list)

players2list.reverse()
print("Players list:")
print(playerslist)

print("Players2 reversed list:")
print(players2list)
