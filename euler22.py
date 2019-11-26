# answer: 871198282
import os

# gets a name and return the sum of gimatry value of all the chars in it
def gimatry(word):
    sumi = 0
    for i in range(len(word)):
        charval = ord(word[i]) - 64
        sumi += charval
    return sumi

# main
if __name__ == "__main__":
    # extract the name and alphabetize them in a list
    # the first cell in the list would be AAAA
    # it won't count becaause we multiply it by 0, but it's gonne start the real list from index 1.
    with open(os.path.join("data", "euler22data.txt"), 'r') as file_content:
        data = file_content.read()
    data = data[1: len(data) - 1]
    lst = data.split("\",\"")
    lst.append("AAAAAAA")
    lst = sorted(lst)

    # going through the list and sumerizing the gimatry value of everything
    mainsum = 0
    for i in range(len(lst)):
        name = lst[i]
        score = gimatry(name) * i
        mainsum += score

    print(f"answer: {mainsum}")
