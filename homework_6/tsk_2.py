str1 = input("string:")
chr1 = input("char:")
var = len(str1)
for i in range(0, var):
    for s in str1:
        var1 = str1.find(chr1, i, i + 1)
        if str1[var1] == chr1 and var1 != -1:
            print(var1, "-", chr1)
            break

