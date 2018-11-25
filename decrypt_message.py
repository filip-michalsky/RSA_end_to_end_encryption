from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import gc

class MsgDecryptor():

    def __init__(self):

        self.private_key = input('Please indicate path to your private key: ')
        self.passw = input('Please enter password to your private key: ')
        self.msg_path = input('Please input path to your encoded txt message: ')

    def decrypt_msg(self):

        with open(f"{self.private_key}", "rb") as key_file:
         private_key = serialization.load_pem_private_key(
             key_file.read(),
             password=self.passw.encode("utf-8"), # password used to save the private key
             backend=default_backend()
         )

         with open(f'{self.msg_path}','rb') as msg_crypto:
            ciphertext = msg_crypto.read()

         plaintext = private_key.decrypt(
             ciphertext,
             padding.OAEP(
                 mgf=padding.MGF1(algorithm=hashes.SHA256()),
                 algorithm=hashes.SHA256(),
                 label=None
             )
         )

         print('Message received:','\n', plaintext.decode('utf-8'))




if __name__ == '__main__':
    decryptor = MsgDecryptor()
    decryptor.decrypt_msg()