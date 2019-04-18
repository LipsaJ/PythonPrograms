import sqlite3
import tkinter


conn = sqlite3.connect('music.sqlite')

for x in conn.execute("SELECT albums.name FROM albums WHERE albums.artists = ? ORDER BY albums.name", (196, )):
    print(x)
