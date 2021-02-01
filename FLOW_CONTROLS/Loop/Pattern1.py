# 3+33+333=369
# ex: "3"*2 = "33",  not 6
#     "hello"*3 = "hellohellohello"

num = input("enter the number :")  # "3"
i = 1
data = 0
pattern = ""                       # pattern need to be intialized
while(i<=int(num)):                # 1<=int("3"),2<=int("3"),3<=int("3"),4<=int("3") -> condition false
    res = num*i                    # res = "3"*1="3","3"*2="33","33"*3="333"
    pattern = pattern + "+" + res  # pattern = "+3","+33","+333"
    data = data + int(res)         # data = 0+int("3")=3,3+int("33")=36,36+int("333")=369
    i+=1                           # i = 2,3,4

pattern = pattern.lstrip("+")      # removing + from front using string function lstrip
print(pattern,end="")
print(" =",data)