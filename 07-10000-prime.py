def is_prime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return n > 1

def nth_prime(x):
    n = 1
    i = 3
    while(n < x):
        if is_prime(i):
            n += 1
        i += 2
    return i - 2

x = int(raw_input('Enter nth prime number: '))
print(nth_prime(x))
