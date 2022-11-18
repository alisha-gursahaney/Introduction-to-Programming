# Name: Alisha Gursahaney
# Net Id: amg9zd

# books = ['calculus', 'physics', 'organic chemistry', 'history', 'literature', 'french', 'astronomy']
# orders_list = []
# orders = 0
#
# def order(books):
#     orders = 0
#     for a in books:
#         for b in books:
#             if a[0] < b[0]:
#                 for c in books:
#                     if c[0] > a[0] and c[0] > b[0]:
#                         for d in books:
#                             if d[0] > a[0] and d[0] > b[0] and d[0] > c[0]:
#                                 orders_list.append(a)
#                                 orders_list.append(b)
#                                 orders_list.append(c)
#                                 orders_list.append(d)
#                                 orders += 1
#                                 print(orders_list)
#                                 orders_list.clear()
#     print(orders)
#
# order(books)
#
# def example(books):
#     global orders
#     global orders_list
#     for a in books:
#         for b in books:
#             if a != b:
#                 for c in books:
#                     if c != a and c != b:
#                         for d in books:
#                             if d != a and d != b and d != c:
#                                 orders_list.append(a)
#                                 orders_list.append(b)
#                                 orders_list.append(c)
#                                 orders_list.append(d)
#                                 orders +=1
#                                 print(orders_list)
#                                 orders_list.clear()
#     print(orders)

# import itertools

# one_positions = set(itertools.combinations(positions, 5))
# print(one_positions)
# for each in one_positions:
#     print(each)
#     count += 1
# print(count)


# def combination(positions_list):
#     orders_list = []
#     count = 0
#     for a in positions:
#         for b in positions:
#             if b > a:
#                 for c in positions:
#                     if c > b and c > a:
#                         orders_list.append(a)
#                         orders_list.append(b)
#                         orders_list.append(c)
#                         print(orders_list)
#                         orders_list.clear()
#                         count += 1
#     print(count)
#
#
# positions = [1, 2, 3, 4, 5, 6, 7, 8]
#
# combination(positions)
# shows the positions of zeros in an 8 digit passcode

passcode = [0, 0, 0, 0, 0, 0, 0, 0]
positions = [0, 1, 2, 3, 4, 5, 6, 7]
numbers = [1, 2, 3, 4, 5, 6, 7]


# def combination(positions_list, passcode_list, numbers_list):
#     possibilities = []
#     count = 0
#     for a in positions:
#         for b in positions:
#             if b > a:
#                 for c in positions:
#                     if c > b and c > a:
#                         for d in positions:
#                             if d != a and d != b and d != c:
#                                 for one in numbers:
#                                     for e in positions:
#                                         if e != a and e != b and e != c and e != d:
#                                             for two in numbers:
#                                                 if two != one:
#                                                     for f in positions:
#                                                         if f != a and f != b and f != c and f != d and f != e:
#                                                             for three in numbers:
#                                                                 if three != one and three != two:
#                                                                     for g in positions:
#                                                                         if g != a and g != b and g != c and g != d and g != e and g != f:
#                                                                             for four in numbers:
#                                                                                 if four != one and four != two and four != three:
#                                                                                     for h in positions:
#                                                                                         if h != a and h != b and h != c and h != d and h != e and h != f and h != g:
#                                                                                             for five in numbers:
#                                                                                                 if five != one and five != two and five != three and five != four:
#                                                                                                     passcode[a] = 0
#                                                                                                     passcode[b] = 0
#                                                                                                     passcode[c] = 0
#                                                                                                     passcode[d] = one
#                                                                                                     passcode[e] = two
#                                                                                                     passcode[f] = three
#                                                                                                     passcode[g] = four
#                                                                                                     passcode[h] = five
#                                                                                                     if passcode not in possibilities:
#                                                                                                         possibilities.append(passcode)
#                                                                                                         count += 1
#                                                                                                         print(passcode)
#     for each in possibilities:
#         print(possibilities)
#
#
#     print(count)
#
#
# combination(positions, passcode, numbers)

def outcomes():
    count = 0
    passcode = [0,0,0,0,0,0,0,0]
    numbers = [1,2,3,4,5,6,7]
    positions = [0,1,2,3,4,5,6,7]
    for a in positions:
        for one in numbers:
            for b in positions:
                if b > a:
                    for two in numbers:
                        if two != one:
                            for c in positions:
                                if c > a and c > b:
                                    for three in numbers:
                                        if three != one and three != two:
                                            for d in positions:
                                                if d > a and d > b and d > c:
                                                    for four in numbers:
                                                        if four != one and four != two and four != three:
                                                            for e in positions:
                                                                if e > a and e > b and e > c and e > d:
                                                                    for five in numbers:
                                                                        if five != one and five != two and five != three and five != four:
                                                                            passcode[a] = one
                                                                            passcode[b] = two
                                                                            passcode[c] = three
                                                                            passcode[d] = four
                                                                            passcode[e] = five
                                                                            count += 1
                                                                            if count <= 100:
                                                                                print(passcode)
                                                                            passcode = [0,0,0,0,0,0,0,0]
    print(count)


import itertools
# itertools.combinations()
