
import os
from cryptography.fernet import Fernet


files = []
dirs = []

def main():
    for file in os.listdir():
        if file == "cryptog.py" or file == 'key.txt' or file =='decrypt.py' or file =='encrypt.py' or file == "cryptog.exe" or file =='encrypt.exe' or file == 'key.key':
            continue
        if os.path.isfile(file):
            files.append(file)
        elif os.path.isdir(file):
            dirs.append(file)



try:
    with open("key.txt", 'rb') as thekey:
        secretkey = thekey.read()

except:
    secretkey = Fernet.generate_key()

    with open("key.txt", 'wb') as thekey:
        thekey.write(secretkey)


'''
def openDirs(dirs):
    for dir in dirs:
        filesInDir = []

        os.chdir(f'{dir}')
        for file in os.listdir():

        with open('misc.xml', 'rb') as f:
            print(f.read())

'''

def encrypt():
    main()
    for file in files:
        with open(file, 'rb') as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).encrypt(contents)


        with open(file, 'wb') as thefile:
            thefile.write(contents_decrypted)

        os.rename(file,f'locked-{file}')
    files.clear()
    dirs.clear()



def decrypt():
    main()
    for file in files:
        with open(file, 'rb') as thefile:
            contents = thefile.read()
        try:
            contents_encrypted = Fernet(secretkey).decrypt(contents)


            with open(file, 'wb') as thefile:
                thefile.write(contents_encrypted)


            if 'locked-' in file:
                newnamefile = file.replace('locked-','',1)
                os.rename(file,f'{newnamefile}')

            print('\nŞifre Çözüldü.')
        except:
            print(f'\nŞifre Hatalı Ya Da Dosya Şifreli Değil. [{file}]')
    files.clear()
    dirs.clear()

while True:
    chose =input('''
Şifrelemek   (encrypt) [1]
Şifre Çözmek (decrypt) [2]
:  ''')
    try:chose=int(chose)
    except:print('\nLütfen sadece sayı giriniz')
    if chose == 1:
        verification = input('Gerçekten şifrelemek istiyor musunuz? [Y] ')
        if verification == 'y' or verification == 'Y':encrypt(), print('\nŞifrelendi')
        else: print('\nŞifrelenmedi')
    elif chose == 2: decrypt()
    else:
        print('\nLütfen 1 veya 2 giriniz.')


