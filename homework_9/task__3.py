import random
lst = [random.randint(1, 10) for i in range(1, 15)]
res = sum((s for s in lst if s % 2 != 0))
res1 = sum((j for j in lst if j % 2 == 0))
if res > res1:
    print("Yes")
else:
    print("No")
