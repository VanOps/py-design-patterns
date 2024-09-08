#!/usr/bin/python3

def iterate(my_list):
    list_iter = my_list.__iter__()
    list_length = len(my_list)
    while list_length > 0:
        print(list_iter.__next__())
        list_length -= 1


def list_comprehension(my_list):
    new_list = [x for x in my_list]
    print(new_list)


def list_comprehension_with_condition(my_list):
    new_list = [x for x in my_list if x % 2 == 0]
    print(new_list)


def list_comprehension_with_nested_condition(my_list):
    new_list = [x for x in my_list if x % 2 == 0 if x > 2]
    print(new_list)


def list_comprehension_with_nested_loop(my_list):
    new_list = [(x, y) for x in my_list for y in my_list]
    print(new_list)


def list_comprehension_with_matrix(my_matrix):
    print('Prints double of the first column of the matrix')
    new_list = [row[0]*2 for row in my_matrix]
    print(new_list)


if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    iterate(my_list)
    list_comprehension(my_list)
    list_comprehension_with_condition(my_list)
    list_comprehension_with_nested_condition(my_list)
    list_comprehension_with_nested_loop(my_list)
    list_comprehension_with_matrix(my_matrix)