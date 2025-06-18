#print comma-separated sequence after sorting them alphabetically
seq_of_words=input("Enter comma separated sequence of words: ")
sorted_words=sorted(seq_of_words.split(','))
print(','.join(sorted_words))