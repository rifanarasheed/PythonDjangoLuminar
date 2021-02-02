# nesteddict

covid = open("covid_19_india.csv","r")

covid_dict = {}

for lines in covid:
    data = lines.rstrip("\n").split(",")
    state = data[3]
    cure = data[7]
    confirmed = data[8]
    if state not in covid_dict:
        covid_dict[state] = {"state":state,"cured":cure,"confirmed":confirmed}
    else:
        covid_dict[state] = {"state": state,"cured": cure,"confirmed": confirmed}
print(covid_dict)

def print_data(**kwargs):
    state = kwargs["state"]
    if state in covid_dict:
        print("state :",covid_dict[state]["state"])
        print("cured : ",covid_dict[state]["cured"])
        if "prop" in kwargs:
            prop = kwargs["prop"]
            print("confirmed :",covid_dict[state][prop])
        else:
            pass
    else:
        print("state doesnot exist")

print_data(state='Kerala', prop="confirmed")