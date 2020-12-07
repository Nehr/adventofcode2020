#! python3
import os
#import re

width = 11
height = 11

x = 0
y = 0

STEP_X = 3

result = 0

currentX = 0
currentY = 0

path = os.getcwd()
fileName = 'day3map.txt'
# fileName = 'day3test.txt'
theFile = os.path.join(path, fileName)
fileExists = os.path.isfile(theFile)

if fileExists:
    fileContent = open(theFile, 'r')
    print(f'The file {fileName} exists in {path}')
    content = fileContent.readlines()

    MAX_LENGTH = int(len(content[0]) - 1)
    #MAX_LENGTH = len(myMap[0]) - 1
    print(f'max length: {MAX_LENGTH}')

    for y in content:
        if (currentX > (MAX_LENGTH - 1)):
            print(f'current {currentX}')
            print(f'new current: {currentX} - {MAX_LENGTH}')
            currentX = currentX - MAX_LENGTH
        else:
            print(f'current: {currentX}')
        print(f'row: {currentY}, current x: {content[currentY][currentX]}')
        if content[currentY][currentX] == '#':
            result += 1
        currentY += 1
        currentX += STEP_X

print(f'result: {result}')
