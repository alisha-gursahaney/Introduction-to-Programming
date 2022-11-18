# Name: Alisha Gursahaney
# Net Id: amg9zd

def get_name(movie):
    """

    :param movie: the indicated movie data
    :return: the name of the movie from the list of data
    """
    return movie[0]


def get_gross(movie):
    """

    :param movie: the indicated movie data
    :return: the gross of the movie from the list of data
    """
    return movie[1]


def get_rating(movie):
    """

    :param movie: the indicated movie data
    :return: the rating of the movie from the list of data
    """
    return movie[3]


def get_num_ratings(movie):
    """

    :param movie: the indicated movie data
    :return: the number of ratings from the list of data
    """
    return movie[4]


def better_movies(movie, lst):
    """

    :param movie: the indicated movie we want to look at
    :param lst: the list of lists of movie data
    :return: a list of movies with a better rating than the given movie
    """
    global rating
    for index in range(len(lst)):
        if movie == lst[index][0]:
            rating = lst[index][3]
    global better_movie
    better_movie = []
    for i in range(len(lst)):
        if get_rating(lst[i]) > rating:
            better_movie.append(lst[i])
    return better_movie


def average(category, lst):
    """

    :param category: a string whose value tells us what average we are computing from the movie data list
    :param lst: list of lists, where the lists inside the list comprises of a movie’s information
    :return: the computed average for the specific movie data type
    """
    if category == "rating":
        list1 = [get_rating(each_movie) for each_movie in lst]
        average1 = sum(list1) / len(list1)
        return average1
    elif category == "gross":
        list1 = [get_gross(each_movie) for each_movie in lst]
        average1 = sum(list1) / len(list1)
        return average1
    elif category == "number of ratings":
        list1 = [get_num_ratings(each_movie) for each_movie in lst]
        average1 = sum(list1) / len(list1)
        return average1

