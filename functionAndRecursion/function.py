
def calc_sum(a,b):
    sum = a+b
    print(sum)


calc_sum(2,3)    


#default argument 
# we always give default parameter value at the last after the normal parameter is over
def prod(a,b=3):
   print(a*b)

prod(2)


def factorial(n):
    fact=1 
    for i in range(1,n+1):
        fact*=i
    print(fact) 

factorial(5)    