# answer: 76576500
# takes like 3 hours

def getDivisors(number):
    divisors = []
    for i in range(1, int(number / 2) + 1, 1):
        if number % i == 0:
            divisors.append(i)
    return divisors

number = 0
addon = 0
addon_change = 1

while True:
    addon += addon_change
    addon_change += 1
    number += addon
    divisors = getDivisors(number)
    print(len(divisors))
    if len(divisors) > 500:
        print(number)
        quit()
