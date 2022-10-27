#1
a1 = 7
b2 = 8
c3 = a1
print(a1, b2)
a1 = b2
print(a1, b2, c3)
b2 = c3
print(a1, b2)
#2
a1, b2 = b2, a1
print(a1, b2)
#3
a1 = a1 + b2
b2 = a1 - b2
a1 = a1 - b2
print(a1, b2)
