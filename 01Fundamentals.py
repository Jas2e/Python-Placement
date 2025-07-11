#python variables and literals

#python variable-type-inferred -automatic recognized type of variable.

# string="program"

# a,b=2,3.23

#challenge..

def bill_split(a,f):
    tax=0.2*a
    total_amount=tax+a
    split=total_amount/f

    return split

amount=3000

friends=5
bill= bill_split(amount,friends)

print("split amount is: ",bill)
