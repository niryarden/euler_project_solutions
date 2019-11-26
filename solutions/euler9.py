# answer: 31875000 (200, 375, 425)

for a in range(1, 999, 1):
    for b in range(1, 1000 - 1 - a, 1):
        c = 1000 - a - b
        if pow(a, 2) + pow(b, 2) == pow(c, 2):
            print(f"{a} < {b} < {c} (a < b < c)")
            print(f"answer: {a * b * c} (a*b*c)")
            quit()
