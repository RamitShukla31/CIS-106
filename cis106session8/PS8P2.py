def CompBatAvg(hitcount, atbats):
    if atbats == 0:
        batavg = 0.0
    else:
        batavg = hitcount / atbats
    return batavg


playercount = 0

userresp = input("Do you want to do this program (Yes or No): ")

while userresp.lower() == "yes":
    lastname = input("Enter player's last name: ")
    hitcount = float(input("Enter number of hits: "))
    atbats = float(input("Enter number of at bats: "))

    batavg = CompBatAvg(hitcount, atbats)

    print(f"Last Name: {lastname}")
    print(f"Batting Average: {batavg}")

    playercount = playercount + 1

    userresp = input("Do you want to continue with this program? ")

print(f"Total number of players entered: {playercount}")