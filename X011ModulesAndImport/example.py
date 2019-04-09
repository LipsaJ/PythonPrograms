# print(dir())
#
# # if name starts with two underscores changed at all, so in fact there's no such thing as private
# # variables in Python and everything is available everywhere but the convention is to use underscores to
# # intention so starting a name with an underscore indicates that it's private to its module. Its up to you to
# # change it or not but python wont stop
#
# print(dir(__builtins__))
#
# for val in dir(__builtins__):
#     print(val)

import shelve  # press cntrl and click
import random

print(dir())  # at last now shelve is added as well
print(dir(shelve))

for val in dir(shelve.Shelf):
    if val[0] != '_':
        print(val)

help(shelve)
help(shelve.Shelf)
help(random)
help(random.randint)  # gives about a particular function