#! python3
import os
import re

seatRegex = re.compile(r'(\w{7})(\w{3})')

MAX_ROWS = 127
MAX_COLUMNS = 7

def getNumber(numberData, startingNumber):
    #print(f'numberData: {numberData}, startingNumber: {startingNumber[0]} - {startingNumber[1]}\n')
    number = startingNumber
    for l in numberData:
        #print(f'NEW LETTER ({l}): {number}')
        number = getUpperOrLower(l, number)
    return number

def getUpperOrLower(letter, number):
    lowNum = number[0]
    highNum = number[1] + 1
    if letter == 'F' or letter == 'L':
        x = int((highNum - lowNum) / 2)
        new_upper = lowNum + x - 1
        #print(f'(lower, x = {x}) new numbers: [{lowNum}, {new_upper}]\n')
        return [lowNum, new_upper]
    else:
        x = int((highNum - lowNum) / 2)
        new_lower = lowNum + x
        #print(f'(upper, x = {x}) new numbers: [{new_lower}, {highNum - 1}]\n')
        return [new_lower, highNum - 1]

def getSeatID(row_number, seat_number):
    return (row_number * 8) + seat_number

path = os.getcwd()
#FILE_NAME = 'day5test.txt'
FILE_NAME = 'day5input.txt'
theFile = os.path.join(path, FILE_NAME)
fileExists = os.path.isfile(theFile)

if fileExists:
    fileContent = open(theFile, 'r')
    print(f'The file {FILE_NAME} exists in {path}')
    content = fileContent.read()
    data = content.split("\n")

    seat_id_list = []

    for d in data:
        seatData = seatRegex.findall(d)
        row = seatData[0][0]
        column = seatData[0][1]
        #print(f'\nrow: {row}, column: {column}')
        rowNumber = getNumber(row, [0,127])
        seatNumber = getNumber(column, [0,7])
        seatID = getSeatID(rowNumber[0], seatNumber[0])
        #print(f'ROW NUMBER: {rowNumber[0]} [{rowNumber[0]}, {rowNumber[1]}]')
        #print(f'SEAT NUMBER: {seatNumber[0]} [{seatNumber[0]}, {seatNumber[1]}]')
        #print(f'SEAT_ID: {seatID} \n\n--- --- --- --- --- --- --- --- ---')
        print(f'SEAT_ID: {seatID}')
        seat_id_list.append(seatID)

    seat_id_list.sort(reverse=True)
    print(f'Highest value: {seat_id_list[0]}')