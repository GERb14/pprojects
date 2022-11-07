var1 = int(input("Write natural number: "))
var2 = var1
cnt = 0
while var2 > 0:
    cnt += 1
    var2 //= 10
for i in range(1, var1 + 1):
    for s in range(1, cnt + 1):
        if i == i * i % 10 ** s:
            print(i, "*", i, "=", i *1)
            break
