value = [1, 2, 5, 7, 9, 99, 87, 200, 39, 2]
value1 = [5, 42, 29, 345, 50, 33, 7, 0, 201, 9, 2, 132, 45, 23, 934]
var = [i for i in value if i in value1]
var1 = set(var)
for s in var1:
    if s != 2:
        print(s, "- 1 time")
    else:
        print(s, "- 2 times")
# Я не понял как доказать то, что у меня два повторения цифры 2
