import pytz
import datetime

# for x in pytz.all_timezones:
#     print(x)

timezoneDict = {"a": "GB",
                "b": "UTC",
                "c": "EST",
                "d": "GMT"}


for i in timezoneDict:
    print(i + " : "+  timezoneDict.get(i))

val = input("Please select a timezone :")

local_time = datetime.datetime.now()
local_utc = datetime.datetime.utcnow()

gb = pytz.timezone(timezoneDict.get(val))

aware_local_time = pytz.utc.localize(local_utc).astimezone(gb)

print("Current time in India is {}".format(local_time))
print("Current time in {} is {}".format(timezoneDict.get(val), aware_local_time))
