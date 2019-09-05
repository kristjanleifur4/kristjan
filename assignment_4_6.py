top_num = int(input("Upper number for the range: "))

for Number in range(1, top_num +1):
    the_sum = 0
    for n in range(1, Number -1):
        if(Number % n == 0):
            the_sum = the_sum + n

    if(the_sum == Number):
        print(Number)