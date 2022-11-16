value = int(input("Your credit amount: "))
year_2 = value / 12
year_5 = value / 60
var = value
for i in range(1, 13):
    per = var * 0.02
    var = var - year_2
    pay = per + year_2
    if i == 1:
        print("for 1 year:")
    print("{:>2} month, amount of payment = {:^10.1f}, percent = {:<2.1f}".format(i, pay, per))
var = value
for i in range(1, 61):
    if i == 1:
        print("for 5 years:")
    if i <= 24:
        per = var * 0.02
        var = var - year_5
        pay = per + year_5
        print("{:>2} month, amount of payment = {:^10.1f}, percent = {:<2.1f}".format(i, pay, per))
    else:
        per = var * 0.04
        var = var - year_5
        pay = per + year_5
        print("{:>2} month, amount of payment = {:^10.1f}, percent = {:<2.1f}".format(i, pay, per))
