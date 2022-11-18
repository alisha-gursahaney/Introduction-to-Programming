#Briana B. Morrison
#wxt4gm
#Program to determine admission rate for users based on day of week and age

def admission(day, age):
    """
    Determines admission rate for users based on parameter values according to policy
    :param day: string, day of the week
    :param age: age of visitor
    :return: string containing the admission rate, one of three values
    """
    if day == "Monday":
        return "We are closed on Monday."
    elif age < 6 or 65 < age:
        return "You get in free."

    elif day == "Tuesday" or day == "Thursday":
        return "You pay half price today!"
    elif day == "Friday":
        return "You pay full price."
    elif day == "Wednesday":
        if 13 <= age <= 20:
            return "You pay half price today!"
        else:
            return "You pay full price."
    elif day == "Saturday" or day == "Sunday":
        if 6 <= age <= 12:
            return "You pay half price today!"
        else:
            return "You pay full price."
    else:
        return "You entered an invalid day of the week."

#Testing One
print(admission("Monday", 22))  #should be closed on Monday
print(admission("Tuesday", 18))  # should be half price
print(admission("Thursday", 6)) # should be half price
#Testing Two
print(admission("Wednesday", 12)) # full price
print(admission("Wednesday", 13)) # half price
print(admission("Wednesday", 14)) # half price
print(admission("Wednesday", 19)) # half price
print(admission("Wednesday", 20)) # half price
print(admission("Wednesday", 21)) # full price
print(admission("Saturday", 50)) # full price
print(admission("Saturday", 6)) # half price
print(admission("Saturday", 7)) # half price
print(admission("Sunday", 11)) # half price
print(admission("Sunday", 12)) # half price
print(admission("Sunday", 13)) # full price
#Testing Three
print(admission("Tuesday", 5))  #free
print(admission("Friday", 6))  #full price
print(admission("Friday", 65))  #full price
print(admission("Tuesday", 66))  #free


dayOfWk = input("Please enter the day of the week: ")
age = int(input("Please enter the visitor's age: "))
result = admission(dayOfWk, age)
print(result)