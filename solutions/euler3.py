# this script works for the example - 13195
# too complex for the real question - 600851475143

number = 13195
# set a list
allnums = []
for i in range(number):
    booli = True
    allnums.append(booli)

allnums[0] = False
allnums[1] = False

# all non-primes indexes will turn into False
for i in range(len(allnums)):
    if allnums[i] == False:
        continue
    for z in range(i*2, len(allnums), i):
        allnums[z] = False

# go over the primes and only numbers which are factors of the input will stay True
for i in range(len(allnums)):
    if allnums[i]:
        if number % i != 0:
            allnums[i] = False

# search for the biggest prime factor and print it
maxi = 2
for i in range(len(allnums)):
    if allnums[i]:
        maxi = i

print(f"answer {maxi}")
