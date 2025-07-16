list=[]
s=input("Enter  sequence of comma separated 4 digit binary numbers :")
numbers=s.split(',')
for numb in numbers:
    if int(numb,2)%5==0:
        list.append(numb)
print(",".join(list))