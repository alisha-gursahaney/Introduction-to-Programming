# Name: Alisha Gursahaney
# Net Id: amg9zd

import urllib.request


def instructor_lectures(department, instructor):
    """

    :param department: given uva department to search within
    :param instructor: given uva instructor within given department
    :return: list of all the course names for the lectures taught by the given instructor within the given department
    """
    url = 'http://arcanum.cs.virginia.edu/cs1110/files/louslist/' + department
    lous_list_website = urllib.request.urlopen(url)
    lous_list = []
    for row in lous_list_website:
        lines = row.decode('utf-8').strip().split('|')
        lous_list.append(lines)
    lous_list_website.close()
    class_list = []
    for line in lous_list:
        find1 = line[4]
        if find1.find("+") != -1:
            find1 = find1.strip("+123456789")
        if department in line[0] and instructor in line[4]:
            if line[5] == 'Lecture' and find1 == instructor:
                class_list.append(line[3])
    remove_duplicates = set(class_list)
    final_course_list = list(remove_duplicates)
    final_course_list.sort()
    return final_course_list


def compatible_classes(first_class, second_class, need_open_space=False):
    """

    :param first_class: first course to look at
    :param second_class: second course to look at
    :param need_open_space: boolean value based on enrollment and enrollment space
    :return: boolean value if 2 classes do not overlap times and can be taken together
    """
    first_days = []
    second_days = []
    department1list = first_class.split()
    first_course_num = department1list[1].split('-')
    department2list = second_class.split()
    second_course_num = department2list[1].split('-')
    first_department = department1list[0]
    second_department = department2list[0]
    url1 = 'http://cs1110.cs.virginia.edu/files/louslist/' + first_department
    url2 = 'http://cs1110.cs.virginia.edu/files/louslist/' + second_department
    lous_list_1 = urllib.request.urlopen(url1)
    lous_list1 = []
    for row in lous_list_1:
        lines = row.decode('utf-8').strip().split('|')
        lous_list1.append(lines)
    lous_list_1.close()
    lous_list_2 = urllib.request.urlopen(url2)
    lous_list2 = []
    for row2 in lous_list_2:
        lines = row2.decode('utf-8').strip().split('|')
        lous_list2.append(lines)
    lous_list_2.close()
    first_class_times = []
    second_class_times = []
    for line in lous_list1:
        if first_course_num[0] in line[1]:
            if first_course_num[1] in line[2]:
                first_days.append(line[7])
                first_days.append(line[8])
                first_days.append(line[9])
                first_days.append(line[10])
                first_days.append(line[11])
                first_class_times.append(line[12])
                first_class_times.append(line[13])
                first_class_times.append(line[15])
                first_class_times.append(line[16])
    for line2 in lous_list2:
        if second_course_num[0] in line2[1]:
            if second_course_num[1] in line2[2]:
                second_days.append(line2[7])  # monday - 0
                second_days.append(line2[8])  # tuesday - 1
                second_days.append(line2[9])  # wednesday - 2
                second_days.append(line2[10])  # thursday -3
                second_days.append(line2[11])  # friday - 4
                second_class_times.append(line2[12])  # start time - 0
                second_class_times.append(line2[13])  # end time - 1
                second_class_times.append(line2[15])  # enrollment number - 2
                second_class_times.append(line2[16])  # enrollment capacity - 3
    if first_class == second_class:
        return False
    if need_open_space:
        if first_class_times[2] >= first_class_times[3]:
            return False
        elif second_class_times[2] >= second_class_times[3]:
            return False
    for i, j in zip(first_days, second_days):
        if i == 'true':
            if j == 'true':
                if first_class_times[0] in range(int(second_class_times[0]), int(second_class_times[1])):
                    return False
                elif second_class_times[0] in range(int(first_class_times[0]), int(first_class_times[1])):
                    return False
                else:
                    return True
            else:
                return True

