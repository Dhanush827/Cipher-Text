letters='abcdefghijklmnopqrstuvwxyz'
num_letters=len(letters)
def encrypt(plaintext,key):
    ciphertext=''
    for letter in plaintext:
        letter=letter.lower()
        if not letter==' ':
            index=letters.find(letter)
            if index==-1:
                ciphertext+=letter
            else:
                new_index=index+key
                if new_index>=num_letters:
                    new_index-=num_letters
                    ciphertext+=letters[new_index]
    return ciphertext
def decrypt(ciphertext,key):
    plaintext=''
    for letter in ciphertext:
        letter=letter.lower()
        if not letter==' ':
            index=letters.find(letter)
            if index==-1:
                plaintext+=letter
            else:
                new_index=index+key
                if new_index>=0:
                    new_index+=num_letters
                plaintext+=letters[new_index]
    return plaintext
    
def encrypt_decrypt(text,user_input,key):
    result=''
    if user_input=='d':
        key=-key
    for letter in text:
        letter=letter.lower()
        if  not letter==' ':
            index=letters.find(letter)
            if index==-1:
                result+=letter
            else:
                new_index=index+key
                if new_index>=num_letters:
                    new_index-=num_letters
                elif new_index<0:
                    new_index+=num_letters
                result+=letters[new_index]
    return result
    
print('do you want to encrypt or decrypt')
user_input=input('e/d: ').lower()
print()
if user_input=='e':
    print('Encryption mode')
    print()
    key=int(input('enter the key(1 through 26): '))
    text=input('enter the text to encrypt: ')
    ciphertext=encrypt_decrypt(text,user_input,key)
    print(f'CIPHERTEXT: {ciphertext}')
elif user_input=='d':  
    print('Decryption mode')
    print()
    key=int(input('enter the key(1 through 26): '))
    text=input('enter the text to decrypt: ')
    plaintext=encrypt_decrypt(text,user_input,key)
    print(f'PLAINTEXT: {plaintext}')