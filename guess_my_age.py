# Name: Alisha Gursahaney
# Net Id: amg9zd

number = int(input("Pick a number between 1 and 10: "))
birthday_this_year = int(input("If you've already had a birthday this year, enter 1771. Otherwise, enter 1770: "))
birth_year = int(input("Enter the year that you were born: "))

magic_number = (((number * 2) + 5) * 50) + birthday_this_year - birth_year

age = magic_number - (100 * number)

print(f'The magic number is "{magic_number}". That means you are {age}! ')

