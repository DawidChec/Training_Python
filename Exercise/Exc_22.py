from collections import Counter

with open('names.txt', 'r') as open_file:
    opened = open_file.read().split()
listed = []
for i in opened:
    listed.append(i)
    
print(Counter(listed))




