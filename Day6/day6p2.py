#! python3
import os
#import re

path = os.getcwd()
#FILE_NAME = 'day6test.txt'
FILE_NAME = 'day6input.txt'
theFile = os.path.join(path, FILE_NAME)
fileExists = os.path.isfile(theFile)

def check_freq(x, group_size):
    freq = {}
    for c in x:
        if c != '\n':
            freq[c] = x.count(c)
    return_number = 0
    for letter in freq:
        #print(f'letter: {letter}, count: {freq[letter]}')
        if freq[letter] >= group_size:
            return_number += 1
    return return_number

if fileExists:
    fileContent = open(theFile, 'r')
    print(f'The file {FILE_NAME} exists in {path}')
    content = fileContent.read()
    data = content.split("\n\n")

    total = 0

    for i, d in enumerate(data):
        #print(f'Group {i + 1}')
        group = d.split("\n")
        size = len(group)
        f = check_freq(d, size)
        total += f
        #print(f'Group size: {size}')
        #print(f'Total from group: {f}')
        #print('--- --- --- ---')

    print(f'TOTAL: {total}')
