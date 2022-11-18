# Name: Alisha Gursahaney
# Net Id: amg9zd

current_value = 0
recent_operation = ""
recent_argument = 0
current_calculation = "0"


#  global variable names chosen based on descriptive words used in directions to keep thoughts organized

def get_value():
    """

    :return: the updated global variable
    """
    return current_value


def clear(integer=0):
    """

    :param integer: optional argument used to change the current value and calculation values (only relevant to clear function)
    :return: clears the operation and argument global variables and sets the current value and calculations to the argument
    """
    global current_value
    global recent_operation
    recent_operation = ""
    global recent_argument
    recent_argument = 0
    global current_calculation
    current_value = integer
    current_calculation = f"{integer}"
    return integer


def repeat():
    """

    :return: repeats the step function using the same arguments
    """
    if recent_operation == "":
        return current_value
    else:
        return step(recent_operation, recent_argument)


def get_expr():
    """

    :return: shows the expanded expression of the calculation specified
    """
    if recent_operation == "":
        return f"{current_value}"
    else:
        return current_calculation


def step(operator="", argument=0):
    """

    :param operator: temporary argument used to change the global operator variable at the end of the function
    :param argument: temporary argument used to change the global argument variable at the end of the function
    :return: the calculation of the updated global variables (calculating the repeated global calculation)
    """
    global current_value

    def helper():
        """

        :return: the previous expression stored into the current calculation variable
        """
        global current_calculation
        value = f"({current_calculation}){str(operator)}{argument}"
        current_calculation = value
        return current_calculation

    #  storing expressions in current calculation variable so expressions will show in calculations instead of only the evaluated integer
    helper()
    if operator == "+":
        calculate = int(current_value) + int(argument)
        current_value = calculate
    elif operator == "-":
        calculate = int(current_value) - int(argument)
        current_value = calculate
    elif operator == "*":
        calculate = int(current_value) * int(argument)
        current_value = calculate
    elif operator == "//":
        calculate = int(current_value) // int(argument)
        current_value = calculate
    global recent_operation
    recent_operation = operator
    global recent_argument
    recent_argument = argument
    return current_value
