import random
numbers = [random.randint(1, 5) for i in range(20)]
numbers1 = [random.randint(1, 5) for s in range(20)]
number_in_degree = lambda x, y = 2: x ** y
print(list(map(number_in_degree, numbers)))
print(list(map(number_in_degree, numbers, numbers1)))