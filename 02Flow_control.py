#if...else-_____if...elif..else
#challenge..
def pass_fails(m):
    if(m>=50):
        print("passed")
    else:
        print("failed")
marks=90

pass_fails(marks)


#for loop
#1] for 

langauge=['pyhton','c','swift']

for lang in langauge:
    print(lang)

#_________2] Range function

for i in range(0,4):
    print(i)

#challegen

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
     
factorial(5)
