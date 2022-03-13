from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

key = b'sultanchissonobiepass'

with open('cipher_file', 'rb') as c_file:
    iv = c_file.read(16)
    ciphertext = c_file.read()

cipher = AES.new(key, AES.MODE_CBC, iv)
print(ciphertext)
plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

print(plaintext)
