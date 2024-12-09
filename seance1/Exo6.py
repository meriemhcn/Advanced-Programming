valeurp=False
while(valeurp==False):
       price = float(input("Please type in a price: "))
       if (price>0):
           valeurp=True
       else: print("Please enter a correct value!")


dinars = int(price)  
centimes = int(round((price - dinars) * 100)) 

print(f"Dinars: {dinars}")
print(f"Centimes: {centimes}")
