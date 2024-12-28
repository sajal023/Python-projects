size=input("enter the size, 'S' for small, 'M' for large, 'L' for large pizza: ")
bill=0
if size=="S":
    bill+=15
    add_pepp=input("enter 'Y' to add pepperoni and 'N' to not add: ")
    if add_pepp=="Y":
        bill+=2
    else:
        bill=bill
elif size=="M":
    bill+=20
    add_pepp = input("enter 'Y' to add pepperoni and 'N' to not add: ")
    if add_pepp == "Y":
        bill += 3
    else:
        bill = bill
else:
    bill += 25
    add_pepp = input("enter 'Y' to add pepperoni and 'N' to not add: ")
    if add_pepp == "":
        bill += 3
    else:
        bill = bill
add_cheese=input("enter 'Y' to add extra cheese and 'N' to not add: ")
if add_cheese=="Y":
    bill=bill+1
else:
    bill=bill
print(f"total bill is {bill}")
