import random
lst = [random.randint(1, 10) for i in range(1, 10)]
print(lst)
print(len(set(lst)), "different numbers")
