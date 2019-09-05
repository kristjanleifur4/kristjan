m = int(input("Input the first integer: ")) # Do not change this line
n = int(input("Input the second integer: "))

gcd = 1
# finding GCD
for i in range(min(m,n),0,-1):                    
    if (m%i) == 0 and (n%i) == 0:
        gcd = i
        break
    
# printing GCD
print("The GCD of the two numbers is ", gcd)