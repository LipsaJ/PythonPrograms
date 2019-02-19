import pickle
# pickle is the concept of serialization like java. That's a process that allows objects to be saved to a file.
# So that they can be stored or restored I should say from the file later. Now python provides a mechanism for
# serializing objects called pickling. Hence the word pickle. So when and object is pickled and it's written to
# a file and format that contains the objects data together with sufficient information to allow that object to
# be recreated when it's loaded back in.

# Imelda = ("More Mayhem",
#           "Mayhem May",
#           "2011",
#           ((1, "Pulling the rug"),
#            (2, "Pyscho"),
#            (3, "Mayhem"),
#            (4, "Kentish Town waltz")))
#
# with open("Imelda.pickle", "wb") as pickle_file:
#     pickle.dump(Imelda, pickle_file)

# with open("Imelda.pickle", "rb") as pickled_file:
#     imelda2 = pickle.load(pickled_file)
#
# print(imelda2)
#
# artist, name, year, album = imelda2
#
# for songs in album:
#     number, song = songs
#     print("number {} : song is {} ".format(number, song))

# we can do for more objects!
#
# Imelda = ("More Mayhem",
#           "Mayhem May",
#           "2011",
#           ((1, "Pulling the rug"),
#            (2, "Pyscho"),
#            (3, "Mayhem"),
#            (4, "Kentish Town waltz")))
#
# even = range(0, 10, 2)
# odd = range(1,10,2)
#
# with open("Imelda.pickle", "wb") as pickle_file:
#     pickle.dump(Imelda, pickle_file)
#     pickle.dump(even, pickle_file)
#     pickle.dump(odd, pickle_file)
#     pickle.dump(223456, pickle_file)

with open("Imelda.pickle", "rb") as pickled_file:
    imelda2 = pickle.load(pickled_file)
    evenlist = pickle.load(pickled_file)
    oddlist = pickle.load(pickled_file)
    x_var = pickle.load(pickled_file)

print(imelda2)

artist, name, year, album = imelda2

for songs in album:
    number, song = songs
    print("number {} : song is {} ".format(number, song))

print(evenlist)
print(oddlist)
print(x_var)

# object must be read back in the same order they are pickeled
