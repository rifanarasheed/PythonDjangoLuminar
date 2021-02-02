# need each states confirmed cases from covid_19_india dataset

covid = open("covid_19_india.csv","r")         # file reading

dict = {}                                      # created an empty dictionary to get count of confirmed cases of each state

# key   value
# state confirmed

for line in covid:                             # reading each line and splitting each word by ,
    data = line.rstrip("\n").split(",")
    # only needed state and confirmed cases
    state = data[3].rstrip("***")              # removing *** from states having ***
    if(state == "Telengana"):                     # there is telengana and telengane, so both are taken as two state
        state = "Telangana"
    confirmed_cases = int(data[8])
    if(state not in dict):                     # if state key is not present in the dict , that key is present with its corresponding case, not 1
        dict[state] = confirmed_cases
    else:
        dict[state] = confirmed_cases          # if the state key is present, then update the confirm case.

for key,value in dict.items():                 # print the dict where state is key and confirmed cases are value
    print(key,"---->",value)

# to get state which has highest confirmed cases ( sort )
# key = dict.get --> to get all values. to get specific value,we need to specify it in ()
# reverse = True , to get highest value
result = sorted(dict,key = dict.get,reverse= True)
print(result)

# to print in alphabetic order
# result = sorted(dict)

# to get highest confirmed state
print(result[0],dict.get(result[0]))              # to get 1st state of list as well as its value.
