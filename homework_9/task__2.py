import random
N = int(input("Write your number: "))
var = [[random.randint(1, 10) for i in range(N)] for k in range(N)]
print(var)
dgn_sum = 0
for i in range(N):
    dgn_sum += var[i][i]
var1 = [i.pop() for i in var]
print("last column numbers sum:", sum(var1))
print("sum of numbers on diagonal:", dgn_sum)

