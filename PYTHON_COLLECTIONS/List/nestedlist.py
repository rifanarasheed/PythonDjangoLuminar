students = [
    [10,"ajay","bca",250],
    [11,"vijay","bca",240],
    [12,"sibin","bca",220],
    [13, "dino", "mca", 220],
    [14, "tom", "mca", 180],
    [15, "jain", "mca", 250],
]

# print names only
for stud in students:
    print(stud[1])

# print student names whose marks >240
for stud in students:
    if(stud[3]>240):
        print(stud[1])

# print total sum of marks
marktotal = 0
for stud in students:
    marktotal = marktotal + stud[3]  # 0+250=250, 250+240= 490,...
print("marks :",marktotal)

# calculate total marks ob bca and mca separetly
mcatotal = 0
bcatotal = 0
for stud in students:
    if stud[2]=="bca":
        bcatotal+=stud[3]
    else:
        mcatotal+=stud[3]
print("mca total",mcatotal)
print("bca total",bcatotal)