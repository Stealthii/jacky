# Tasks 1-4
import random


# Task 1

def menu():
    """Menu for this program"""
    while True:  # keep menu going until user exits
        print('Welcome to the encryption program!\n')
        print('To encrypt your file, input 1')
        print('To decrypt your file, input 2')
        print('To do extended encryption, input 3')
        print('To exit this program, input 4')

        number = input('Please input a selection: ')
        if number == '1':
            encryption()
        elif number == '2':
            decryption()
        elif number == '3':
            pass  # To do Task 10
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

    key = generate_key()
    offset = get_offset_factor(key)
    ciphertext = encrypt(phrase, offset)

    print("Your encryption key is:", key)
    print("The offset factor is:", offset)
    print("Text being encrypted is:", phrase)
    print("Encrypted text is:", ciphertext)

    newfilename = input('\nNew filename: ')
    savefile(ciphertext, newfilename)


# Task 7 & 9

def decryption():
    """Decrypt a phrase and print it"""

    print("Please choose a file for decryption.")
    filename = input('Enter filename: ')
    try:
        ciphertext = loadfile(filename)
    except IOError:
        print("We couldn't open the file!")
        return

    key = input('Enter the eight character encryption key: ')
    if len(key) is not 8:
        print("Not a valid key!")
        return
    offset = get_offset_factor(key)
    phrase = decrypt(ciphertext, offset)

    print("The decrypted phrase is:", phrase)  # Task 9


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
    phrase = []
    for letter in ciphertext:
        ascii_code = ord(letter)
        # Do not decrypt spaces
        if ascii_code == 32:
            pass
        else:
            ascii_code = ascii_code - offset
            # Add 94 to make character a valid ASCII code
            if ascii_code < 32:
                ascii_code = ascii_code + 94
        new_letter = chr(ascii_code)
        phrase.append(new_letter)
    phrase = ''.join(phrase)  # Convert list to string
    return phrase


# Task 3

def generate_key():
    """Generate an 8 character key"""
    key = []  # List to store key characters
    for _ in range(8):
        random_integer = random.randrange(33, 126)
        new_letter = chr(random_integer)
        key.append(new_letter)
    key = "".join(key)  # Convert list into string
    return key


# Task 4

def get_offset_factor(key):
    """Calculate the offset factor for a key"""
    total = 0
    for letter in key:
        total += ord(letter)
    offset_factor = int((total / 8) - 32)  # Calculate offset factor
    return offset_factor


if __name__ == "__main__":
    menu()
