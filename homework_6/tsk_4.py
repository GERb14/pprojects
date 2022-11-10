txt = input("Type your string, using more than 15 symbols:")
var = len(txt)
if var > 15:
    print(txt[2])
    print(txt[-2])
    print(txt[0:5])
    print(txt[0:-2])
    print(txt[0::2])
    print(txt[1::2])
    print(txt[::-1])
    print(txt[-1::-2])
    print(var)
else:
    print("There isn't enough symbols")
