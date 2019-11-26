# answer: 70600674
import os

square= []
# extracting the data out from the web page in placing it a list of lists called square
with open(os.path.join("data", "euler11data.txt"), 'r') as data:
    for line in data:
        x = line.split()
        for i in range(len(x)):
            x[i] = int(x[i])
        square.append(x)

# defining some variables
maxi = 0
lineindex = -1
numindex = -1

# each loop is a line of the square
for line in square:
    lineindex += 1
    #each loop is a number
    for num in line:
        numindex += 1
        num = int(num)

        #checking the location of the number in square in order to understand which checks i can do
        if numindex > 2:
            left = True
        else: left = False
        if numindex < 17:
            right= True
        else: right = False
        if lineindex > 2:
            up = True
        else: up = False
        if lineindex < 17:
            down = True
        else: down= False

        #bonus output- log of the status of each number in the square
        print(f"number: {square[lineindex][numindex]}, line: {lineindex}, collumn: {numindex}")
        print(f"left: {left}, right: {right}, up: {up}, down: {down}")
        print()

        #checking for each number all the possible products- left, right, up down and diagonal
        if left:
            check = square[lineindex][numindex] * square[lineindex][numindex - 1] * square[lineindex][numindex - 2] * square[lineindex][numindex - 3]
            if check > maxi:
                maxi = check

        if right:
            check = square[lineindex][numindex] * square[lineindex][numindex + 1] * square[lineindex][numindex + 2] * square[lineindex][numindex + 3]
            if check > maxi:
                maxi = check

        if up:
            check = square[lineindex][numindex] * square[lineindex - 1][numindex] * square[lineindex - 2][numindex] * square[lineindex- 3][numindex]
            if check > maxi:
                maxi = check

        if down:
            check = square[lineindex][numindex] * square[lineindex + 1][numindex] * square[lineindex + 2][numindex] * square[lineindex + 3][numindex]
            if check > maxi:
                maxi = check

        if left and down:
            check = square[lineindex][numindex] * square[lineindex + 1][numindex - 1] * square[lineindex + 2][numindex - 2] * square[lineindex + 3][numindex - 3]
            if check > maxi:
                maxi = check

        if left and up:
            check = square[lineindex][numindex] * square[lineindex - 1][numindex - 1] * square[lineindex - 2][numindex - 2] * square[lineindex - 3][numindex - 3]
            if check > maxi:
                maxi = check

        if right and down:
            check = square[lineindex][numindex] * square[lineindex + 1][numindex + 1] * square[lineindex + 2][numindex + 2] * square[lineindex +3][numindex+ 3]
            if check > maxi:
                maxi = check

        if right and up:
            check = square[lineindex][numindex] * square[lineindex - 1][numindex + 1] * square[lineindex - 2][numindex + 2] * square[lineindex - 3][numindex + 3]
            if check > maxi:
                maxi = check

    numindex = -1

print(f"answer {maxi}")
