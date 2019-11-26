# answer: 45228

pandigital_products = list()
# loop through all the possible multipliers
for product in range(2000, 9999):
    # looping through possible multipliers
    for multiplier in range(2, int(product / 2 + 2)):
        multiplier = int(multiplier)
        if product % multiplier == 0:
            multiplicand = int(product / multiplier)
            # make a string of the digits of all product/multiplier/multiplicand so we can do the checks in it as a whole
            array = str(product) + str(multiplier) + str(multiplicand)
            cond = True
            for i in range(1, 10, 1):
                if str(i) not in array:
                    cond = False
            if len(array) == 9 and cond:
                # i could save only the product int the tupple but it's useful to save everything in order to do checks
                tup = (product, multiplier, multiplicand)
                pandigital_products.append(tup)
                # the break is essential for not getting the same multiplier/multiplicand twice
                break

# and finally, just sum the products
sumi = sum([line[0] for line in pandigital_products])
print(f"answer: {sumi}")
