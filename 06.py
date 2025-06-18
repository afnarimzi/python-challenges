import math
C=50
H=30
user_input=(input("Enter the values(comma_separated): "))
list=[]
for x in user_input.split(','):
    x=int(x)
    answer=math.sqrt((2 * C *x)/H)
    list.append(int(answer))  
print(list)
