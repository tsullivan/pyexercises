# This can be easily solved by using formula for sum of first n natural numbers
# or sum of squares of first n natural numbers, which are n(n+1)/2 and
# n(n+1)(2n+1)/6 respectively

n = int(input("For how many natural number the difference of sum is to be found? "))

SumSquare = n*(n+1)*(2*n+1)//6

SquareSum = (n * (n+1)//2)**2

print(SquareSum - SumSquare)

# hes my code
# i programed it myself
# im a huge fagot
numbers = range(1, n + 1)

sum_numbers = sum(numbers)
sum_squares = sum(x ** 2 for x in numbers)

result = sum_numbers ** 2 - sum_squares
print result
