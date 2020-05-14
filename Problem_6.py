# The sum of the squares of the first ten natural numbers is, 1^2+2^2+...+10^2=385. The square of the sum of the first
# ten natural numbers is, (1+2+...+10)^2=55^2=3025. Hence the difference between the sum of the squares of the first
# ten natural numbers and the square of the sum is 3025−385=2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
# Input:
# First n numbers
#
# 100

n = int(input())
# Big up A-Level maths helping me remember these
sum_of_squares = 1/6 * n * (n+1) * (2*n+1)
square_of_sums = 0.5 * n * (n+1)

print(square_of_sums**2 - sum_of_squares)