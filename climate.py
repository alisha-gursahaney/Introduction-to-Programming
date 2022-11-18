# Name: Alisha Gursahaney
# Net Id: amg9zd

filename = input("Please enter an input file: ")

file = open(filename, "r")

file_lines = file.readlines()

for line in file_lines:
    line.split()

def calculateClimate(day1, day2):
    sum = day1 + day2
    average = sum/2
    return sum

done = calculateClimate(file_lines[5], file_lines[11])

print(done)
