valeurp=False
while(valeurp==False):
       nbperson=int(input("How many people need a ride? "))
       if (nbperson>=0):
           valeurp=True
       else: print("Please enter a correct value!")
valeurp=False
while(valeurp==False):
       nbpersontaxi=int(input("How many people fit in one taxi? "))
       if (nbpersontaxi>0):
           valeurp=True
       else: print("Please enter a correct value!")

nbtaxi = nbperson // nbpersontaxi  
if nbperson % nbpersontaxi != 0:  
    nbtaxi += 1 

print(f"Number of taxis needed: {nbtaxi}")