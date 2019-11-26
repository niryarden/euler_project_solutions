# answer: 5537376230
import os

lst = []
with open(os.path.join("data", "euler13data.txt"), 'r') as data:
    for line in data:
        lst.append(int(line[:11]))

sumi = sum(lst)
print(int(str(sumi)[:10]))
