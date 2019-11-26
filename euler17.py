# answer: 21124
import json
import os

def render_textual_number(num):
    # reading the dictionary of the basic words
    with open(os.path.join("data", "euler17dictionary.json"), 'r') as file_content:
        wordict = json.loads(file_content.read())
    numstr = ""
    if num == 1000: # if the number is 1000
        numstr += wordict[str(1000)]
    elif num > 99: # if the number has three digits
        num = str(num)
        numstr += wordict[num[0]] + "hundred"
        if (int(num[1]) * 10) > 19:
            numstr += "and" + wordict[str(int(num[1]) * 10)]
            if int(num[2]) > 0:
                numstr += wordict[num[2]]
        elif int(num[1:]) > 0:
            numstr += "and" + wordict[str(int(num[1:]))]
    elif num > 19: # if the has two digits and its above 19
        num = str(num)
        numstr += wordict[str(int(num[0]) * 10)]
        if int(num[1])> 0:
            numstr += wordict[num[1]]
    else: # if the number is under 20
        numstr += wordict[str(num)]

    return numstr

# main (utf-8)
if __name__ == "__main__":
    sum = 0
    for num in range(1, 1001, 1):
        sum += len(render_textual_number(num))
    print(f"answer: {sum}")

    #bounus output - insert a number and get it written for you
    print("Bonus:")
    while True:
        x = input("Insert a valid number (up to 1090) >>> ")
        try:
            print()
            print(render_textual_number(int(x)))
        except:
            print("Wasn't a valid number up to 1090")
        print()
        print("Ctrl+C to exit")
