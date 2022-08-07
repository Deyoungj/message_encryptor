import base64



def Encrypt(key, message):
    enc = []
    for i in range(len(message)):
        key_c = key[i % len(key)]
        # a = chr((ord(message[i]) + ord(key_c)) % 256)
        # b = (ord(message[i]) + ord(key_c))
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))

    encryption = base64.urlsafe_b64encode(''.join(enc).encode()).decode()
    return encryption


