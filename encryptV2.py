import os
from cryptography.fernet import Fernet
from datetime import datetime
import shutil

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
        if file == "_encrypt.py" or file == "cryptog.py" or file == 'key.txt' or file =='decrypt.py' or file =='encrypt.py' or file == "encryptv2.py" or file == "cryptog.exe" or file =='encrypt.exe' or file == 'key.key' or "key_backup" in file:
            continue
        if os.path.isfile(file):
            files.append(file)
        elif os.path.isdir(file):
            dirs.append(file)

def validate_key(key):
    """Check if the provided key is a valid Fernet key."""
    try:
        # Try to load the key to see if it's valid
        Fernet(key)
        return True
    except Exception:
        return False

def generate_backup_filename():
    """Generate a backup filename with an increasing number if necessary."""
    backup_filename = "key_backup.txt"
    counter = 1
    while os.path.exists(backup_filename):
        backup_filename = f"key_backup{counter}.txt"
        counter += 1
    return backup_filename

try:
    with open("key.txt", 'rb') as thekey:
        secretkey = thekey.read().strip()

    # Check if the key is valid
    if not validate_key(secretkey):
        print("Geçersiz anahtar bulundu.")
        user_choice = input("Yeni bir anahtar oluşturulsun mu? [Evet - Y / Hayır - N]: ").strip().lower()
        if user_choice == 'y':
            # Yedeğini al
            backup_filename = generate_backup_filename()  # Yedek dosyasının adını oluştur
            shutil.copy("key.txt", backup_filename)  # Eski key.txt'yi yedekle
            print(f"Eski anahtar yedeklendi: {backup_filename}")

            # Yeni bir anahtar oluştur ve yeni dosyaya yaz
            secretkey = Fernet.generate_key()
            with open("key.txt", 'wb') as thekey:
                thekey.write(secretkey)
            print("Yeni anahtar başarıyla oluşturuldu ve key.txt'ye kaydedildi.")
        else:
            print("Yeni anahtar oluşturulmadı. Program durduruluyor.")
            exit(0)

except FileNotFoundError:
    print("Anahtar dosyası bulunamadı. Yeni anahtar oluşturuluyor...")
    secretkey = Fernet.generate_key()

    with open("key.txt", 'wb') as thekey:
        thekey.write(secretkey)
    print("Yeni anahtar başarıyla oluşturuldu.")

def encrypt():
    main()
    total_files = len(files)
    if total_files == 0:
        print("No files to encrypt.")
        return

    for index, file in enumerate(files):
        if "key_backup" in file:
            continue  # Skip backup files
        with open(file, 'rb') as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).encrypt(contents)

        with open(file, 'wb') as thefile:
            thefile.write(contents_decrypted)

        os.rename(file, f'locked-{file}')
        
        # Log encryption activity with timestamp
        log_activity("Encrypted", file)

        # Show progress on the same line
        progress = (index + 1) / total_files * 100
        print(f"\rEncryption Progress: {progress:.2f}%", end="")

    print()  # Ensure the cursor moves to the next line after the progress updates
    files.clear()
    dirs.clear()

def decrypt():
    main()
    total_files = len(files)
    if total_files == 0:
        print("No files to decrypt.")
        return

    for index, file in enumerate(files):
        if "key_backup" in file:
            continue  # Skip backup files
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

        except:
            print(f'\rŞifre Hatalı Ya Da Dosya Şifreli Değil. [{file}]', end='')

        # Show progress on the same line
        progress = (index + 1) / total_files * 100
        print(f"\rDecryption Progress: {progress:.2f}%", end="")

    print()  # Ensure the cursor moves to the next line after the progress updates
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
