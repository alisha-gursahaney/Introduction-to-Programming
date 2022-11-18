# Name: Alisha Gursahaney
# Net Id: amg9zd

def gellish2(age):
    """

    :param age: age (in years)
    :return: maximum heart rate at that age (in beats per minute)
    """
    HRmax = float(191.5 - 0.007 * (age ** 2))
    return HRmax


def in_target_range(hr, age):
    """

    :param hr: heart rate (in beats per minute)
    :param age: age (in years)
    :return: if the heart rate is within (or exactly at a boundary of) the target range based on the given age (bool)
    """
    min = float(0.65 * gellish2(age))
    max = float(0.85 * gellish2(age))
    x = bool(min <= hr <= max)
    return x
