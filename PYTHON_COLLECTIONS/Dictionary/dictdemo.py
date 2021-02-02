# define : {}
# values stored in dictionary in the form key value pair
# to fetch value from dictionary : use key
# not possible to store duplicate key as key must be unique.
# key error will arise if we try to access wrong key

expenses = {"jan":3000,"feb":2500,"march":500}
print(expenses["march"])

# to check whether a key is present in the dict or not
print("june" in expenses)
print("jan" in expenses)

# to add new key value dictionary
# april = 600
expenses["april"] = 600
print(expenses)

# to change value in key
expenses["april"]-=200
print(expenses["april"])