######################### List Comprehension ###########################
# offers to create new list based on values of existing list 

numbers=[1,3,4,5,6]

Comprehension=[num*2 for num in numbers]


print(Comprehension)


# find vowels in string

string1="ifnotoktobeok"

vowels="aeiou"

list1=[char for char in string1 if char in vowels]

print(list1)

################################ lambda/Anonymous function ###############################
# special type of function without function name

greet_user= lambda name : print('hey there',name)

print(greet_user("boss"))


##################################### Iterator ################################

# methods that iterate collection like list,tuples,etc.

# we can loop through an object and return its elements

#iterator protocol-___iter__() and __next__()

list2=[1,23,4]

iterateList= iter(list2)

# print(next(iterateList))
# print(next(iterateList))
# print(next(iterateList))
#### for loop

for i in iterateList:
    print(i)


################################ Generators #############################

# A generator is a function that returns as iterator that produces a sequence of value when 
# iterated over..

# useful when we want to produce a large sequence of values,but
# we don't want to store all of them in memory at once..

def my_generator(n):
    value=0

    while value<(n):
        yield value

        value+=1
for value in my_generator(3):
    print(value)

# yield-keyword is used to produce a value from generator and
# pause generator function execution until the next value is requsted.

#1]Easy to implement..
# 2]memory Efficient..
#   ---produces one item at once..

# 4] pipelining generator

# find the sum of squres of numbers in fibonacci series

def fibonacci(nums):
    x,y=0,1
    for i in range (nums):
         x,y=y,x+y
         yield x

def squres(nums):
    for num in nums:
        yield num**2


print(sum(squres(fibonacci(10))))


#################################### Decorator #####################################
# takes in a function ,add some functionality and return it..
   


