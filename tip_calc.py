print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
valid_tips = [10, 12, 15]
tip_percentage = 0
while tip_percentage not in valid_tips:
    tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))

tip_amount = (bill / 100) * tip_percentage
total_to_pay = bill + tip_amount

each_person_pays = total_to_pay / num_people

print(f"Each person should pay: ${each_person_pays:.2f}")