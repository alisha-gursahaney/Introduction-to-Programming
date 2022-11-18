# Name: Alisha Gursahaney
# Net Id: amg9zd


List = ['Turkey','Turkey-G',
        'Mashed', 'Mashed-G',
        'Dressing', 'Dressing-G',
        'Green', 'Green-G',
        'Corn', 'Corn-G',
        'Cranberry Sauce',
        'Sweet potato casserole',
        'Cornbread', 'Cornbread-G',
        'Macaroni and Cheese']

List2 = ['Turkey',
        'Mashed',
        'Dressing',
        'Green',
        'Corn',
        'Cranberry Sauce',
        'Sweet potato casserole',
        'Cornbread',
        'Macaroni and Cheese']


from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))



# driver code
# n = 0
# for i in list(powerset(List)):
#     if 'Turkey' in i and 'Turkey-G' in i:
#         n += 0
#     elif 'Mashed' in i and 'Mashed-G' in i:
#         n += 0
#     elif 'Dressing' in i and 'Dressing-G' in i:
#         n += 0
#     elif 'Green' in i and 'Green-G' in i:
#         n += 0
#     elif 'Corn' in i and 'Corn-G' in i:
#         n += 0
#     elif 'Cornbread' in i and 'Cornbread-G' in i:
#         n += 0
#
#     else:
#         print(i)
#         n += 1
#
# print(n)

y = 0
for j in list(powerset(List2)):
    if 'Corn' in j and 'Cornbread' in j:
        y += 0
    else:
        print(j)
        y += 1
print(y)

# for j in templist:
#     if 'Turkey' and 'G-Turkey' in templist[j]:
#         n += 0
#     elif 'Mashed Potatoes' and 'G-Mashed' in templist[j]:
#         n += 0
#     elif 'Dressing' and 'G-Dressing' in templist[j]:
#         n += 0
#     elif 'Green Beans' and 'G-Green' in templist[j]:
#         n += 0
#     elif 'Corn' and 'G-Corn' in templist[j]:
#         n += 0
#     elif 'Cornbread' and 'G-Cornbread' in templist[j]:
#         n += 0
#     else:
#         finallist.append(templist)
#         n += 1




