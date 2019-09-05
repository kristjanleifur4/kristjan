num = int(input("Enter an integer: "))

the_sum = 0

count_even = 0

count_odd = 0

largest_so_far = 0

while num > 0 :
    the_sum += num
    print("Cumulative total: " , the_sum)
    if  num > largest_so_far :
        largest_so_far = num
    if num % 2 == 0 :
        count_even += 1
    else :
        count_odd += 1
    num = int(input("Enter an integer: "))
else: 
    if the_sum > 0:
        print("Largest number: " , largest_so_far,) 
        print("Count of even numbers: " , count_even)
        print("Count of odd numbers: " , count_odd)

        


