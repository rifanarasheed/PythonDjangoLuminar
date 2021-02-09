from functools import reduce

isl_2019 = [
    {"team":"mumbaicity","match_played":16,"won":10,"drawn":4,"loss":2,"goal_for":25,"goal_acquired":11,"goal_differ":14,"points":34},
    {"team":"ATK","match_played":15,"won":9,"drawn":3,"loss":3,"goal_for":20,"goal_acquired":10,"goal_differ":10,"points":30},
    {"team":"goa","match_played":16,"won":5,"drawn":8,"loss":3,"goal_for":24,"goal_acquired":19,"goal_differ":5,"points":23},
    {"team":"hyderabad","match_played":16,"won":5,"drawn":8,"loss":3,"goal_for":20,"goal_acquired":16,"goal_differ":4,"points":23},
    {"team":"northeast","match_played":16,"won":5,"drawn":8,"loss":3,"goal_for":21,"goal_acquired":20,"goal_differ":1,"points":23},
    {"team":"bengaluru","match_played":16,"won":4,"drawn":7,"loss":5,"goal_for":19,"goal_acquired":19,"goal_differ":0,"points":19},
    {"team":"jamshedpur","match_played":16,"won":4,"drawn":6,"loss":6,"goal_for":15,"goal_acquired":19,"goal_differ":-4,"points":18},
    {"team":"chennaiyin","match_played":16,"won":3,"drawn":8,"loss":5,"goal_for":11,"goal_acquired":16,"goal_differ":-5,"points":17},
    {"team":"eastbengal","match_played":16,"won":3,"drawn":7,"loss":6,"goal_for":14,"goal_acquired":21,"goal_differ":-7,"points":16},
    {"team":"keralablasters","match_played":16,"won":3,"drawn":6,"loss":7,"goal_for":20,"goal_acquired":27,"goal_differ":-7,"points":15},
    {"team":"odisha","match_played":15,"won":1,"drawn":5,"loss":9,"goal_for":14,"goal_acquired":25,"goal_differ":-11,"points":8}
]

# print number of teams present in isl
print("Total number of teams present in isl 2019 : ",len(isl_2019))

# print highest points team and lowest points team
point_list = list(map(lambda point: point["points"],isl_2019))
print(point_list)

highestpoint = reduce(lambda num1,num2: num1 if num1>num2 else num2,point_list)
print(highestpoint)

highestpointeam = list(filter(lambda team: team["points"] == highestpoint,isl_2019))
print(highestpointeam)

# highestpointeam = list(filter(lambda team: team["points"] == reduce(lambda num1,num2: num1 if num1>num2 else num2,list(map(lambda point: point["points"],isl_2019))),isl_2019))

lowestpoint = reduce(lambda num1,num2: num1 if num1<num2 else num2,point_list)
print(lowestpoint)

lowestpointteam = list(filter(lambda team: team["points"] == lowestpoint,isl_2019))
print(lowestpointteam)













