var = [i + 1 for i in range(9, 250)]
cnt = -1
for s in var:
    cnt += 1
    if s % 20 == 0:
        var.pop(cnt)
print(var)
