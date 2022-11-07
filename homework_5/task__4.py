var = int(input("Write your number: "))

for i in range(var):
    i *= i
    if i > var:
        break
    if i != 0:
        print(i, end= " ")
    if var == 1:
        print(var)