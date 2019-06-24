import math

def main():
		
	print("This is an EMI Calculator.\nEnter details to proceed.")

	#Getting details: 

	principal = float(input("\n\nEnter principal amount.\nRs. "))
	rate = float(input("Enter rate of interest(%)\n"))
	term_period = int(input("Enter term period:"))
	terms_in = input("Terms in:\n\ta)Years \tb)Months\tc)Week\n")
	interval = input("Compounding interval:\n\ta)Annually \tb)Monthly\tc)Weekly\n")

	if terms_in == "a":
	    n = term_period*12
	elif terms_in == "c":
	    n = math.ceil(term_period/4)
	    
	rate_revised = rate/1200

	#Formula of calculating mortgage for monthly payments:
	mortgage = (principal*rate_revised*((1+rate_revised)**n))/(((1+rate_revised)**n)-1) 

	if interval == "a":
	    mortgage*=12
	    print(f"\nThe mortgage value is:\nRs. {round(mortgage,2)}, annually.")
	elif interval == "c": 
	    mortgage/=4
	    print(f"\nThe mortgage value is:\nRs. {round(mortgage,2)}, weekly.")
	else:
	    print(f"\nThe mortgage value is:\nRs. {round(mortgage,2)}, monthly.")

if __name__ == '__main__':
	main()