# answer: 906609

# 999 * 999 = 998001
# 100 * 100 = 10000
# So we can say for sure that our number should have 5 or 6 digits

# this functions gets a num and return True if it is a palindrome
def isPalindrome(num):
    num = str(num)
    if len(num) == 5:
        if num[0] == num[4] and num[1] == num[3]:
            return True
        else:
            return False
    elif len(num) == 6:
        if num[0] == num[5] and num[1] == num[4] and num[2] == num[3]:
            return True
    return False

# loop through all the palindrome products and find the largest one.
maxi = 0
for i in range(100, 999, 1):
    for j in range(100, 999, 1):
        num = i * j
        if isPalindrome(num):
            if num > maxi:
                maxi = num

print(f"answer: {maxi}")
