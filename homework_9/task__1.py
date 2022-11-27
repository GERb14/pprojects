N = int(input("Write your number: "))
var = [[i if i % 2 == 0 else s for s in range(-N, 0)] for i in range(1, N + 1)]
print(var)
