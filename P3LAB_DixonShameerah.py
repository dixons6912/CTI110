# Shameerah Dixon
# April 19, 2026
# P3LAB.py
# Converting Currency

def main():
    # Get the amount of money 
    try:
        amount = float(input("Enter the amount of money as a float: $"))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    # Change to total cents and calculate currency
    
    total_cents = int(round(amount * 100))

    if total_cents <= 0:
        print("No change")
        return

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


if __name__ == "__main__":
    main()
