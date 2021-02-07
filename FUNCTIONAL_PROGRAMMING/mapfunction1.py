# if num<5 then num-1 and if num>5 then num+1
lst1 = [1,2,3,4,6,8,9]

def sub(num):
    if (num<5):
        return num-1
    else:
        return num+1
res_lst = list(map(sub,lst1))
print(res_lst)

# when using lambda function, we use ternary operation to concise the code
# the result when if statement is correct should be given then if condition then else statements
res_lst1 = list(map(lambda num: num-1 if num<5 else num+1,lst1))         # do num-1 if num is less than 5 else do n+1
print(res_lst1)

# if num<5 then num-1 and if num>5 then num+1 and if num=5,print num
lst2 = [1,2,3,4,5,6,8,9]
#def sub(num):
#    if (num<5):
#        return num-1
#    else:
#        if (num>5):
#            return num+1
#        else:
#           num

res_lst2 = list(map(lambda num: num-1 if num<5 else num+1 if num>5 else num,lst2))        # do num-1 if num is less than 5 else do num+1 if num is greater than 5 else num
print(res_lst2)