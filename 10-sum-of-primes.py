from util import isPrime

def sumPrimesBelow(goal):
	primes = []
	for n in [i for i in range(2, goal)]:
		if isPrime(n):
			primes.append(n)

	print ("Number of primes less than %d: %d" % (goal, len(primes)))
	print ("Sum of primes less than %d: %d" % (goal, sum(primes)))

goal = int(input("Find the sum of all the primes below: "))
sumPrimesBelow(goal)
