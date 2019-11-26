# answer: 104743

primes_list = []
current = 1
while len(primes_list) < 10002:
    current = current + 1
    status = True
    for i in range(2, current, 1):
        if current % i == 0:
            status = False
            break
    if status:
        primes_list.append(current)

answer = primes_list[-2]
print(f"answer: {answer}")
