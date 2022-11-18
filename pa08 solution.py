# Name: Alisha Gursahaney
# Net Id: amg9zd

def mean_all(inputList):
    """
    doc string
    :param inputList:
    :return:
    """
    total = 0
    count = 0
    for each in inputList:
        for item in each:
            total += item
            count += 1
    if count != 0:
        return total / count
    else:
        return 0


def mean_by_row(inputList):
    """
    doc string
    :param inputList:
    :return:
    """

    result = []
    for each in inputList:
        total = 0
        count = 0
        for item in each:
            total += item
            count += 1
        if count != 0:
            result.append(total / count)
        else:
            result.append(0)
    return result


def mean_by_col(inputList):
    """

    :param inputList:
    :return:
    """
    result = []
    if len(inputList) > 0:
        x = len(inputList[0])
    if x == 0:
        return result
    for index in range(x):
        total = 0
        count = 0
        for each in inputList:
            total += each[index]
            count += 1
        if count != 0:
            result.append(total / count)
        else:
            result.append(0)
    return result