from numpy import sum
from numbersletters import toLetter, toNumber

PUBLIC_KEY = ()

ENCRYPT_TERMS = ["1", "encrypt", "enc", "encr"]
DECRYPT_TERMS = ["2", "decrypt", "dec", "decr"]


def encrypt(message, public_key): #public key is (e, n)
    message = list(message.lower())
    e, n = public_key
    numerical = ""
    chunks = []

    for letter in message:
        if letter == " ":
            numerical += "99"
        else: 
            numerical += str(toNumber(letter) + 10)

    if int(numerical) > n:
        while int(numerical) > n:
            for i in range(len(numerical)):
                if int(numerical[0:i+1])>n:
                    if numerical[i] == '0':
                        chunks.append(numerical[0:i-1])
                        numerical = numerical[i-1:None]
                        break
                    else:

                        chunks.append(numerical[0:i])
                        numerical = numerical[i:None]
                    break
            continue
        chunks.append(numerical)
            
    else:
        chunks.append(numerical)  

    chunks = [((int(x)**e)%n) for x in chunks]

    return chunks

            
    
def decrypt(chunks, private_key):
    d, n = private_key
    chunks = [int(x) for x in chunks]
    chunks = [str(pow(x, d, n)) for x in chunks]
    final = ''
    string = ''
    for chunk in chunks:
        string += chunk
    while len(string) > 0:
        
        if string[0:2] == "99":
            final += " "
            string = string[2:None]
        else:
            final += toLetter(int(string[0:2])-10)
            string = string[2:None]


    return final


#en = encrypt("mr gach you said you played video games which is your favorite of all time", (941, 10194739))
enciphered = ""



t = "9397891 5490870 9871931 8654921 2835910 5395423 8527455 1737856 2825337 4081073 9729278 6087148 2040808 4489618 3675468 3474439 5482663 3966927 958610 935519 3483551 6025261"
print(t.split())
de = decrypt(t.split(), (2901413, 10194739))
print(de)
"""
en = encrypt("you said you played video games which is your favorite of all time", (941, 10194739))
print(en)
de = decrypt(en, (2901413, 10194739))
print(de)
"""

which = input("What would you like to do?\n1. Encrypt\n2. Decrypt\n")


if which.lower() in ENCRYPT_TERMS:
    message = input("What is the message?\n").lower()
    en = encrypt(message, (941, 10194739))
    enciphered = ''
    for x in en:
        enciphered += str(x) + " "
    print(enciphered)
    


if which.lower() in DECRYPT_TERMS:
    ciphertext = input("What would you like to decipher?\n")
    try:
        ciphertext = ciphertext.split()
    except:
        pass

    print(decrypt(ciphertext, (2901413, 10194739)))

input()
