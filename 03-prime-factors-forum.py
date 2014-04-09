"indienchild"
# Python, pretty simple, no need for modulos!
def largestPrimeFactor(N):
	k = 2
	while (k < N):
		while (N/k*k == N):
			N = N/k
		k += 1
	return k
print largestPrimeFactor(600851475143)
