from math import sqrt
neg=True
while neg:
    nbr=int(input("entrez un nombre: "))
    if(nbr<0):
        print("invalid number! \n") 
    else: neg=False
if (nbr!=0):
    print(sqrt(nbr))