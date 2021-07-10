import os

rootdir = "d:\music"
songsList = []

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        #print (os.path.join(subdir, file))
        #print ((file.rsplit(".",1))[0])
        songsList.append ((file.rsplit(".",1))[0])

with open('D:\music\SongsList.txt', 'w', encoding="utf-8") as f:
    for song in songsList:
        f.write("%s\n" % song)

