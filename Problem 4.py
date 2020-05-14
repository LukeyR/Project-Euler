# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
# 9009 = 91 × 99. Find the largest palindrome made from the product of two 3-digit numbers.
#
# No input

# Maximum number from 2 x 3-digit numbers is 999*999
# As we want largest palindrome, count down, starting from 999*999, 999*998, ... , 998*998, 998*997, ... , 100*100


def reverse(word):
    rev_word = ""
    for k in range(len(word)):
        rev_word += word[len(word) - k - 1]
    return rev_word


max_palindrome = 0

for i in range(900):
    for j in range(900 - i):
        product = (999 - i) * (999 - j)
        if str(product) == reverse(str(product)) and product > max_palindrome:
            max_palindrome = product

print(max_palindrome)
