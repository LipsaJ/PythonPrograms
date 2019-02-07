# Iterator and Iterable:
# Iterator is an object that represents String of Data
# so far we have come across String and List, it returns one data at  a time
# Object that supports iterator is called iterable objects

string = "0123456"

for it in string:
    print(it)

# In background iterator object is created like this
# iter_obj = iter(string)

# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))

# print(next(iter_obj)) #so when the final object is reached , iterator throws an error which is handled inbuilt
print("iterator object starts here")
for itr in iter(string):
    print(itr)


