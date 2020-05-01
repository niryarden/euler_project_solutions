# answer: 837799


def generate_next_number(num):
    if num % 2 == 0:
        return num / 2
    return 3 * num + 1


max_steps = 0
leader = 1

for i in range(2, 1000000, 1):
    current = i
    counter = 0
    while current > 1:
        current = generate_next_number(current)
        counter += 1
    if counter > max_steps:
        leader = i
        max_steps = counter

print(f"the number {leader} need {max_steps} steps")
