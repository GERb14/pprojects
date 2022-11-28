import random
lst = [random.randint(1, 100) for i in range(1, 50)]
lst1 = [random.randint(1, 100) for s in range(1, 50)]
print(lst, "\n", lst1)
print(len(set(lst) & set(lst1)), "different numbers in 2 lists")
