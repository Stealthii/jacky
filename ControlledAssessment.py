#Tasks 1-4
import random


def menu():
    while True:
        print('Welcome to the encryption program!\n')
        print('To encrypt your file, input 1')
        print('To decrypt your file, input 2')
        print('To see the encrypted message, input 3')
        print('To exit this program, input 4')
        number = input('Please input a selection: ')
        if number == '1':
            encryption()
        elif number == '2':
            decryption()
        elif number == '3':
            block_encryption()
        elif number == '4':
            raise SystemExit(0)
        else:
            print('That was not an option!')


def encryption():
    sumofvalues = offsetz()
    phrase = loadFile()
    offset = get_offset_factor(sumofvalues)
    print('>> Text being encrypted is:', phrase)
    print('>> The sum of the generated encryption key values is:', sumofvalues)
    ciphertext = encrypt(phrase, offset)
    newfilename = input('\nNew filename: ')
    newfile = open(newfilename, 'a')
    newfile.write(ciphertext)


def loadFile():
    print('A file must be chosen for encryption...')
    try:
        fileName = input('Enter filename: ')
        txtFile = open(fileName,'r')
        phrase = txtFile.read()
        txtFile.close()
        return phrase
    except IOError:
        print('File does not exist!')


def encrypt(phrase, offset):
    letter = len(phrase)
    ciphertext = []
    for letter in phrase:
        ascii_code = ord(letter)
        if ascii_code >= 33 or ascii_code <= 126:
            ascii_code = ascii_code + offset
            if ascii_code > 126:
                ascii_code = ascii_code - 94
            else:
                ascii_code = ascii_code
        else:
            ascii_code = ascii_code
        new_letter_2 = chr(ascii_code)
        print('', new_letter_2, end='')
        ciphertext.append(new_letter_2)
    ciphertext = ciphertext
    ciphertext = ''.join(ciphertext)
    return ciphertext


def offsetz():
    ascii_number = 0
    for x in range(8):
        random_integer = random.randrange(33, 126)
        ascii_number = ascii_number + random_integer
        new_letter = chr(random_integer)
        print('', new_letter, end='')
    ascii_number = ascii_number / 8
    ascii_number = int(ascii_number)
    ascii_number = ascii_number - 32
    offset_factor = ascii_number
    print('\n')
    print('Offset Factor = ', ascii_number)
    return offset_factor


def generating_key():
    sumofvalues=0
    for x in range (0, 8):
        my_random_value = random.randrange(33, 126)
        displayChar = chr(my_random_value)
        sumofvalues = sumofvalues + my_random_value
        print('', displayChar, end='')
    return sumofvalues

#Tasks 4-8

def get_offset_factor(values):
    offset_factor = values
    offset_factor = offset_factor / 8
    offset_factor = int(offset_factor)
    offset_factor = offset_factor - 32
    print('This is your offset factor for your eight character key:', offset_factor)
    return offset_factor
    ACSCII_char()


def ACSCII_char():
    if displayChar == 32:
        print(' ')
    else:
        ASCII_message = ord(displayChar)
        ascii_val = ASCII_message + offset_factor
        if ascii_val > 126:
            ascii_val = ascii_val - 94
            letter = chr(ascii_val)
        print(ascii_val)
        print('The plaintext letter', displayChar, 'converts to the ASCII code', ASCII_message, 'add the offset factor', offset_factor, ' to get the result', ascii_val)
    return ascii_val
    return ASCII_message
    save_file()


def save_file():
    try:
        aFile = input('Save as File Name:      \n')
        myfile = open(aFile,'r+w')
        try:
            myfile.write('The plaintext letter', displayChar, 'converts to the ASCII code', ASCII_message, 'add the offset factor', offset_factor, ' to get the result', ascii_val)
        finally:
            myfile.close()
    except TypeError:
        print('filename error!')
        return
    return aFile


def decryption():
    sumVal = 0
    file = loadFile()
    encryption_key = input('Please enter the eight character key that was used to encrypt the message: \n')
    for letter in encryption_key:
        val = ord(letter)
        sumVal = sumVal + val
    offset = offset_factor(sumVal)
    for displayChar in file:
        if displayChar == 32:
            print(' ')
        else:
            ASCII_message = ord(displayChar)
            ascii_val = ASCII_message - offset
            if ascii_val < 133:
                ascii_val = ascii_val + 94
            letter = chr(ascii_val)
            print('', displayChar, end='')


def block_encryption():
    number = 0
    text = decryption()
    offset_factor = offset_and_key3()
    length = len(text)
    cipher_text = ''
    for x in range(length):
        letter = (text[number])
        asciiv = ord(letter)
        final_ascii = asciiv + offset_factor
        if final_ascii > 126:
            final_ascii = final_ascii - 94
        final_letter = chr(final_ascii)
        number = number + 1
        if letter != ' ':
            cipher_text = cipher_text + final_letter
    length2 = int(len(cipher_text) / 5)
    ciphertext = ''
    num = 0
    for x in range(length2):
        for x in range(5):
            let = (cipher_text[num])
            ciphertext = ciphertext + let
            num = num + 1
        let = ' '
        ciphertext = ciphertext + let
    print ('Block-encrypted Text: ', ciphertext, '\n')
    try:
        input_name = input('Save as filename(.txt): ')
        cipher_text_file = open(input_name, 'w')
        cipher_text_file.write(ciphertext)
        print ('The message you encrypted has been saved to ', input_name)
        print ('\n')
    finally:
        cipher_text_file.close()


if __name__ == "__main__":
    menu()
