rng = input("input your number:")
cnt_2 = 0.1
if rng.isdigit():
    for cnt in range(-1, int(rng)):
        cnt += 1
        cnt_2 *= 10
        print("{:>5} {:>20}".format(cnt, "%.i" % cnt_2))
else:
    print("Wrong data. Write a natural number")


