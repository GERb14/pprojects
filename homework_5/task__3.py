
sum = 0
cnt = 0
min = 0
max = 0
even = 0
odd = 0
while True:
    var1 = int(input("numbers: "))
    if var1 == 0:
        break
    sum += var1
    cnt += 1
    if var1 > max:
        max = var1
    if var1 < min and var1 != 0:
        min = var1
    if var1 % 2 == 0:
        even += 1
    if var1 % 2 != 0:
        odd += 1
print("Sum of numbers :", sum, "\n"
      "Average value:", sum / cnt, '\n'
      "Min. number:", min, '\n'
      "Max. number:", max, '\n'
      "Even numbers:", even, '\n'
      "Odd numbers:", odd
      )