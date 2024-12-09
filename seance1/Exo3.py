amount = float(input("Total amount: "))
nb_item = int(input("Number of items: "))
day = input("Day of the week: ").capitalize() 

if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    discount = 0.10 
elif day in ["Saturday", "Sunday"]:
    discount = 0.20 
else:
    print("Invalid day of the week.")
    exit()

if nb_item > 5:
    discount += 0.05 

price = amount * (1 - discount)

print(f"Total price after discount: {price} dinars")
