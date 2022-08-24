#formula c=(x-n)%26

def ImageEncryption():
    path = input(r'Enter path of Image : ')
    key = int(input('Enter Key for encryption of Image : '))

    print('The path of file : ', path)
    print('Key for encryption : ', key)
    fin = open(path, 'rb')
    
    image = fin.read()
    fin.close()

    image = bytearray(image)

    for index, values in enumerate(image):
        image[index] = values ^ key
        
    fin = open(path, 'wb')
    fin.write(image)
    fin.close()
    print('Encryption Done...')

def ImageDecryption():

    path = input(r'Enter path of Image : ')
    key = int(input('Enter Key for encryption of Image : '))
    print('The path of file : ', path)
    print('Note : Encryption key and Decryption key must be same.')
    print('Key for Decryption : ', key)
    fin = open(path, 'rb')
    
    image = fin.read()
    fin.close()
    image = bytearray(image)

    for index, values in enumerate(image):
        image[index] = values ^ key

    fin = open(path, 'wb')
    fin.write(image)
    fin.close()
    print('Decryption Done...')


def encrypted(string,k):
    e_cipher = ''
    for char in string:
        if char==' ':
            e_cipher=e_cipher+char
        elif char.isupper():
            e_cipher=e_cipher+chr((ord(char)+k-65)%26+65)
        else:
            e_cipher=e_cipher+chr((ord(char)+k-97)%26+97)
    return e_cipher

def decrypted(string,k):
    d_cipher = ''
    for char in string:
        if char==' ':
            d_cipher=d_cipher+char
        elif char.isupper():
            d_cipher=d_cipher+chr((ord(char)-k-65)%26+65)
        else:
            d_cipher=d_cipher+chr((ord(char)-k-97)%26+97)
    return d_cipher
print("Enter Choice:")
print("1.Text Encryption \n2.Decryption")
choice1 = int(input())
if choice1 == 1:
    text = input("Enter the text: ")
    k = int(input("Enter the shift key: "))
    print("Enter Choice:")
    print("1.Encryption \n2.Decryption")
    choice2 = int(input())
    if choice2==1:
        e_text = encrypted(text,k)
        print("Encrypted message: ",e_text)
    elif choice2==2:
        d_text = decrypted(text,k)
        print("Decrypted message: ",d_text)
    else:
        print("Wrong Choice")
elif choice1 == 2:
    print("Enter Choice:")
    print("1.Encryption \n2.Decryption")
    choice = int(input())
    if choice==1:
        ImageEncryption()
    elif choice==2:
        ImageDecryption()
    else:
        print("Wrong Choice")
