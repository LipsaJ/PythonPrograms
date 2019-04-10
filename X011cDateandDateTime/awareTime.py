import pytz
import datetime

local_time = datetime.datetime.now()
local_utc = datetime.datetime.utcnow()

print("Current time now is {}".format(local_time))
print("UTC time is {}".format(local_utc))

aware_local_time = pytz.utc.localize(local_utc).astimezone()
aware_local_utc = pytz.utc.localize(local_utc)

print("Aware local time{}, time zone: {}".format(aware_local_time, aware_local_time.tzinfo))
print("Aware utc time{}, time zone: {}".format(aware_local_utc, aware_local_utc.tzinfo))

gap_time = datetime.datetime(2015, 10, 25, 1, 30, 0, 0)
print(gap_time)
print(gap_time.timestamp())

s = 1445733000
t = s + (60 * 60)
x = s + (3000)

gb = pytz.timezone('GB')
dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb)
dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb)
dt3 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(x)).astimezone(gb)
print(s)
print(t)
print(x)

print(dt1)  # before daylight saving time
print(dt2)
print(dt3)