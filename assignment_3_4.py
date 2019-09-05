n = int(input("Input an int: ")) # Do not change this line

factor = 1

while factor <= n:
    if n % factor == 0:
        print(factor)
    factor += 1
        