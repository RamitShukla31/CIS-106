#Last Name: Ramit Shukla  Date created: 4/14/2026

def ProcessName(fullname):
    
    fullname = fullname.strip()
    
    if fullname == "":
        return "Invalid input: empty name."
    
    nameparts = fullname.split()
    
    if len(nameparts) != 2:
        return "Invalid input: please enter first and last name only."

    firstname = nameparts[0]
    lastname = nameparts[1]
    
    firstinitial = firstname[0]
    
    return f"{lastname}, {firstinitial}."

fullname = input("Enter first and last name (Firstname Lastname): ")

formattedname = ProcessName(fullname)

print(f"Formatted Name: {formattedname}")