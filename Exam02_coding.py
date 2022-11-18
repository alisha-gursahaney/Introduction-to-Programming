# Name: Alisha Gursahaney
# Net Id: amg9zd


def get_diagonal(grid):
    """

    :param grid: 2d list with length and height N
    :return: diagonal contents of grid with length N
    """
    diagonal = []
    count = 0
    for i in grid:
        count_index = i[count]
        diagonal.append(count_index)
        count += 1
    return diagonal


def sum_all(string1):
    """

    :param string1: given string full of characters and digits
    :return: the sum of the digits in the string
    """
    string_list = string1.split(",")
    if "/" in string_list:
        string_list.remove("/")
    elif "n" in string_list:
        string_list.remove("n")
    for i in range(0, len(string_list)):
        string_list[i] = int(string_list[i])
    string_sum = sum(string_list)
    return string_sum


def groceries(d, i, n):
    """

    :param d: given dictionary consisting of grocery id numbers and names
    :param i: new id number to be added to the dictionary as a key (or 0 if key already exists_
    :param n: new name to be added as the value of the id number in the dictionary
    :return: updated grocery dictionary
    """
    if i in d:
        d[0] = n
    else:
        d[i] = n
    return d

