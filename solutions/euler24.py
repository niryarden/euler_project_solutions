# answer:
# too complex. does not return

permutations = list()
for i in range(123456787, 9876543210):
    current = str(i)
    # turn current into a 10-digit number (with zeros in the begining)
    currnet = (10 - len(current)) * "0" + current
    if "0" in current and "1" in current and "2" in current and "3" in current and "4" in current and "5" in current and "6" in current and "7" in current and "8" in current and "9" in current:
        permutations.append(current)
    if len(permutations) > 1000000:
        break

print(permutations[999999])
