var = input("Write a sentence, using more than 2 words:")
var1 = var.split(" ")
var1.sort()
if var.count(" ") >= 2:
    for i in range(var1.count("")):
        var1.remove("")
var2 = len(var1)
cnt = -1
if var2 > 2:
    for s in var1:
        cnt += 1
        print("index - {:^5}; word - {:^5}".format(cnt, s))
    print(var2, "words")
else:
    print("Wrong data. Not enough words")
