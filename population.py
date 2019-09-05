year = int(input("Years: "))
population = 307357870

population = float(population + (31536000/7 - 31536000/13 + 31536000/35) * year) #31536000 eru sekúndur í einu ári 

if year >= 0 :
    print("New population after" ,year, "years is" , int(population))

else :
    print("Invalid input!")
