# prints the lines after making all characters in the sentence capitalized
lines=[]
while True:
   s= input("Enter sequences of lines: ")
   if s:
       lines.append(s.upper())
   else:
       break
for line in lines:
   print(line)
          
