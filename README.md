# RSA_end_to_end_encryption
Light-weight wrapper on top of `cryptography` python package.

We describe a procedure allowing you to implemented a fully-customized RSA asymmetric end-to-end encryption.

Use cases:
- Encryption of email correspondence

## Requirements:

- `Python 3+` 
- `cryptography`
- `gc`

## User Guide (navigate from `bash`)

1. User A AND User B: python3 generate_rsa_keys.py

- This script will generate a unique 4048 private key as well as a corresponding public ket with SHA256 encryption stored in `.pem` files. 

- After generating the keys, User A and User B exchange `pubkey.pem`  to be able to encrypt messages send to have a secret conversation with.

2. python3 encrypt_message.py

- Specify public key of a person you would like to send message to.
- Type in secret message

A `.txt` file with an encrypted message is generated.

3. Send encrypted message (either txt or paste into email/other communication form)

4. python3 decrypt_message.py 

- You will be prompted for the password you used to generate your public-private key pair. This allows an extra layer of protection.

- A decrypted message is displayed.

## TO DO

- More streamlined user experience (reduce number of steps)

Features:

- 4048 key size
- password-protected private key

