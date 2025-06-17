x=int(input("Enter number of rows:"))
y=int(input("Enter number of columns:"))
result=[]
for i in range(x):
    row=[]
    for j in range(y):
        row.append(i*j)
    result.append(row)
print(result)