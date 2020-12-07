#! python3
import os
import re

savedPasswordRegex = re.compile(r'(\d{1,2})-(\d{1,2})\s(\w):\s(\w+)')

path = os.getcwd()
print(path)

def checkPasswords(data):
    posOne = data[0]
    posTwo = data[1]
    character = data[2]
    password = data[3]
    print(f'The password {password} needs the character "{character}" at pos {posOne} or {posTwo}')
    if password[int(posOne) - 1] == character:
        if password[int(posTwo) - 1] == character:
            return False
        else:
            return True
    else:
        if password[int(posTwo) - 1] == character:
            return True
        else:
            return False

fileName = 'day2inputs.txt'
theFile = os.path.join(path, fileName)
fileExists = os.path.isfile(theFile)

resultAmount = 0

if fileExists:
    fileContent = open(theFile, 'r')
    print(f'The file {fileName} exists in {path}')
    content = fileContent.readlines()
    for line in content:
        pw = savedPasswordRegex.search(line)
        passwordGroup = pw.groups()
        res = checkPasswords(passwordGroup)
        if res != False:
            resultAmount = int(resultAmount) + 1
            print(resultAmount)
        else:
            print(res)

    fileContent.close()
    print(resultAmount)
