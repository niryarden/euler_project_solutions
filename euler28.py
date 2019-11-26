# answer: 669171001

# summing the diagonals is actually suming a sequence of numbers
# the pattern is that the difference between a number to the one after him is bigger by 2 every 4 numbers
# the sequence is (1), 3, 5, 7, 9, 13, 17, 21, 25, 31, 37, 43, 49, 57, 65, 73, 81, 91, 101, 111, 121...
# so the differences: 2, 2, 2, 2, 4, 4, 4, 4, 6, 6, 6, 6, 8, 8, 8, 8, 10, 10, 10, 10...
# so i've just built the sequence and sumed it

# the upper_edge which is 1001**2 (1002001), the biggest number of the table
upper_edge = 1001 ** 2
# the variable which is suming for the final answer
sumi = 1
# the variable which running through the sequence
run = 1
# the variable which hold the current differance between the numbers in the sequence
current_difference = 2
# the variable who tells the scripts when to raise the current difference by 2 (every 4 numbers)
mone = 0

while run < upper_edge:
    run += current_difference
    # print(run) # if you want all the sequence printrd (without 1, which was included in the sum to begin with)
    sumi += run
    mone += 1
    if mone > 3:
        mone = 0
        current_difference += 2

print(f"answer: {sumi}")
