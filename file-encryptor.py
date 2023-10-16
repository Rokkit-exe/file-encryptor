#!/usr/bin/env python3

# file encryptor script with Fernet

import os
import sys
from cryptography.fernet import Fernet

script_name = "file-encryptor.py"

current_path = os.getcwd()

# getting all the files in a directory and its subdirectories
def get_all_files_in_directory(dir):
    all_files = []
    for dirpath, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            if filename == "file-encryptor.py" or filename == "the-key.key":
                print("Skipping file: ", filename)
                continue
            file_path = os.path.join(dirpath, filename)
            print("Appending file: ", file_path)
            all_files.append(file_path)
    return all_files

# generate a key and save it to a file (file_name)
def generate_key():
    key = Fernet.generate_key()
    return key

def create_key_file(file_name, key):
    print("file name: ", file_name)
    print("key: ", key)
    with open(file_name, 'wb') as key_file:
        key_file.write(key)

# encrypting the file with the key
def encrypt(file, key):
    with open(file, 'rb') as f:
        data = f.read()
    print("Encrypting file: ", file)
    data_encrypted = Fernet(key).encrypt(data)
    with open(file, 'wb') as f:
        f.write(data_encrypted)

# decrypting the file with the key
def decrypt(file, key):
    with open(file, 'rb') as f:
        data = f.read()
    data_decrypted = Fernet(key).decrypt(data)
    with open(file, 'wb') as f:
        f.write(data_decrypted)

# getting the key from the file
def load_key(file_name):
    return open(file_name, 'rb').read()

# encrypting all the files in a list
def encrypt_files(files, key):
    for file in files:
        encrypt(file, key)

# decrypting all the files in a list
def decrypt_files(files, key):
    for file in files:
        decrypt(file, key)

def encryption_management():
    # getting the path of the directory to encrypt and the name of the key file
        path = input("Enter the path of the directory to encrypt: ")
        key_file = input("Enter the name of the key file: ")
        print()

        # getting all the files in the directory
        files = get_all_files_in_directory(path)
        print()
        print("Files to encrypt: ", files)
        choice = input("Do you want to continue? (y/n): ")
        if choice == "n":
            print("Exiting...")
            sys.exit(0)

        # generating the key
        print()
        print("Generating key...")
        key = generate_key()

        # creating the key file
        print()
        print("creating key file...")
        create_key_file(key_file, key)

        # encrypting the files
        print()
        print("Encrypting files...")
        encrypt_files(files, key)
        
        print()
        print("Files encrypted successfully!")

def decryption_management():
    # getting the path of the directory to decrypt and the path of the key file
        path = input("Enter the path of the directory to decrypt: ")
        key_path = input("Enter the path of the key file: ")

        # getting all the files in the directory
        files = get_all_files_in_directory(path)
        print()
        print("Files to decrypt: ", files)
        print()
        choice = input("Do you want to continue? (y/n): ")
        if choice == "n":
            print("Exiting...")
            sys.exit(0)

        # loading the key from the file
        print()
        print("Loading key...")
        key = load_key(key_path)

        # decrypting the files
        print()
        print("Decrypting files...")
        decrypt_files(files, key)

        print()
        print("Files decrypted successfully!")


# main function
def __main__():
    print("Welcome to the file encryptor script!")
    print("Please choose an option:")
    print("1. Encrypt files")
    print("2. Decrypt files")
    print("3. Exit")
    choice = input("Enter your choice: ")

    # encrypting files
    if choice == "1":
        encryption_management()
    # decrypting files
    elif choice == "2":
        decryption_management()
    # exiting
    elif choice == "3":
        print("Exiting...")
        sys.exit(0)
    else:
        print("Invalid choice!")
        sys.exit(1)


__main__()

