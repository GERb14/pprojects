import random


def prime_numbers(n, z):
    lst = []
    for i in range(n, z):
        d = 2
        while i % d != 0:
            d += 1
        if d == i:
            lst.append(i)
    return lst


end = random.randint(1, 100)
result = prime_numbers(2, end)
print(result)
