num = input("input number from 3 to 9:")
num1 = "123456789"
if num.isdigit():
    if 3 <= int(num) <= 9:
        for i in range(0, int(num)):
            var = (num1[0:i] + num1[i::-1])
            print("{:>20}".format(var))
    else:
        print("Invalid number...")
else:
    print("Wrong data...")
    #ВИРІВНЮВАННЯ ПО ЦЕНТРУ
# if num.isdigit():
#     if 3 <= int(num) <= 9:
#         for i in range(0, int(num)):
#             var = (num1[0:i] + num1[i::-1])
#             print("{:^20}".format(var))
#     else:
#         print("Invalid number...")
# else:
#     print("Wrong data...")
