import Problem_3 as p3  # Using for isPrime


counter = 1
i = 0
while counter <= 10001:
    if p3.is_prime(i):
        counter += 1
    i += 1

print(i-1)  # -1 needed as an extra one is added to i at end of loop