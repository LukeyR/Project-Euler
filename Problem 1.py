'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

Input:
Number to count up to
multiple 1
multiple 2

1000
5
3
'''


max_num = int(input())
mult1 = int(input())
mult2 = int(input())
total_sum = 0

for i in range(max_num):
    if i % mult1 == 0 or i % mult2 == 0:
        total_sum += i

print(total_sum)
