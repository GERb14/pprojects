import random


def numbers_sum(some_list, sum_of_numbers):
    my_result = False
    for aa in some_list:
        for bb in some_list:
            if aa + bb == sum_of_numbers:
                my_result = True
    return my_result


lst = [random.randint(1, 100) for i in range(1, 50)]
number = random.randint(1, 100)
result = numbers_sum(lst, number)
print(result)
