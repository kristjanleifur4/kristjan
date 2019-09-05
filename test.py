first = int(input("First: "))
step = int(input("Step: "))
the_sum = 0
i = 0

while the_sum <= 100:
    i += step
    the_sum = first + i
    print(i, end=" ")
else:
    print()
    print("Sum of series:",the_sum)






