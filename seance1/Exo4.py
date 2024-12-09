valeurp=False
while(valeurp==False):
       age1 = int(input("Please type in the age of the first person: "))
       if (age1>0):
           valeurp=True
       else: print("Please enter a correct value!")
valeurp=False
while(valeurp==False):
       age2 = int(input("Please type in the age of the second person: "))
       if (age2>0):
           valeurp=True
       else: print("Please enter a correct value!")
if age1 > age2:
    print(f"The older age is: {age1}")
elif age2 > age1:
    print(f"The older age is: {age2}")
else:
    print("Both people are the same age!")
