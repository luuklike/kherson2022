import random as ganyu

aliexpress = []

sumpair = 0
sumnonpair = 0
sumnegative = 0
sumpositive = 0
res = 1
res1 = 1
res2 = 0

aliexpress = [ganyu.randint(-50,100) for i in range(1,18)]

print(aliexpress)

for i in aliexpress:

    if (i%2) == 0:

        sumpair += i

for b in aliexpress:

    if (b % 2) == 0:
        continue
    sumnonpair += b

for s in aliexpress:

    if s > 0:

        sumpositive += s

for u in aliexpress:

    if u < 0:

        sumnegative += u

for r in aliexpress:

    if r < 0:

        sumnegative += r

for h in range(len(aliexpress)):
    if h % 3 == 0 and i != 0:
        res *= aliexpress[h]

for n in range(len(aliexpress)):
    if n > 0 == 0 and n < 17:
        res2 += aliexpress[n]

for m in range(len(aliexpress)):
    macs = 0
    macs = max(aliexpress)
    meen = 0
    meen = min(aliexpress)
    res1 *= aliexpress[m]
print(sumpair)
print(sumnonpair)
print(sumpositive)
print(sumnegative)
print(res)
print(res1)
print(res2)