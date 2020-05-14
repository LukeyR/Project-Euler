'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
Input:
Item 1 of Fibonacci list
Item 2 of Fibonacci list

1
2
'''


fib_list = []

a = int(input())
b = int(input())
fib_list.append(a)
fib_list.append(b)

total_sum = 0
while b < 4000000:
    if b < 4000000 and b % 2 == 0:
        total_sum += b
    b += a
    a = b - a

print(total_sum)
