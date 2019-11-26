# this script doesn't return. too complex

lst = []
# 1099511627775 is the value of 40 times 1 in binary (11111...[30 more 1]...11111)
for i in range(1099511627775):
    bina = bin(i)[2:]
    ll = list(bina)
    sumi = 0
    for z in ll:
        sumi += int(z)
    if sumi == 20:
        lst.append(bina)

print(len(lst))
