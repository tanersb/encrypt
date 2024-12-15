import os
from cryptography.fernet import Fernet
from datetime import datetime

files = []
dirs = []

# Log directory setup
log_dir = "log"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Log file setup
log_file = os.path.join(log_dir, "activity_log.txt")

def log_activity(action, filename):
    """Log the file action (encrypt or decrypt) with timestamp to a log file."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Current date and time
    with open(log_file, 'a') as log:
        log.write(f"{timestamp} - {action}: {filename}\n")

def main():
    for file in os.listdir():
        if file == "cryptog.py" or file == 'key.txt' or file =='decrypt.py' or file =='encrypt.py' or file == "encryptv2.py" or file == "cryptog.exe" or file =='encrypt.exe' or file == 'key.key':
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

def encrypt():
    main()
    for file in files:
        with open(file, 'rb') as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).encrypt(contents)

        with open(file, 'wb') as thefile:
            thefile.write(contents_decrypted)

        os.rename(file, f'locked-{file}')
        
        # Log encryption activity with timestamp
        log_activity("Encrypted", file)

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
                newnamefile = file.replace('locked-', '', 1)
                os.rename(file, f'{newnamefile}')
                
            # Log decryption activity with timestamp
            log_activity("Decrypted", file)

            print('\nŞifre Çözüldü.')
        except:
            print(f'\nŞifre Hatalı Ya Da Dosya Şifreli Değil. [{file}]')

    files.clear()
    dirs.clear()

while True:
    chose = input('''
Şifrelemek   (encrypt) [1]
Şifre Çözmek (decrypt) [2]
:  ''')
    try:
        chose = int(chose)
    except:
        print('\nLütfen sadece sayı giriniz')
    if chose == 1:
        verification = input('Gerçekten şifrelemek istiyor musunuz? [Y] ')
        if verification == 'y' or verification == 'Y':
            encrypt()
            print('\nŞifrelendi')
        else:
            print('\nŞifrelenmedi')
    elif chose == 2:
        decrypt()
    else:
        print('\nLütfen 1 veya 2 giriniz.')
