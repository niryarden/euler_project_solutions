# answer: 9183

tmplist = []
for a in range(2, 101):
    tmplist += [a ** b for b in range(2, 101)]

lst = []
lst.append(tmplist[0])
cond = True

for i in range(1, len(tmplist)):
    cond = True
    for z in range(0, i):
        if tmplist[i] == tmplist[z]:
            cond = False
    if cond:
        lst.append(tmplist[i])

print(f"answer: {len(lst)}")
