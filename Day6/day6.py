#! python3
import os
#import re

path = os.getcwd()
#FILE_NAME = 'day6test.txt'
FILE_NAME = 'day6input.txt'
theFile = os.path.join(path, FILE_NAME)
fileExists = os.path.isfile(theFile)

def check_freq(x):
    freq = {}
    for c in x:
        if c != '\n':
            freq[c] = x.count(c)
    return_number = 0
    for letter in freq:
        return_number += 1
    return return_number

if fileExists:
    fileContent = open(theFile, 'r')
    print(f'The file {FILE_NAME} exists in {path}')
    content = fileContent.read()
    data = content.split("\n\n")

    total = 0

    for i, d in enumerate(data):
        f = check_freq(d)
        #print(f'Group {i + 1}')
        #print(f)
        total += f
        #print('--- --- --- ---')
    
    print(f'TOTAL: {total}')