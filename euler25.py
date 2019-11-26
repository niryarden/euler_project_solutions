# answer: 4782

# define the begining of the list
fibonacci = list()
fibonacci.append(0)
fibonacci.append(1)

# make the list 5000 cells long
for i in range(5000):
    fibonacci.append(fibonacci[i] + fibonacci[i + 1])

# run along the list and look for a cell with 1000 character
for i in range(len(fibonacci) + 1):
    leng = len(str(fibonacci[i]))
    if leng == 1000:
        print(i)
        break
