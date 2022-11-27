import random
N = int(input("Write your number: "))
var = [[random.randint(1, 10) for i in range(N)] for k in range(N)]
print(var)
dgn_sum = 0
for i in range(N):
    for k in range(N):
        if i == k:
            dgn_sum += var[i][k]
var1 = [i.pop() for i in var]
print("last column numbers sum:", sum(var1))
print("sum of numbers on diagonal:", dgn_sum)

