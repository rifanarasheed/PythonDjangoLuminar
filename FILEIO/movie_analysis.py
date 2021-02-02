# to print number of movie release of each year
# to print year which has highest movie release

movie = open("movies.csv","r")

dict = {}

for line in movie:
    data = line.rstrip("\n").split(",")
    # ['1', 'The Nightmare Before Christmas', '1993', '3.9', '4568']
    year = data[2]
    release_no = data[4]
    if(year not in dict):
        dict[year] = release_no
    else:
        dict[year] = release_no

for key,value in dict.items():
    print(key,"-->",value)

# to sort highest release year
result = sorted(dict,key=dict.get,reverse=True)
print(result)
print(result[0],"-->",dict.get(result[0]))
