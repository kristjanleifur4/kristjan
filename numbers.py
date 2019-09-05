divisors = 0
for i in range(10,100):
    for n in range(1,i):
        while i % n == 0:
            divisors += 1
            i += 1
        if divisors == 10:
            print(i)