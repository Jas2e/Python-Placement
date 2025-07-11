#numerical
# number-integer,float,complex number 2+3j
#1]random

# import random

#2]math

# import math
# math.pi


###########################  LIST #######################
# store multiple item in single variable.

# like array...

# contais differnt data type like string ,numbers,another list

# characteristics:
# 1]ordered
# 2]mutable:item can be cahnged after creation
# 3]allow duplicates

# slicing oprator : 

#Methods

age=[23,43,42,52,21]

name="jasvant"

print(age[1],age[-1],type(age))

print(name[::-2])

###################################  Tuples ################################
# similar to the list but immutable...

# characteristics:
# 1]ordered
# 2]immutable:can not be changed after creation.
# 3]allow duplicates

numbers=(1,2,-3,4,-5)

print(numbers,type(numbers))

####################################### STrings ################################

# string is sequence of characters . for example "hello" is string 
# containing 'h','e', etc.

#python string are immutable

name="python"

print(name[:-1],name[1])
 
print(f'heloo Iam {name}') 

#challenge
def double_letter(s):
    string1=""
    for char in s:
        char*=2
        string1+=char

    print(string1)

string="hello"

double_letter(string)


########################## SETs###############################
# unique data 
# cannot be duplicates
# differnt types of data
# cannot mutable
# no particular order

number={1,3,24,1,3,1,4,52,64}

print(number)


# ###################################### Dictionary ##########################
# Dictionary has to key value pair

country_capital={
    "india":"dehli",
    "italy":"rome"
}

print(country_capital["india"])