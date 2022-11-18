# Name: Alisha Gursahaney
# Net Id: amg9zd

def fine(speed_limit, my_speed, zone="none"):
    if my_speed > speed_limit:
        if 0 < int(my_speed - speed_limit) < 20:
            if zone == "school":
                school_fine = int(my_speed - speed_limit) * 7
                return school_fine
            if zone == "work":
                work_fine = int(my_speed - speed_limit) * 7
                return work_fine
            if zone == "residential":
                residential_fine = int(my_speed - speed_limit) * 8 + 200
                return residential_fine
            else:  # defaults to zone = none
                no_zone_fine = int(my_speed - speed_limit) * 6
                return no_zone_fine
        else:  # 20 mph over the speed limit/reckless driving
            return 350
    elif my_speed == speed_limit:  # going the exact speed limit, so no fine
        return 0
    else:  # speeds below the speed limit
        slow_fine = 30
        return slow_fine


def demerits(speed_limit, my_speed):
    if my_speed > speed_limit:
        if 1 <= int(my_speed - speed_limit) <= 9:
            return 3
        elif 10 <= int(my_speed - speed_limit) <= 19:
            return 4
        elif int(my_speed - speed_limit) >= 20:
            return 6
    else:  # not speeding therefore zero demerit points (speed is equal to or less than speed limit)
        return 0
