var1 = input("The amount of pupils in 1st class: ")
var2 = input("The amount of pupils in 2st class: ")
var3 = input("The amount of pupils in 3st class: ")
res1 = ((int(var1) % 2) + int(var1)) // 2
res2 = ((int(var2) % 2) + int(var2)) // 2
res3 = ((int(var3) % 2) + int(var3)) // 2
sum = res1 + res2 + res3
print(sum, "desks")

#         + int(var2) + int(var3)) // 2
# res2 = (int(var1) + int(var2) + int(var3)) % 2
# if res2 == 1:
#     print(res1 + 1)
# else:
#     print(res1)
    