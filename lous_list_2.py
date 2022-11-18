# Name: Alisha Gursahaney
# Net Id: amg9zd

import urllib.request

def instructor_lectures(department, instructor):
    """
    This function will return a list of all the course names for
    the lectures taught by a given instructor within the given
    department, but not repeated courses if they are at different times

    :param department: the department that the classes are categorized
    under

    :param instructor: the name of the professor of each course
    :return:
    """
    link = 'http://arcanum.cs.virginia.edu/cs1110/files/louslist/' + department
    s = urllib.request.urlopen(link)
    list1 = []
    linklist = []
    for row in s:
        row = row.decode('utf-8')
        cells = row.strip().split('|')
        linklist.append(cells)
    s.close()

    for each in linklist:
        if instructor in each[4] and each[5] == "Lecture":
            if each[3] not in list1:
                list1.append(each[3])
    return list1

def compatible_classes(first_class, second_class, needs_open_space=False):
    """
    This function will return True if the the two classes given
    are compatible within the same schedule and return False if not.
    Additionally, if the third parameter is True then the function
    will automatically return False.

    :param first_class: the first course given by abbreviation and course numbers

    :param second_class: the second course given by abbreviation and course number

    :param needs_open_space: a True or False value given based on class capacity
    :return:
    """
    if first_class == second_class:
        return False

    firstdept = first_class.split(" ")
    depttitle = firstdept[0]

    secdept = second_class.split(" ")
    depttitle2 = secdept[0]

    link1 = 'http://arcanum.cs.virginia.edu/cs1110/files/louslist/' + depttitle

    link2 = 'http://arcanum.cs.virginia.edu/cs1110/files/louslist/' + depttitle2

    s = urllib.request.urlopen(link1)
    list1 = []
    class1 = []
    for row in s:
        row = row.decode('utf-8')
        cells = row.strip().split('|')
        class1.append(cells)
    s.close()

    t = urllib.request.urlopen(link2)
    list2 = []
    class2 = []
    for row in t:
        row = row.decode('utf-8')
        cells = row.strip().split('|')
        class2.append(cells)
    t.close()

    classnums = firstdept[1].split('-')
    prenum1 = classnums[0]
    classnum1 = classnums[1]
    # print(classnums)

    classnums2 = secdept[1].split('-')
    prenum2 = classnums2[0]
    classnum2 = classnums2[1]

    classes_compat = True

    for each in class1:
        for each2 in class2:
            if each[1] == prenum1 and each[2] == classnum1:
                if each2[1] == prenum2 and each2[2] == classnum2:
                    # print(each[12], each[13], each2[12], each2[13])
                    if needs_open_space == True:
                        if int(each[15]) >= int(each[16]) or int(each2[15]) >= int(each2[16]):
                            classes_compat = False
                    for i in range(7, 12):
                        if each[i] == each2[i]:
                            if each[12] <= each2[12] <= each[13]:
                                classes_compat = False
                            elif each2[12] <= each[12] <= each2[13]:
                                classes_compat = False
                            elif each[12] <= each2[13] <= each[13]:
                                classes_compat = False
                            elif each2[12] <= each[13] <= each2[13]:
                                classes_compat = False
    return classes_compat
