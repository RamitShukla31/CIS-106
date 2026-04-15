#Last Name: Ramit Shukla  Date created: 4/14/2026

def BuildLine(textvalue, charcount):
    textvalue = textvalue.strip()
    if textvalue == "":
        return "Invalid input"
    repeatedtext = textvalue
    while len(repeatedtext) < charcount:
        repeatedtext = repeatedtext + textvalue
    return repeatedtext[:charcount]

def ShiftLeft(linevalue):
    return linevalue[1:] + linevalue[0]

def ShiftRight(linevalue):
    return linevalue[-1] + linevalue[:-1]


textvalue = input("Enter a line of text: ")
charcount = int(input("Enter number of characters per line: "))
linecount = int(input("Enter number of lines to print: "))
directionvalue = input("Enter scroll direction (left or right): ").strip().lower()

linevalue = BuildLine(textvalue, charcount)

if linevalue == "Invalid input":
    print(linevalue)
elif directionvalue != "left" and directionvalue != "right":
    print("Invalid direction")
else:
    currentline = linevalue
    for _ in range(linecount):
        print(currentline)
        if directionvalue == "left":
            currentline = ShiftLeft(currentline)
        else:
            currentline = ShiftRight(currentline)