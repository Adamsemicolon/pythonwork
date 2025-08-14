amount = int(input("Enter amount in cents "))
if amount < 0 or price > 99:
    print("Price must be between 0 and 99 cents!")
else:
    change = 100 - price
    print("Your change is", change, "cents:")
    quarters = change // 25
    change = change - (quarters * 25)
    dimes = change // 10
    change = change - (dimes * 10)
    nickels = change // 5
    change = change - (nickels * 5)
    pennies = change

    if quarters > 0:
        print(quarters, "quarter(s)")
    if dimes > 0:
        print(dimes, "dime(s)")
    if nickels > 0:
        print(nickels, "nickel(s)")
    if pennies > 0:
        print(pennies, "pennies")