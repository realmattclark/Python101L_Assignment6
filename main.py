import string


'''print('Main Menu:')
option_1 = int(input("Enter '1' to encrypt a message"))
option_2 = int(input("Enter '2' to decrypt a message"))
option_3 = input("Enter 'Q' to quit")'''
selection = input("Main Menu:\nEnter '1' to encrypt a message \nEnter '2' to decrypt a message \nEnter 'Q' to quit\n")


if selection == '1':  
    def encryption():
        user_text = input('Enter a brief message to encrypt ')
        word_shift = int(input('Enter a number to shift by '))
        encrypt = ' '
        for i in user_text:
            if i.isupper():
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


elif selection == '2':
    def decryption():
        user_text = input('Enter your message to decrypt ')
        word_shift = int(input('Enter the number to shift '))
        decrypt = ' '
        for i in user_text:
            if i.isupper():
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
                decrypt -= i

        print('Ecrypted text: ', user_text)
        print('Plain text: ', decrypt)

