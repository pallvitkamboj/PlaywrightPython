from cryptography.fernet import Fernet


def generate_key():
    return Fernet.generate_key()


def encrypt_password(passkey, generated_key):
    cipher = Fernet(generated_key)
    encrypted_pass = cipher.encrypt(passkey.encode())
    return encrypted_pass


def decrypt_password(enc_password, generated_key):
    cipher = Fernet(generated_key)
    dec_password = cipher.decrypt(enc_password).decode()
    return dec_password


password = "mysecretpassword"
key = generate_key()

encrypted_password = encrypt_password(password, key)
decrypted_password = decrypt_password(encrypted_password, key)

print("Original password:", password)
print("Encrypt password:", encrypted_password)
print("Decrypted password:", decrypted_password)
