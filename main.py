import string

def encryption():
    user_text = input('Enter a brief message to encrypt ')
    word_shift = int(input('Enter a number to shift by '))
    encrypt = ' '
    for i in user_text:
        if i.isupper() or i.islower():
            #find unicode
            i_unicode = ord(i)
            i_index = ord(i) - ord('A')

            #letter shift
            new_index = (i_index + word_shift) % 26

            #convert to character
            new_unicode = new_index + ord('A')

            new_character = chr(new_unicode)

            encrypt = encrypt + new_character
        else:
            encrypt += i
    print('Plain text: ', user_text)
    print('Encrypted text: ', encrypt)


def decryption():
    user_text = input('Enter your message to decrypt ')
    word_shift = int(input('Enter the number to shift '))
    decrypt = ' '
    for i in user_text:
        if i.isupper() or i.islower():
            #find unicode
            i_unicode = ord(i)
            i_index = ord(i) + ord('A')

            #letter shift
            new_index = (i_index - word_shift) % 26

            #convert to character
            new_unicode = new_index - ord('A')
            new_character = chr(new_unicode)
            decrypt = decrypt - new_character
        else:
            decrypt += i

    print('Ecrypted text: ', user_text)
    print('Plain text: ', decrypt)
menu = {}
menu['1'] = 'Encrypt a message'
menu['2'] = 'Decrypt a message'
menu['3'] = 'Quit'

while True:
    options = menu.keys()
    for entry in options:
         print(entry, menu[entry])
    selection = int(input('Please select '))
    if selection == 1:
        encryption()
    elif selection == 2:
        decryption()
    elif selection == 3:
        quit()
    else:
        print('Sorry, you must choose between the three options listed')
