#Last Name: Ramit Shukla  Date created: 3/5/2026

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
f = open(os.path.join(script_dir, "data5.txt"), "r")

c = 0 
totaltuition = 0.0

#get first part of the data 

lastname = f.readline()

while lastname !="":    # detect end of file
    dcode = f.readline()
    credits = float(f.readline())

    if dcode == 'I':
        cotspercredit = 250.00
    else:
        cotspercredit = 500.00

    tuition  = cotspercredit * credits
    c = c + 1
    totaltuition = totaltuition + tuition 

    print("Student:       ", lastname)
    print("Credits taken: ", credits)
    print("Tuition Owed   ", tuition)

    lastname = f.readline()

f.close()
print("Number of students ", c)
print("Total Tuition Owed ", totaltuition)







