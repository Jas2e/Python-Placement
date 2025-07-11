# create function

def greet(name):
    print("hello",name)

# call function

# greet()


# function argument-input to given function

greet("john")# pass argument

### Library functions-print,sqrt,pow

# used math module

#challenges
import math
def is_prime(n):
    if n <= 1:
        print("it not be prime numebr")
    for i in range(2,int(math.sqrt(n))):
           if n%i==0:
             print("not prime number")  
           else:
                print("prime")   

number=13
is_prime(number)

########### Arbitrary arguments ###########
# Arbitrary arguments allows us to pass varying number of values during function call

# example: def sumof numbers(*numbers)

###################### *args and **kwargs ##################################
used when we are unsure about number of arguments to pass function


# i] *args- passes variable number of non-keyworded arguments
#           on which operation of the tuple can be performed.

# ii] **kwargs-  passes variable number of keyworded arguments
#           on which operation of the dictionary can be performed. dict 
