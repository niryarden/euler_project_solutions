# answer: 137846528820
# this scripts is working. eular15b and eular15c are too complex scripts that do not work due to inefficiency

def atzeret(num):
    atz = 1
    for i in range(1, num + 1):
        atz *= i
    return atz

if __name__ == "__main__":
    n = 40
    k = 20
    mone = atzeret(n)
    mechane = atzeret(k) * atzeret(n-k)
    answer = int(mone / mechane)
    print(answer)
