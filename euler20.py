# answer: 648

# turning sumi into 100! (100 factorial)
sumi = 1
for i in range(1, 101, 1):
    sumi *= i
sumi = str(sumi)

# checking for the sum of the digits of sumi
sum_of_digits = 0
for i in sumi:
    sum_of_digits += int(i)

print(f"answer: {sum_of_digits}")
