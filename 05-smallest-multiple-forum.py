#Made use of log and prime factors for efficiency

import math

n=up=20


#Finding prime factors
a=[2]

m=3

ans=1

while m<=n:
    for i in a:
        if m%i==0:
            break
    else:
        a.append(m)
    m+=2

#all prime factors stored in a


for i in a:
    ans*=i**(int(math.log(up,i)))   # Used log to find highest power below the upper bound

#using highest power ensures that all factors of lcm are taken into consideration

print(ans)
