#! python3
import os
import re

idRegex = re.compile(r'(\w{3})+:(#?\w+)')
heightRegex = re.compile(r'((\d{3})(cm))|((\d{2,3})(in))')
hairColorRegex = re.compile(r'#[a-f0-9]{6}')
passportIdRegex = re.compile(r'^\d{9}$')

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

def validatePassportId(passportId):
    p = passportIdRegex.match(passportId)
    if p:
        print(f'pid is valid {p.group()}')
        return True
    else:
        print(f'!pid is invalid {passportId}')
        return False

def validateEyeColor(color):
    VALID_COLORS = [
        'amb',
        'blu',
        'brn',
        'gry',
        'grn',
        'hzl',
        'oth'
    ]
    if color in VALID_COLORS:
        print(f'ecl is valid {color}')
        return True
    else:
        print(f'!ecl is invalid {color}')
        return False

def validateHairColor(color):
    c = hairColorRegex.match(color)
    if c:
        print(f'hcl is valid {c.group()}')
        return True
    else:
        print(f'!hcl is invalid {color}')
        return False

def validateHeight(height):
    h = heightRegex.findall(height)
    newh = [tuple(' '.join(x).split()) for x in h]
    if len(newh) > 0:
        if 'cm' in newh[0]:
            return validateMinMaxNumber('hgt (cm)', int(newh[0][1]), 150, 193)
        elif 'in' in newh[0]:
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
# FILE_NAME = 'day4test2.txt'
theFile = os.path.join(path, FILE_NAME)
fileExists = os.path.isfile(theFile)

if fileExists:
    fileContent = open(theFile, 'r')
    print(f'The file {FILE_NAME} exists in {path}')
    content = fileContent.read()
    data = content.split("\n\n")
    validAmount = 0

    for person in data:
        personInfo = idRegex.findall(person)
        personalRequiredFields = 0
        personFields = []
        personId = 0
        personData = {}
        validFields = []

        for item in personInfo:
            personFields.append(item[0])
            personData[item[0]] = [item[1]]
            if item[0] == 'pid':
                personId = item[1]

        print(f'\nNEW PERSON ({personId})')

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
                elif reqFld == 'hcl':
                    validFields.append(validateHairColor(personData[reqFld][0]))
                elif reqFld == 'ecl':
                    validFields.append(validateEyeColor(personData[reqFld][0]))
                elif reqFld == 'pid':
                    validFields.append(validatePassportId(personData[reqFld][0]))
                else:
                    print(f'{reqFld} is existing')
                personalRequiredFields += 1
            else:
                print(f'{reqFld} is missing')
                validFields.append(False)

        print(f'SUMMARY\nTotal fields in passport: {personalRequiredFields} / 7')

        if personalRequiredFields > 6:
            if False in validFields:
                print(f'Validation of fields: {validFields}')
                print('Not all fields are valid')
            else:
                print('All fields are valid')
                validAmount += 1
                print(f'VALID AMOUNT (counting): {validAmount}')
        else:
            print('Not all required fields are existing')

    print(f'\nVALID AMOUNT TOTAL: {validAmount}\n')

    fileContent.close()
