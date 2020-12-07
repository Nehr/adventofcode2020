#! python3
import os
import re

# idRegex = re.compile(r'((\w{3}:(#)?\w)+\n)')
idRegex = re.compile(r'(\w{3})+:(#?\w+)')
heightRegex = re.compile(r'((\d{3})(cm))|((\d{2})(in))')

requiredFields = [
    'hcl',
    'iyr',
    'eyr',
    'ecl',
    'pid',
    'byr',
    'hgt'
]

# byr : birth year : 1920 - 2002
# iyr : issue year : 2010 - 2020
# eyr : expiration year : 2020 - 2030
# hgt : height : if cm(150-193) if in(59-76)
# hcl : hair color : #(followed by exactly 6 characters 0-9,a-f)
# ecl : eye color : one of (amb blu brn gry grn hzl oth)
# pid : passport id : 9 digit number including leading zeroes


def validateHeight(height):
    h = heightRegex.findall(height)
    newh = [tuple(' '.join(x).split()) for x in h]
    # print(newh)
    if len(newh) > 0:
        if 'cm' in newh[0]:
            #print(f'height is in cm: {height}')
            return validateMinMaxNumber('hgt (cm)', int(newh[0][1]), 150, 193)
        elif 'in' in newh[0]:
            #print(f'height is in inches: {height}')
            return validateMinMaxNumber('hgt (in)', int(newh[0][1]), 59, 76)
        else:
            print(f'!hgt is invalid {height}')
            return False
    else:
        print(f'!hgt is invalid {height}')
        return False


def validateMinMaxNumber(name, number, MIN, MAX):
    if number >= MIN and number <= MAX:
        print(f'{name} is valid {number} [{MIN}-{MAX}]')
        return True
    else:
        print(f'!{name} is invalid {number} [{MIN}-{MAX}]')
        return False


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
        personData = {}
        validFields = []

        for item in personInfo:
            # print(item)
            personFields.append(item[0])
            personData[item[0]] = [item[1]]
            if item[0] == 'pid':
                personId = item[1]

        print(f'\nnew person: {personId}')

        for reqFld in requiredFields:
            if reqFld in personFields:
                if reqFld == 'byr':
                    validFields.append(validateMinMaxNumber(
                        'byr', int(personData[reqFld][0]), 1920, 2002))
                elif reqFld == 'iyr':
                    validFields.append(validateMinMaxNumber(
                        'iyr', int(personData[reqFld][0]), 2010, 2020))
                elif reqFld == 'eyr':
                    validFields.append(validateMinMaxNumber(
                        'eyr', int(personData[reqFld][0]), 2020, 2030))
                elif reqFld == 'hgt':
                    validFields.append(validateHeight(personData[reqFld][0]))
                else:
                    print(f'reqFld {reqFld} is existing')
                personalRequiredFields += 1
            else:
                print(f'reqFld {reqFld} is invalid')
                personFieldsMissing.append(reqFld)

        if personalRequiredFields > 6:
            isValid = True
            validAmount += 1
        else:
            print('Missing fields:')
            for fld in personFieldsMissing:
                print(f'\t- {fld}')
        print(f'personal required fields: {personalRequiredFields}')
        print(f'missing fields validation, valid: {isValid}\n')
        print(f'validation of fields: {validFields}')

    print(f'VALID AMOUNT: {validAmount}')

    fileContent.close()
