# answer: 1366

sum = 1
for i in range(1000):
    sum *= 2
sum = str(sum)

again = 0
for i in sum:
    again += int(i)

print(again)
