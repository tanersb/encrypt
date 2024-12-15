# Encrypt - File Encryption and Decryption

## Description
`Encrypt` is a Python-based tool that allows you to encrypt and decrypt files in your current directory. Using the `cryptography.fernet` library, it ensures secure encryption with generated keys, making it suitable for protecting sensitive files. The script also provides the ability to rename files with a prefix (e.g., `locked-`) after encryption.

## Features
- **File Encryption:** Encrypts all files (except specified ones) in the current directory.
- **File Decryption:** Decrypts previously encrypted files.
- **Key Management:** Automatically generates and saves a key for encryption and decryption.

## Prerequisites
- Python 3.6 or later
- `cryptography` library (install it using `pip install cryptography`)

## Usage
1. Clone or download the repository containing the script.
2. Ensure all files you want to encrypt or decrypt are in the same directory as the script.
3. Run the script and follow the prompts.

### Command-line Options
- **Encrypt Files**
    1. Choose option `1` when prompted.
    2. Confirm the operation by entering `Y` or `y`.
    3. All eligible files will be encrypted and renamed with the `locked-` prefix.

- **Decrypt Files**
    1. Choose option `2` when prompted.
    2. The script will attempt to decrypt all encrypted files.

### Key File
- A key file (`key.txt`) will be generated during the first run.
- Ensure the `key.txt` file remains in the directory; it is required for decrypting files.

## Example
```bash
python cryptog.py

# Output:
# Şifrelemek   (encrypt) [1]
# Şifre Çözmek (decrypt) [2]
# :
```

### Encryption Example:
```text
Şifrelemek   (encrypt) [1] 
Gerçekten şifrelemek istiyor musunuz? [Y] 

# Output:
# Şifrelendi
```

### Decryption Example:
```text
Şifre Çözmek (decrypt) [2] 

# Output:
# Şifre Çözüldü.
```

## Files Ignored by the Script
The following files are not encrypted or decrypted:
- `cryptog.py`
- `key.txt`
- `decrypt.py`
- `encrypt.py`
- `cryptog.exe`
- `encrypt.exe`
- `key.key`

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Disclaimer
This script is provided for educational purposes. Use it responsibly. The author takes no responsibility for any damage or data loss resulting from the use of this script.

