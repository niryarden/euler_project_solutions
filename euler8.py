# answer: 23514624000
import os

# turn the file into a long string of 1000 digits
number = ""
with open(os.path.join("data", "euler8data.txt"), 'r') as file_content:
    for line in file_content:
        number += line.strip()

# find the biggset product
max_product = 1
max_begining_pointer = 0
for pointer in range(0, 1000 - 13, 1):
    # slice the slice according to the current pointer
    slice = number[pointer: pointer + 13]
    product = 1
    # calc the product
    for digit in list(slice):
        product *= int(digit)
    # compare to the current maximun product
    if product > max_product:
        max_product = product
        max_begining_pointer = pointer

# print the final answer
print(f"The slice: {number[max_begining_pointer: max_begining_pointer + 13]}")
print(f"The product (answer): {max_product}")
