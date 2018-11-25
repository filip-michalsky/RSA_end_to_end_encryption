from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

import gc

class RSA_key_gen():

    def __init__(self):

        self.person = input('What is your name? ')
        self.save_pass =  input("Please enter one-time pass for saving credentials. SAVE IT. This won't be restored. ")


    def generate_pem(self):

        print('Generating your private key...')
        private_key = rsa.generate_private_key(
             public_exponent=65537,
             key_size=4048,
             backend=default_backend())

        chosen_pass = self.save_pass

        # serialize the key for saving
        pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(chosen_pass.encode('utf-8'))
         )

        # save key
        print('Saving to pem file...')
        with open(f'{self.person}_key.pem','w') as f:
            f.write(pem.decode("utf-8"))

        
        print('Done!')

        print('Generating public keys...')

        public_key = private_key.public_key()

        pubkey = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
         )
        
        print(f'You public key is: \n {pubkey.decode("utf-8")}')

        print('Saving the public key to file...')

        with open(f'pubkey.pem','w') as f:
            f.write(pubkey.decode('utf-8'))

        print('Public key saved as well!')
        
        del pem
        gc.collect()

if __name__ == '__main__':
    keygen = RSA_key_gen()
    keygen.generate_pem()