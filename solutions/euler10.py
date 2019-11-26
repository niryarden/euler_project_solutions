# answer: 142913828922


# the function recieves a number and return True if it is a prime number (and False if not)
def isPrime(num):
    for i in range(3, int(num / 2) + 1, 2):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__":
    sumi = 2
    for i in range(3, 2000000, 2):
        if isPrime(i):
            sumi += i
        # just for tracking
        if i % 10001 == 0:
            print(i)
    print(f"answer {sumi}")
