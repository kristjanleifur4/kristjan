n = int(input("Input a natural number: ")) # Do not change this line

counter = 0
prime = 0
    # Fill in the missing code below

while counter < n:
    if ((n % 2) != 0) or (n == 2):
        print("Prime")
        break
    else:
        print("Not prime")
        break