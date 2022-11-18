# Name: Alisha Gursahaney
# Net Id: amg9zd

import math


def randomNumGenerator(count):
    x_0, a, c, k, u = 1000, 24693, 3967, 2 ** 18, 0
    randList = []
    for i in range(103404, 213410):
        x_0 = (a * x_0 + c) % k
        u = round(x_0 / k, 4)
        randList.append(u)
    return randList[count]


# when n = 10
# print("when n = 10")
# print("")
# position = 0
# estNum = 0
# for j in range(110):
#      finalSum = 0
#      for i in range(10):
#         finalSum += (-6498 * math.log(1 - randomNumGenerator(position)))**(1/2)
#         position += 1
#     estNum += 1
#     average = round(finalSum / 10, 4)
#     # print("estimate " + str(estNum) + ": " + str(average))
#     print(average)

# print(" ")

# # when n = 30
# print("when n = 30")
# print(" ")
# position = 1101
# estNum = 0
# for j in range(110):
#     finalSum = 0
#     for i in range(30):
#         finalSum += (-6498 * math.log(1 - randomNumGenerator(position)))**(1/2)
#         position += 1
#     estNum += 1
#     average = round(finalSum / 30, 4)
#     # print("estimate " + str(estNum) + ": " + str(average))
#     print(average)
#
# print(" ")
#
# # when n = 50
# print("when n = 50")
# print(" ")
# position = 4402
# estNum = 0
# for j in range(110):
#     finalSum = 0
#     for i in range(50):
#         finalSum += (-6498 * math.log(1 - randomNumGenerator(position))) ** (1 / 2)
#         position += 1
#     estNum += 1
#     average = round(finalSum / 50, 4)
#     # print("estimate " + str(estNum) + ": " + str(average))
#     print(average)

# print(" ")
#
# # when n = 100
# print("when n = 100")
# print(" ")
# estNum = 0
# position = 9903
# for j in range(110):
#     finalSum = 0
#     for i in range(100):
#         finalSum += (-6498 * math.log(1 - randomNumGenerator(position)))**(1/2)
#         position += 1
#     estNum += 1
#     average = round(finalSum / 100, 4)
#     # print("estimate " + str(estNum) + ": " + str(average))
#     print(average)

print(" ")

# # when n = 250
# print("when n = 250")
# print(" ")
# estNum = 0
# position = 20904
# for j in range(110):
#     finalSum = 0
#     for i in range(250):
#         finalSum += (-6498 * math.log(1 - randomNumGenerator(position)))**(1/2)
#         position += 1
#     estNum += 1
#     average = round(finalSum / 250, 4)
#     # print("estimate " + str(estNum) + ": " + str(average))
#     print(average)

# print(" ")
#
# when n = 500
print("when n = 500")
print(" ")
# position = 48404
position = 0
estNum = 0
for j in range(110):
    finalSum = 0
    for i in range(1000):
        finalSum += (-6498 * math.log(1 - randomNumGenerator(position)))**(1/2)
        position += 1
    estNum += 1
    average = round(finalSum / 1000, 4)
    # print("estimate " + str(estNum) + ": " + str(average))
    print(average)

# print(" ")
#
# # when n = 1000
# print("when n = 1000")
# print(" ")
# estNum = 0
# # position = 103404
# position = 1
# for j in range(110):
#     finalSum = 0
#     for i in range(1000):
#         finalSum += (-6498 * math.log(1 - randomNumGenerator(position)))**(1/2)
#         position += 1
#     estNum += 1
#     average = round(finalSum / 1000, 4)
#     print("estimate " + str(estNum) + ": " + str(average))
#     print(average)
#
#
