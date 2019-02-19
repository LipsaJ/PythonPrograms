# Imelda = "More Mayhem", "Mayhem May", "2011", {
#     (1, "Pulling the rug"), (2, "Some New Song")}
#
# with open("Imelda.txt", "w") as imelda_file:
#     print(Imelda, file=imelda_file )

with open("Imelda.txt", "r") as imelda_file:
    contents = imelda_file.readline()

imelda = eval(contents)

print(imelda)
artist, album, year, tracks = imelda
print(artist)
print(album)
print(year)
print(tracks)
