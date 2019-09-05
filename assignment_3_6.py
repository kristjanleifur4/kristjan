#Write a program using a while statement, that finds the only two-digit number where the following applies:
#When you square it, the resulting three-digit number has its rightmost two digits the same as the original two-digit number.
#That is, for a number in the form AB:
#AB * AB = CAB, for some C.
num = 10

while num <= 99:
    AB = num
    squared = (AB)** 2
    s_AB = squared % 100
    if s_AB == AB and squared < 1000:
        print(AB)

    num += 1