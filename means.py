# Name: Alisha Gursahaney
# Net Id: amg9zd

def mean_all(table):
    """

    :param table: list of lists of numbers
    :return: arithmetic mean of all the numbers in the table
    """
    sum_of_table = 0
    num_of_values = 0
    for i in table:
        for j in i:
            sum_of_table += j
            num_of_values += 1
    return sum_of_table/num_of_values


def mean_by_row(table):
    """

    :param table: list of lists of numbers
    :return: a list containing the arithmetic means of each row's values
    """
    mean_list = []
    for i in table:
        row_sum = 0
        row_num = 0
        for j in i:
            row_sum += j
            row_num += 1
        row_mean = row_sum/row_num
        mean_list.append(row_mean)
    return mean_list


def mean_by_col(table):
    """

    :param table: list of lists of numbers
    :return: a list containing the arithmetic means of each column's values
    """
    col_table = []
    for i in range(len(table[0])):
        col_list = []
        col_list.clear()
        for j in table:
            col_list.append(j[i])
        col_table.append(col_list)
    col_mean = mean_by_row(col_table)
    return col_mean
