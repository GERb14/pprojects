var1 = input("Write your number: ")
var2 = 0
cnt = 0
for i in var1:
    cnt += 1
    for s in var1:
        if s == i:
            var2 += 1
if var2 != cnt:
    print("Yes")
else:
    print("No")
