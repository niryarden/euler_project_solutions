# this script doesn't return. too complex
# it does work for smaller grids then 20 (10x10 for example)

# the input is the length of one side of the square
try:
    grid = int(input("How big is your grid >> "))
except:
    print("Please insert an int")
    quit()

# if 0 means “go down“ and 1 means "go right"
# we can translate the path to a binary number of (grid*2) chars

maxbin = int(grid * 2 * "1", 2)
paths = list()

# looping through all the numbers which equals to the binary number under grid*2*"1"
# putting into a list every binary number which has same amount of "1"s and ”0's
# cause that means it can be translated to “down" and "n'ght' and go from corner to corner of the square
for i in range(maxbin):
    bina = bin(i)[2:]
    bina = "0" * (len(grid * 2 * "1") - len(bina)) + bina
    chars = [int(char) for char in bina]
    if sum(chars) == grid:
        paths.append(bina)

#output the length of the list of paths which means ”how many possible paths“
print(len(paths))
