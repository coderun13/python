#Work Flow
#Inputs we need from the user
# Total rent
# Total food ordered for snacking
# Electricity units spend
# Charge per unit 
# Persons living in room/flat

#Process
# Total bill = electricity spent * charge per unit

# Output
# Total amount you've to pay is = (food + rent + total bill)// persons

rent = int(input("Enter your hostel/Flat rent = "))
Food = int(input("Enter amount spent for food = "))
Electricity_spent = int(input("Enter total electricity spent = "))
Charge_per_unit = int(input("Enter the charge per unit = "))
Person = int(input("Enter total person living in room/Flat = "))

Total_Bill = Electricity_spent * Charge_per_unit
Total_amount = (Food + Total_Bill + rent) / Person

print("The total electricity bill is  ",Total_Bill)
print("Amount to be paid per person is ", Total_amount)
