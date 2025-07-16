#prints the words after removing all duplicate words and sorting them alphanumerically
s=input("Enter sequence of whitespace separated words :")
words=s.split()
unique=set(words)
sorted=sorted(unique)
print(" ".join(sorted))