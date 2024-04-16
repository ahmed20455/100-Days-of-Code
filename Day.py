print("Welcome to Tip Calculator")
bill = float(input("What was the total bill?$"))
tip_per = int(input("What percentage tip would you like to give 10,12 or 15 ?"))
tip = tip_per/100
total_bill = bill + (tip*bill)
ind = int(input("How many people to split the bill ?"))
ind_bill = round(total_bill / ind,2)
print(f"Each person should pay: ${ind_bill}.")

