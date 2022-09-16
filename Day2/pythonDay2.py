print("Welcome to the tip calculator.\n")
bill = input("What was the total bill? $")
tip_perc = input("What percentage tip would you like to give? 10, 12, or 15? ")
num_people = input("How many people to split the bill? ")
bill_int = float(bill)
tip_perc_int = int(tip_perc)
num_people_int = int(num_people)
if tip_perc_int == 10 :
    tip_person = bill_int * 1.1 / num_people_int
elif tip_perc_int == 12 :
    tip_person = bill_int * 1.12 / num_people_int
elif tip_perc_int == 15 :
    tip_person = bill_int * 1.15 / num_people_int
tip_person_r = round(tip_person, 2)

print(f"Each person should pay: ${tip_person_r}")