name = input("Please enter your name: ")
valeurp=False
if name == "VIP":
    print("Enjoy the show for free!")
else:
    while(valeurp==False):
       nbticket = int(input("How many tickets would you like to buy? "))
       if (nbticket>0):
           valeurp=True
       else: print("Please enter a correct value!")
    prix = 15.5
    prix_total = nbticket * prix
    print(f"The total cost is {prix_total}")
    print("Enjoy your tickets!")
