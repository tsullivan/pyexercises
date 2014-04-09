# 2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

seek = 20
n = seek
answered = False
while not answered:
	answered = True
	for i in list(reversed(range(1, seek + 1))):
		if n % i != 0:
			answered = False
			break

	if answered:
		print((n, answered))
	n = n + seek

