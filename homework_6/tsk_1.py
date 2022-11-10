while True:
    var = input("Write 2 words, each from capital letter:")
    var1 = var.split()
    if len(var1) == 2 and var1[0].istitle() and var1[1].istitle():
        print(var1[0][::-1].capitalize(), var1[1][::-1].capitalize())
        break
    else:
        print("Wrong data. Change your answer")
