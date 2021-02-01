#different types of languages
#1.Strictly typed languages
#2.Dynamically typed languages
#3.Statically typed languages

#Strictly typed languages
## when declare a variable, we explicitly mention its datatype
#  datatype variable_name = value
#  eg: int mark = 45;
#      mark = "hello";    ERROR BECAUSE MARK'S DATATYPE IS GIVEN AS INTEGER
#      String name = "Luminar";
# java,C,C++

#Dynamically typed languages
#   datatype not required, datatype of variable depend on value assigned to it.
#   variable_name = value
# python, R

#Statically typed languages
#During declaration of variable, it can be in any datatype.
#Its datatype depends on value intialized
#   eg: var mark;
#       mark = 10;  INTEGER VALUE IS ASSIGNED, MAKING THAT VARIABLE AS INTEGER VARIABLE.
# Scala


# Variable is used to represent a memory location
# eg : number = 2
# a variable named as number has been created and value 2 as assigned to it.
# this means that value 2 has been stored in a memory location(ex: 0010001) which has a memory address to identify it.

company_name = "Luminar Technolab"
location = "Kakkanad"
print("Company Name =",company_name)  # to concatenate variable value to string, use concatenate operator comma.
print("Location =",location)

# TO PRINT "our company luminar technolab is located at Kakkanad"
print("our company",company_name,"is located at ",location)

