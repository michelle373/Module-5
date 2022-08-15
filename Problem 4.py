# Michelle Patlan
# 8/13/2022
#Search on the internet for a way to calculate an approximation for pi. There are
#many that use simple arithmetic. Write a program to compute the approximation and then
#print that value as well as the value of math.pi from the math module.

import math

# Initialize denominator
k = 1

# Initialize sum
s = 0

for i in range(1000000):

    # even index elements are positive
    if i % 2 == 0:
        s += 4 / k
    else:

        # odd index elements are negative
        s -= 4 / k

    # denominator is odd
    k += 2

print(s)
print(math.pi)


