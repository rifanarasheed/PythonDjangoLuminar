# nested dictionary
# to read from another file and prints name and course

stud = open("students","r")

students = {}

for lines in stud:
    id,name,total,course = lines.rstrip("\n").split(",")   # assigning values into each variable by splitting them
    # print(id)
    # print(name)
    # print(total)
    # print(course)
    if id not in students:
        students[id]={"id":id,"name":name,"total":total,"course":course}      # nested dictionary is created with id [outerkey]=[innerkey and value]
print(students)

def print_data(**kwargs):
    id = kwargs["id"]
    if id in students:
        print("id :",students[id]["id"])
        print("name : ",students[id]["name"])
        if "prop" in kwargs:
            prop = kwargs["prop"]
            print("course : ",students[id][prop])
        else:
            pass
    else:
        print("id does not exist")


print_data(id="1001",prop="course")    # if id is in string, put id in "" or convert into id when assigning

