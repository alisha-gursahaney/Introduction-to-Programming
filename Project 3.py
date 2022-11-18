# Name: Alisha Gursahaney
# Net Id: amg9zd

def findX (n):
    count = 0
    x = 1000
    a = 24693
    c = 3967
    k = 2 ** 18
    sum = 0

    while count < n:
        y = ((a*x) + c) % k
        u = y/k
        x = y
        count += 1
        sum += x
    return sum

def samplemean(n):
    j = 0
    sum = 0
    # while j < n:


print(findX(10)/10)