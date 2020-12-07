#! python3
import os
import re

# idRegex = re.compile(r'((\w{3}:(#)?\w)+\n)')
idRegex = re.compile(r'(\w{3})+:(#?\w+)')

requiredFields = [
    'hcl',
    'iyr',
    'eyr',
    'ecl',
    'pid',
    'byr',
    'hgt'
]

path = os.getcwd()
FILE_NAME = 'day4input.txt'
theFile = os.path.join(path, FILE_NAME)
fileExists = os.path.isfile(theFile)

if fileExists:
    fileContent = open(theFile, 'r')
    print(f'The file {FILE_NAME} exists in {path}')
    content = fileContent.read()
    # print(content)
    data = content.split("\n\n")
    validAmount = 0

    for person in data:
        personInfo = idRegex.findall(person)
        personalRequiredFields = 0
        isValid = False
        personFields = []
        personFieldsMissing = []
        personId = 0

        for item in personInfo:
            # print(item)
            personFields.append(item[0])
            if item[0] == 'pid':
                personId = item[1]

        print(f'\nnew person: {personId}')

        for reqFld in requiredFields:
            if reqFld in personFields:
                print(f'reqFld {reqFld} is valid')
                personalRequiredFields += 1
            else:
                print(f'reqFld {reqFld} is invalid')
                personFieldsMissing.append(reqFld)

        if personalRequiredFields > 6:
            isValid = True
            validAmount += 1
        else:
            print(f'Missing fields:')
            for fld in personFieldsMissing:
                print(f'\t- {fld}')
        print(f'personal required fields: {personalRequiredFields}')
        print(f'valid: {isValid}\n')

    print(f'VALID AMOUNT: {validAmount}')

    fileContent.close()
