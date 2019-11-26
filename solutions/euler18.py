# answer: 1074
import os

# extract the numbers from the data into a list of lists of ints (lines [])
lines = list()
with open(os.path.join("data", "euler18data.txt"), 'r') as data:
    for line in data:
        temp = line.split(" ")
        temp[-1] = temp[-1][:-1]
        temp = list(map(int, temp))
        lines.append(temp)

total = 0
maxtotal = 0
pointer = 0

# 0 in decimal =     00000000000000 in binary
# 16383 in decimal = 11111111111111 in binary
for index in range(16384):
    # converting each decimal index into a path based on binary
    route = bin(index)[2:]
    route = ((15 - int(len(route))) * str(0)) + route

    # going through the triangle based on the binary route
    for lineindex in range(15):
        pointer += int(route[lineindex])
        total += lines[lineindex][pointer]

    if total > maxtotal:
        maxtotal = total
    total = 0
    pointer = 0

print(f"answer: {maxtotal}")
