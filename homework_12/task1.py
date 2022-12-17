import random


def decorator_func(func):
    def wrapper(*args, **kwargs):
        multiple_3 = "кратне 3"
        nomultiple_3 = "не кратне 3"
        even = "парне"
        odd = "не парне"
        for i in func(*args, **kwargs):
            if i % 3 == 0 and i % 2 == 0:
                print("{:^10} {:<15} {:<10}".format(i, multiple_3, even))
            if i % 3 == 0 and i % 2 != 0:
                print("{:^10} {:<15} {:<10}".format(i, multiple_3, odd))
            if i % 3 != 0 and i % 2 != 0:
                print("{:^10} {:<15} {:<10}".format(i, nomultiple_3, odd))
            if i % 3 != 0 and i % 2 == 0:
                print("{:^10} {:<15} {:<10}".format(i, nomultiple_3, even))
        return
    return wrapper


@decorator_func
def set_func(amount_of_numbers):
    my_set = {random.randint(1, 100) for s in range(0, amount_of_numbers)}
    return my_set


print(set_func(3))
