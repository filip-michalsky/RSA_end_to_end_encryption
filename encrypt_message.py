from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import gc

class MsgEncryptor():

    def __init__(self):

        self.pem_path = input('Please indicate path to public key of person you would like to send message to: ')

        with open(f'{self.pem_path}','rb') as pub:
            public_key = serialization.load_pem_public_key(
            pub.read(),
            backend=default_backend()
            )
        self.public_key = public_key

    def encrypt_msg(self):

        msg = input("Please enter the message you would like to send: ")

        print('Encrypting message with SHA256 hash.')

        ciphertext = self.public_key.encrypt(
             msg.encode('utf-8'),
             padding.OAEP(
                 mgf=padding.MGF1(algorithm=hashes.SHA256()),
                 algorithm=hashes.SHA256(),
                 label=None
             )
         )

        with open('crypto_msg.txt','wb') as crypto:
            crypto.write(ciphertext)

        print(f'Message encrypted and cipher text saved!')
        print(f'encrypted message: \n {ciphertext}')

if __name__ == '__main__':
    encryptor = MsgEncryptor()
    encryptor.encrypt_msg()