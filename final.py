# Name: Alisha Gursahaney
# Net Id: amg9zd

def num_strings(big_list):
    """

    :param big_list: list of string lists
    :return: total number of strings in big list
    """
    numstrings = 0
    for i in big_list:
        for j in i:
            if type(j) == str:
                numstrings += 1
    return numstrings


def contacts(contact_list):
    """

    :param contact_list: list of contact details
    :return: csv file with contact details from original list
    """
    file = open('contacts.txt', 'w')
    for i in contact_list:
        for j in i:
            if j != (i[0]):
                file.write(',')
            file.write(j)
        file.write('\n')


def find_elephant(url):
    """

    :param url: given website to search
    :return: True or False depending on if the word "elephant" is within the text on the website
    """
    import re
    import urllib.request
    stream = urllib.request.urlopen(url)
    text = stream.read().decode('utf-8')
    elephant_regex = r'elephant'
    pattern = re.compile(elephant_regex, re.IGNORECASE)
    if re.search(pattern, text):
        return True
    else:
        return False


def results(file):
    """

    :param file: scores csv file to read through
    :return: a dictionary with tallies of how many wins for each team
    """
    teams = {}
    connection = open(file, 'r')
    score_string = connection.read()
    lines = score_string.strip().split('\n')
    for line in lines:
        line_list = line.split(',')
        teams[line_list[0]] = 0
        teams[line_list[2]] = 0
    for cells in lines:
        team_list = cells.split(',')
        if int(team_list[1]) > int(team_list[3]):
            teams[team_list[0]] += 1
        elif int(team_list[3]) > int(team_list[1]):
            teams[team_list[2]] += 1
    return teams


def num_orders(availability, order):
    """

    :param availability: dictionary containing the names of items and the number available
    :param order: list containing all of the food orders
    :return: how many food orders can be filled before the supply of food runs out
    """
    order_num = 0
    for i in order:
        if i in availability and availability[i] > 0:
            availability[i] -= 1
            order_num += 1
        else:
            break
    return order_num


# TESTING:
big_list_1 = [['apple', 'banana']]
print(num_strings(big_list_1))

big_list_2 = [['and', 'book'], ['car', 'dog', 'egg'], ['ear', 'go'], ['I']]
print(num_strings(big_list_2))

list1 = [['McBurney','Discord','Twitch'],['Caroline','Text','Call']]
list2 = [['Pettit','Rice 212','Morse Code']]

contacts(list1)
contacts(list2)

url_1 = 'https://en.wikipedia.org/wiki/List_of_largest_mammals'
print(find_elephant(url_1))
url_2 = 'https://en.wikipedia.org/wiki/Mouse'
print(find_elephant(url_2))

print(results('scores_1.csv'))

Availability_1 = {'El Jefe':1}
Orders_1 = ['Mayweather','El Jefe']
print(num_orders(Availability_1, Orders_1))

Availability_2 = {'El Jefe':1, 'Mayweather':5}
Orders_2 = ['El Jefe', 'El Jefe', 'Mayweather']
print(num_orders(Availability_2, Orders_2))

Availability_3 = {'El Jefe':3, 'Mayweather':1}
Orders_3 = ['El Jefe', 'El Jefe', 'Mayweather', 'Mayweather', 'El Jefe', 'Mayweather']
print(num_orders(Availability_3, Orders_3))
