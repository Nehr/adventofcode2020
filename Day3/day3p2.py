#! python3
import os

# [x, y]
steps = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2]
]

result = [0] * len(steps)
RES_MAX = len(result) - 1
print(result)

path = os.getcwd()
fileName = 'day3map.txt'
theFile = os.path.join(path, fileName)
fileExists = os.path.isfile(theFile)

if fileExists:
    fileContent = open(theFile, 'r')
    print(f'The file {fileName} exists in {path}')
    content = fileContent.readlines()

    MAX_LENGTH = int(len(content[0]) - 1)
    print(f'max length: {MAX_LENGTH}')
    currentIndex = 0

    for step in steps:
        print(f'x: {step[0]}, y: {step[1]}')
        x = 0
        y = 0
        currentX = 0
        currentY = 0
        STEP_X = step[0]

        for con in content:
            if step[1] == 1 or currentY % 2 == 0:
                print(f'currentY + 1: {currentY + 1}, % 0 = {(currentY + 1) % 2 == 0}')
                if (currentX > (MAX_LENGTH - 1)):
                    print(f'current {currentX}')
                    print(f'new current: {currentX} - {MAX_LENGTH}')
                    currentX = currentX - MAX_LENGTH
                else:
                    print(f'current: {currentX}')
                print(f'row: {currentY}, current x: {content[currentY][currentX]}')
                if content[currentY][currentX] == '#':
                    result[currentIndex] += 1
                currentY += 1
                currentX += STEP_X
            else:
                print(f'row: {currentY} is even')
                currentY += 1
        print(f'\n ### \n')

        currentIndex += 1

answer = 0

for res in result:
    print(f'answer: {answer}')
    print(f'res: {res}')
    if answer != 0:
        answer = answer * res
    else:
        answer = res

print(f'final answer: {answer}')
