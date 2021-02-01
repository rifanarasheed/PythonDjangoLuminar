lst = [1,2,3,5]
low = 0
upp = len(lst)-1
element = int(input("enter the element"))
pairlist = []
while(low<upp):
    tot = lst[low]+lst[upp]
    if(element==tot):
        print(lst[low],lst[upp])  # pairlist.append((lst[low],lst[upp]))
        break   # upp-=1
    elif(element>tot):
        low+=1
    else:
        upp-=1