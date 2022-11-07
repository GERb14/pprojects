var1 = int(input("Enter a year: "))
if 1900 < int(var1) < 1_000_000:
    if var1 % 4 == 0 and var1 % 100 != 0:
        print(var1, "is a leap year")
    elif var1 % 400 == 0:
        print(var1, "is a leap year")
    else:
        print(var1, "isn't a leap year")
else:
    print("Selected year doesn't match the condition")
