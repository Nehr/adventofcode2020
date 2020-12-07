#! python3
import os
import re

savedPasswordRegex = re.compile(r'(\d{1,2})-(\d{1,2})\s(\w):\s(\w+)')

path = os.getcwd()
print(path)

def checkPasswords(data):
    amount = data[3].count(data[2])
    print(f'The password {data[3]} needs the character "{data[2]}" {data[0]}-{data[1]} times ({data[2]}: {amount})')
    #|| amount >= int(data[0]): {amount >= int(data[0])} || amount <= int(data[1]): {amount <= int(data[1])}'
    if amount >= int(data[0]) and amount <= int(data[1]):
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
