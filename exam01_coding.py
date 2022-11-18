# Name: Alisha Gursahaney
# Net Id: amg9zd

def show_one_higher():
    """

    :return: the user's input value plus one
    """
    x = input("Enter a number: ")
    y = int(x) + 1
    return f"One more than {x} is {y}."


def roll_two(x, y):
    """

    :param x: first roll of two dice
    :param y: second roll of two dice
    :return: the result depending on the value of the dice
    """
    if x == y:
        return "YOU WIN"
    elif ((x + y) % 2) == 0:
        return x + y
    else:
        return x * y


def initials(first, last, middle="x"):
    """

    :param first: first name
    :param last: last name
    :param middle: middle name
    :return: initials from a person's full name
    """
    f = first.lower()
    L = last.lower()
    m = middle.lower()
    if middle != "x":
        return f[0] + m[0] + L[0]
    else:
        return f[0] + m + L[0]

