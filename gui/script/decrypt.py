import base64

def Decrypt(key, encryption):
    message = base64.urlsafe_b64decode(encryption).decode()
    dec = []
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))

    # print('your massage: \n'+ ''.join(dec))
    msg = ''.join(dec)
    return msg


