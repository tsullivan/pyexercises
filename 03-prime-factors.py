# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
import math

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif (n % 2 == 0):
        return False
    else:
        sqr = int(math.sqrt(n)) + 1
        for divisor in range(3, sqr, 2):
            if n % divisor == 0:
                return False
        print("prime: ", n)
        return True

def prime_factors(n):
      return [i for i in range(1, n + 1) if n % i == 0]

print ("setup answer: ", max(prime_factors(13195)))
print ("challenge answer: ", max(prime_factors(600851475143)))
