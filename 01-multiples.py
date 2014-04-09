end = 1000
sum = 0

while (end > 0):
        end -= 1
        current = end
        if (current % 3 == 0 or current % 5 == 0):
                sum += current

print(sum)
