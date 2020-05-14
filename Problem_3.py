# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
#
# Input:
# number to search up to
#
# 600851475143

import math as m


# Even though we are testing a large number and brute force may not be appropriate
# We only need to check up to the sqrt so brute force may be possible

# Could be made more efficient by sieve of eratosthenes, but probably not necessary in this context
def is_prime(n):
    if n <= 1:  # Needed as sqrt(4) = 2 so for loop will not enter
        return False
    if n == 2:  # Needed as sqrt(3) < 2 so for loop will not enter
        return True
    for k in range(2, int(m.sqrt(n))+1):
        if n % k == 0:
            return False
    return True

if __name__ == "__main__":
    max_num = int(input())

    for i in range(sqrt := int(m.sqrt(max_num))):
        if max_num % (sqrt - i) == 0 and is_prime(sqrt - i):
            print(sqrt - i)
            break
