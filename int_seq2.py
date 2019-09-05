num = int(input("Enter an integer: "))
the_sum = 0
odd_num = 0
evn_num = 0
highest_num = 0

while num > 0:
    the_sum += num
    print("Cumulative total:",the_sum)      #eftir second input þá prentast út allt print, á ekki að gerast
    if highest_num < num:
        highest_num = num
    if num % 2 == 0:
        evn_num += 1
    else:
        odd_num += 1
    num = int(input("Enter an integer: "))
    print("Largest number:", highest_num)
    print("Count of even numbers:", evn_num)
    print("Count of odd numbers:", odd_num)