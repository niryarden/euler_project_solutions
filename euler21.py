# answer:31626

def dfunc(num):
    sumi = 0
    for i in range(1, num):
        if num % i == 0:
            sumi += i
    return sumi


# main
if __name__ == "__main__":
    mainsum = 0
    lst = []
    # build a 10000-cell-long list
    # dfunc all the cells in the list
    for i in range(10000):
        lst.append(i)
        lst[i] = dfunc(i)

    for i in range(10000):
        if lst[i] < 10000:
            if lst[lst[i]] == i:
                if lst[lst[i]] != lst[i]:
                    mainsum += i
                    print(f"yey! {i} match {lst[i]}")

    print(f"answer: {mainsum}")
