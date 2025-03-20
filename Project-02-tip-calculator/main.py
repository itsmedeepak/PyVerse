print("Welcome to Tip Calculator!")

bill = float(input("What was the total bill? $ "))
tip_percent = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
distribution = int(input("How many people to split the bill? "))

total_with_tip = bill * (1 + tip_percent / 100)
each_person_pays = round(total_with_tip / distribution, 2)

print(f"Each person should pay: ${each_person_pays}")