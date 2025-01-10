def fact(x):
    if x==0:
        return 1
    else:
        return x * fact(x-1)
x=eval(input("Enter a number: "))
print(fact(x))    
    
