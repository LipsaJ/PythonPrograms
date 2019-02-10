imelda = "More Mayhem", "Imelda May", 2011, {
    (1, "Pulling the rug"),
    (2, "Psycho"),
    (3, "Mayhem"),
    (4, "Kentish town")}

title, artist, year, album = imelda
print(title)
print(artist)
print(year)

for i in album:
    # print("\t"),
    # print(i)
    # that also works
    # print('\t',i)

    track_number, song = i
    print("\t"),
    print("Track number is {} and song is {}".format(track_number, song))

    # so tupple is imuttable it cant be changed but if a tuple contains a list that can be changed/appended
    # example in chapter 49
