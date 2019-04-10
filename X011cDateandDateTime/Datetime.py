import time
print("The epoch time on this system is :" + time.strftime('%c', time.gmtime(0)))
print("Current timezone is {0} with an offset of {1}".format(time.tzname[0], time.timezone))

if time.daylight != 0:
    print("Day light saving time is in effect of this location")
    print("The DST timezone is " + time.tzname[1])

print("The local time is "+ time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print("The UTC time is "+ time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime()))

print()
print("#########################DateTime##################")
print()
import datetime

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())