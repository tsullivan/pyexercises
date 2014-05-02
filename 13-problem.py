# Work out the first ten digits of the sum of the following one-hundred
# 50-digit numbers.

numFile = open("13-input.txt", "r")
numLines = numFile.readlines()
number = 0
for i in xrange(len(numLines)):
    number += long(numLines[i])
print(str(number)[:10])
