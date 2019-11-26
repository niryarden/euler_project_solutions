# answer: 233168

limit = 1000

sumi = 0
for i in range(limit):
    if i % 3 == 0 or i % 5 == 0:
        sumi += i

print(f"answer: {sumi}")
