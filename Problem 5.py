# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# No input

# if its divisible by 20, its also divisible by 2,4,5,10, so dont check
# This works to be true for all 11-20, so only check for 11-20 divisibility and add 2520 each time (a multiple of 1-10)


def is_divisible_by_20(n):
    for i in range(11, 21):
        if n % i != 0 or n <= 0:
            return False
    return True


smallest_number = 0
while not is_divisible_by_20(smallest_number):
    smallest_number += 2520

print(smallest_number)