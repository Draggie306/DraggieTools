import random

# First, define the plaintext that you want to encrypt
plaintext = [1,0,1,0,1,1,0,1]


def generate_key(length):
  key = []
  for i in range(length):
    key.append(random.randint(0, 1))
  return key

def encrypt(plaintext, key):
  ciphertext = []
  for i in range(len(plaintext)):
    ciphertext.append(int(plaintext[i]) ^ key[i])
  return ciphertext

def decrypt(ciphertext, key):
  plaintext = []
  for i in range(len(ciphertext)):
    plaintext.append(ciphertext[i] ^ key[i])
  return plaintext

x = decrypt([67, 100, 96, 111, 114], [0, 0, 0, 0, 1])
print(f"{x}")

# First, define the plaintext that you want to encrypt
plaintext = list("Beans")

# Convert the characters in the plaintext to ASCII integers
plaintext = [ord(c) for c in plaintext]

# Generate a random key of the same length as the plaintext
key = generate_key(len(plaintext))

# Encrypt the plaintext
ciphertext = encrypt(plaintext, key)

# The ciphertext is now a list of integers that can be transmitted securely
print(ciphertext)

# To decrypt the ciphertext, you will need the key that was used to encrypt it
decrypted_plaintext = decrypt(ciphertext, key)

# Convert the decrypted plaintext back to a string
decrypted_plaintext = "".join(chr(c) for c in decrypted_plaintext)

# Check that the decrypted plaintext is the same as the original
assert decrypted_plaintext == "Beans"
