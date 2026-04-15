#Last Name: Ramit Shukla  Date created: 4/14/2026


def GetInput():
    return input("Enter a line of text: ")

def CleanSpaces(textvalue):
    
    wordslist = textvalue.strip().split()
    cleanedtext = " ".join(wordslist)
    return cleanedtext

def ReverseText(textvalue):
    reversedtext = textvalue[::-1]
    return reversedtext

def DisplayOutput(resultvalue):
    print(f"Reversed Text: {resultvalue}")

textvalue = GetInput()

cleanedtext = CleanSpaces(textvalue)
reversedtext = ReverseText(cleanedtext)

DisplayOutput(reversedtext)