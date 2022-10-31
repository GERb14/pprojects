var1 = [0000, 1111, 1234, 4321, 9999]
var2 = input("Enter your password: ")
if int(var2) in var1:
    print("Correct")
else:
    print("Access denied. Your password is incorrect")
