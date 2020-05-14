# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
#
# Input:
# The number to check up to (not including)
#
# 2000000

# A lot of primes to check, so should probably use sieve of Eratosthenes algorithm


max_num = int(input())
array = [False, False]  # This array will represent the numbers 0 -> 2,000,000, using index. We know that 0, 1 are not prime

for i in range(max_num):
    array.append(True)

for i in range(int(max_num**0.5)):
    if array[i]:
        count = 0
        j = i ** 2
        while j < max_num:
            array[j] = False
            count += 1
            j = (i ** 2) + (count * i)

total_sum = 0
for i in range(max_num):
    if array[i]:
        total_sum += i
print(total_sum)
