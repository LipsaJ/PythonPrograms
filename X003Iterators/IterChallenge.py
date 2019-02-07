# for loop is creating iterator for us.
#
# for itb in range(0, len(string)):
#     print("The current char in string is {} ".format(itb))

days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday "]
iterForString = iter(days_list)

for itr in range(0, len(days_list)):
    print("The current day is : {}".format(next(iterForString)))

