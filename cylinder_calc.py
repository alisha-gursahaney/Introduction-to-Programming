# Name: Alisha Gursahaney
# Net Id: amg9zd
# Partner: Nathaniel Gleberman Njg7hy
# Breakout room 40

# Define value of pi
pi = 3.14

# Cylinder statistic calculation functions
def surface_area(R,H):
    """

    :param R: cylinder radius
    :param H: cylinder height
    :return: cylinder surface area (units squared)
    """
    x = (2 * pi * R * H) + (2 * pi * R * R)
    x = round(x, 2)
    return x

def volume(R,H):
    """

    :param R: cylinder radius
    :param H: cylinder height
    :return: cylinder volume (units cubed)
    """
    y = pi * R * R * H
    y = round(y, 2)
    return y

def lateral_area(R,H):
    """

    :param R: cylinder radius
    :param H: cylinder height
    :return: cylinder lateral area (units squared)
    """
    z = 2 * pi * R * H
    z = round (z, 2)
    return z

def base_area(R,H):
    """

    :param R: cylinder radius
    :param H: cylinder height
    :return: cylinder base area (units squared)
    """
    a = pi * R * R
    a = round(a, 2)
    return a

# function for printing all statistics
def print_cylinder(R,H):
    """

    :param R: cylinder radius
    :param H: cylinder height
    :return: print cylinder statistics with all 4 calculations
    """
    Radius = print(f"Radius: {R}")
    Height = print(f"Height: {H}")
    S = print(f"Surface Area: {surface_area(R,H)}")
    V =print(f"Volume: {volume(R,H)}")
    L = print(f"Lateral Area: {lateral_area(R,H)}")
    B = print(f"Base Area: {base_area(R,H)}")
    return (Radius,Height,S,V,L,B)

print_cylinder(3,4)

# how I would have printed without a 5th function:
# print(f"Surface Area: {surface_area(3,4)} \nVolume: {volume(3,4)} \nLateral Area: {lateral_area(3,4)} \nBase Area: {base_area(3,4)}")
