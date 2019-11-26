# answer: 4613732

# define the begining of the list
fibonacci = []
fibonacci.append(0)
fibonacci.append(1)

# make the list until 4000000
i = 0
term = 0
sumi = 0
while term < 4000000:
    term = fibonacci[i] + fibonacci[i + 1]
    fibonacci.append(term)
    i += 1
    # mean while, sum the even-valued terms
    if term % 2 == 0:
        sumi += term

print(f"answer: {sumi}")
