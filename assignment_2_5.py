year = int(input("Input a year: ")) # Do not change this line

if ((year % 400 == 0 or year % 100 != 0) and (year % 4 == 0)):
    print(True)
else:
    print(False)
# Fill in the missing code below
