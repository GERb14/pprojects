def longest_words(file):
    my_file = open(file, 'r', encoding='utf-8')
    my_file1 = my_file.read().replace('\"', ' ').split()
    lst2 = [len(i) for i in my_file1]
    for j in range(len(my_file1)):
        if lst2[j] == max(lst2):
            print("{:>10}".format(my_file1[j], emd=' '))
    return


if __name__ == '__main__':
    longest_words('article.txt')

