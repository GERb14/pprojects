import random


def prime_numbers(n, z):
    for i in range(n, z):
        d = 2
        while i % d != 0:
            d += 1
        if d == i:
            yield i


end = random.randint(1, 100)
for s in prime_numbers(2, end):
    print(s, end=' ')
