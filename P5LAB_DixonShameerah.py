# Shameerah Dixon
# May 10, 2026
# P5LAB.py
# Using user-defined functions

import random

def disperse_change(change):

    # Change to total cents and calculate currency
    
    total_cents = int(round(change * 100))

    # Calculate Dollars
    dollars = total_cents // 100
    total_cents %= 100

    # Calculate Quarters
    quarters = total_cents // 25
    total_cents %= 25

    # Calculate Dimes
    dimes = total_cents // 10
    total_cents %= 10

    # Calculate Nickels
    nickels = total_cents // 5
    total_cents %= 5

    # Calculate Pennies
    pennies = total_cents

    # Output results 
    if dollars > 0:
        if dollars == 1:
            print(f"{dollars} Dollar")
        else:
            print(f"{dollars} Dollars")

    if quarters > 0:
        if quarters == 1:
            print(f"{quarters} Quarter")
        else:
            print(f"{quarters} Quarters")

    if dimes > 0:
        if dimes == 1:
            print(f"{dimes} Dime")
        else:
            print(f"{dimes} Dimes")

    if nickels > 0:
        if nickels == 1:
            print(f"{nickels} Nickel")
        else:
            print(f"{nickels} Nickels")

    if pennies > 0:
        if pennies == 1:
            print(f"{pennies} Penny")
        else:
            print(f"{pennies} Pennies")

def main() :
    # Logic goes here

    # Generate the amount owed
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe: ${amount_owed: .2f}")
    
    # Create variable to represent money put into machine
    money_in = float(input("How much cash will you put in the self-checkout? "))

    # Calculate change owed to customer
    change = money_in - amount_owed
    print(f"Change owed: ${change: .2f}")

    # Call the disperse change function
    disperse_change(change)



# Call the main function
main()


