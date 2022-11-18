# Name: Alisha Gursahaney
# Net Id: amg9zd

import re

time_pattern = r"([1-9]|1[0-2]):([0-5][0-9]):([0-5][0-9])\s(AM|PM)"
coursetitle_pattern = r"([A-Z]{2,4})\s([0-9]{4}):\s\".*\S.*\""

time = re.compile(time_pattern)
coursetitle = re.compile(coursetitle_pattern)
