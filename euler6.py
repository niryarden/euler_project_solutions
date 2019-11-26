# answer: 25164150

# calculate the square of sums
lst = list(range(1, 101, 1))
square_of_sums = pow(sum(lst), 2)

# calculate the sum of squares
sum_of_squares = 0
for num in lst:
    sum_of_squares = sum_of_squares + pow(num, 2)

# calculate and print the final answer
answer = square_of_sums - sum_of_squares
print(f"answer: {answer}")
