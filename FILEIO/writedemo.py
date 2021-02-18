# data should be string value in writing

f = open("write.txt","w")

names = ["rifa","amy","umma","isha","ikkaka"]

for name in names:
    f.write(name+"\n")