import time
#
# print(time.gmtime(0))  # this is the epoc time 1970 when , before that it takes negetive
# print(time.localtime())  # this is current time
# print(time.time())  # time in seconds, number of seconds since epoch which is 00:00 01-01-1970
#

# how to create our own tuples, its similar to normal tuples


time_here = time.localtime()
print(time_here)
print("Year: ", time_here[0], time_here.tm_year)
print("Month: ", time_here[1], time_here.tm_mon)
print("Day: ", time_here[2], time_here.tm_mday)
