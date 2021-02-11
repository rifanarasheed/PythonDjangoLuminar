lst = [1,2,3,4,5,6,7,8,9,10]

even_lst = [num for num in lst if num%2==0]
print(even_lst)

odd_lst = [num for num in lst if num%2!=0]
print(odd_lst)