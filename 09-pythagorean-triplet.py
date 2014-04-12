# Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a**2 + b**2 = c*2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

goal = 1000

def run(pm, pn):
    a = b = c = 0
    m = pm
    n = pn
    while a + b + c < goal:
        m += 1

        a = m**2 - n**2
        b = 2 * m * n
        c = m**2 + n**2

    if sum([a, b, c]) == goal:
        return ([a, b, c], a * b * c)
    else:
        return run(pm + 1, pn + 1)

print run(3, 2)
