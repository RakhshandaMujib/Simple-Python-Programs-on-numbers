import math

def main():
    print("This program will return the total change in different denominations-\nquarters, dimes, nickels and pennies:\n\n")
    cost = float(input("What is the cost of article (in USD)?\n"))
    amount = float(input("What is the amount you've paid (in USD)?"))
    change = amount-cost
    
    if change <= 0:
        print("You won't get any change!")
    else: 
        quarters = math.floor(round(change,2)/0.25) # 1 quarter = 25% of 1 USD.
        change -= quarters*0.25
        nickels = math.floor(round(change,2)/0.2) # 1 nickel = 20% of 1 USD.
        change -= nickels*0.2
        dimes = math.floor(round(change,2)/.1) # 1 dime = 10% of 1 USD.
        change -= dimes*0.1
        pennies = math.floor(round(change,2)/.01) # 1 penny = 1% of USD.
        print("\n\nThe change you get is:\n")
        print(f"{quarters} quarter(s)\n{nickels} nickel(s)\n{dimes} dime(s)\n{pennies} penny/pennies")

if __name__ == '__main__':
    main()