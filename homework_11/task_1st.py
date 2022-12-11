import random


def numbers_sum(some_list, sum_of_numbers):
    my_result = False
    for aa in range(len(some_list)):
        for bb in range(aa + 1, len(some_list)):
            if sum([some_list[aa], some_list[bb]]) == sum_of_numbers:
                my_result = True
    return my_result


lst = [random.randint(1, 100) for i in range(0, 20)]
number = random.randint(1, 100)
result = numbers_sum(lst, number)
print(result)
