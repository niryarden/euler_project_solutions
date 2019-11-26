# answer: 983

from decimal import *
getcontext().prec = 10000

# the function get the precision (the numbers behind the dot) of a 1/num, looking for repited pattern and returns the length of it.
# if the precision is shorter than 10, return 0, same as if there is no precision at all.
def find_pattern(precision):
    if len(precision) < 10:
        return 0
    # starting from the fifth digit in the precision because the beginning is sometimes out of the precision
    precision = precision[5:]
    # returning one if the pattern is only one digit long (0.33333333)
    if precision[0] == precision[1] and precision[0] == precision[2] and precision[0] == precision[3]:
        return 1
    for i in range(3, 5000):
        if precision[:i] == precision[i:(2 * i)]:
            return i
            break
    return 0

# main
if __name__ == "__main__":
    nums_and_precisions = list()
    for num in range(1,1001):
        precision= str(Decimal(1) / Decimal(num))[2:]
        tup = (num, find_pattern(precision))
        nums_and_precisions.append(tup)

    maxi = 0
    maxipointer = 0

    for i in range(len(nums_and_precisions)):
        length = nums_and_precisions[i][1]
        pointer = nums_and_precisions[i][0]
        if length > maxi:
            maxi = length
            maxipointer = pointer

    print(f"answer: {Decimal(1) / Decimal(maxipointer)}")
    print(f"the number {maxipointer} has a {maxipointer} digits long pattern")
