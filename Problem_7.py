# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

import Problem_3 as p3  # Using for isPrime


counter = 1
i = 0
while counter <= 10001:
    if p3.is_prime(i):
        counter += 1
    i += 1

print(i-1)  # -1 needed as an extra one is added to i at end of loop