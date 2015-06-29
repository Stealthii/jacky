# Tasks 1-4
import random


# Task 1

def menu():
    """Menu for this program"""
    while True:  # keep menu going until user exits
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
            pass  # TODO
        elif number == '4':
            raise SystemExit(0)
        else:
            print('That was not an option!')


# Task 2

def encryption():
    """Encrypt a phrase and save to file"""

    print("Please choose a file for encryption.")
    filename = input('Enter filename: ')
    try:
        phrase = loadfile(filename)
    except IOError:
        print("We couldn't open a file!")
        return

    key, offset = generate_key()
    ciphertext = encrypt(phrase, offset)

    print("Your encryption key is:", key)
    print("The offset factor is:", offset)
    print("Text being encrypted is:", phrase)
    print("Encrypted text is:", ciphertext)

    newfilename = input('\nNew filename: ')
    savefile(ciphertext, newfilename)


# Task 7

def decryption():
    """Decrypt a phrase and print it"""
    print("Please choose a file for decryption.")
    filename = input('Enter filename: ')
    try:
        ciphertext = loadfile(filename)
    except IOError:
        print("We couldn't open the file!")
        return
    encryption_key = input('Please enter the eight character key that was used to encrypt the message: \n')
    if len(encryption_key) is not 8:
        print("Not a valid key!")
        return
    sumVal = 0
    for letter in encryption_key:
        val = ord(letter)
        sumVal = sumVal + val
    offset = get_offset_factor(sumVal)
    decryptedtext = []
    for displayChar in ciphertext:
        if displayChar == 32:
            print('bork')
        else:
            ASCII_message = ord(displayChar)
            ascii_val = ASCII_message - offset
            if ascii_val < 32:
                ascii_val = ascii_val + 94
            letter = chr(ascii_val)
            decryptedtext.append(letter)
            # print('', letter, end='')
    decryptedtext = ''.join(decryptedtext)
    print(decryptedtext)


def loadfile(filename):
    """Will return file contents as a string"""
    with open(filename, "r") as myfile:
        return "".join(line.rstrip() for line in myfile)


# Task 6

def savefile(text, filename):
    """Opens a file and writes text to it"""
    with open(filename, "w") as myfile:
        myfile.write(text)


# Task 5

def encrypt(phrase, offset):
    """Returns an encrypted phrase"""
    ciphertext = []
    for letter in phrase:
        ascii_code = ord(letter)
        # Do not encrypt spaces
        if ascii_code == 32:
            pass
        elif ascii_code >= 33 or ascii_code <= 126:
            ascii_code = ascii_code + offset
            # Remove 94 to make character a valid ASCII code
            if ascii_code > 126:
                ascii_code = ascii_code - 94
        new_letter = chr(ascii_code)
        ciphertext.append(new_letter)
    ciphertext = ''.join(ciphertext)  # Convert list into string
    return ciphertext


# Task 8

def decrypt(ciphertext, offset):
    """Returns a decrypted phrase"""

# Task 3 & 4

def generate_key():
    """Generate an 8 character key and offset factor"""
    ascii_number = 0
    key = []  # List to store key characters
    for _ in range(8):
        random_integer = random.randrange(33, 126)
        ascii_number = ascii_number + random_integer
        new_letter = chr(random_integer)
        key.append(new_letter)
    key = "".join(key)  # Convert list into string
    offset_factor = int((ascii_number / 8) - 32)  # Calculate offset factor
    return key, offset_factor


# Tasks 4-8

def get_offset_factor(values):
    offset_factor = values
    offset_factor = offset_factor / 8
    offset_factor = int(offset_factor)
    offset_factor = offset_factor - 32
    print('This is your offset factor for your eight character key:', offset_factor)
    return offset_factor
    # ACSCII_char()

"""
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
"""


if __name__ == "__main__":
    menu()
