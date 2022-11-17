value = [1, 2, 5, 7, 9, 99, 87, 200, 39, 2]
value1 = [5, 42, 29, 345, 50, 33, 7, 0, 201, 9, 2, 132, 45, 23, 934]
var = [i for i in value if i in value1]
var.sort()
cnt = -1
for s in var:
    count = cnt + 1
    if s == var[count]:
        var.remove(s)
        print(s, "- 2 times")
    else:
        print(s, "- 1 time")

