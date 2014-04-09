# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import math

def is_palindrome(n):
	n_as_string = str(n)
	n_reversed = "".join(list(reversed(n_as_string)))
	return n_as_string == n_reversed

# print ("palindrome test, 9009: ", is_palindrome(9009))

pals = []
current = 100

n1 = current
n2 = current

while (n1 < 1000):
	while (n2 < 1000):
		product = n1 * n2
		n2 = n2 + 1
		if (is_palindrome(product)):
			pals.append(((n1, n2), product))
	current = current + 1
	n1 = n1 + 1
	n2 = current

products = map(lambda p: p[1], pals)
answer = max(products)
factors = filter(lambda f: f[1] == answer, pals)[0]

print (factors)
