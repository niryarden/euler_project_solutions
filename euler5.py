# answer: 232792560

status = True
num = 2520
answer = 0

while status:
    num = num + 20
    # make a list of all the remainders of the deviding by 1 to 20
    remainders = []
    for i in range(1, 21, 1):
        remainders.append(num % i)
    # check if the sum of the remainders is 0 (which means the number fits)
    if sum(remainders) == 0:
        answer = num
        status = False

print(f"answer: {answer}")
