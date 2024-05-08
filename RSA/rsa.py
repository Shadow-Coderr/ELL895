import math
import random
import copy
from PIL import Image
import numpy as np

def keygen(p,q):
    n = p*q
    phi = (p-1)*(q-1)
    e=0
    for i in range(phi-1,1,-1):
        if(math.gcd(phi,i) == 1):
            e = i
            break
    d = pow(e,-1,phi)
    return (e,d,n)

def encrypt(m,e,n):
    # e = 7
    # n = 187
    return pow(m,e,n)

def decrypt(M,d,n):
    # d = 23
    # n = 187
    return pow(M,d,n)


def pad(block):
    a = len(block)%255

    for i in range(0,255-a):
        block+=(bytes([255-a]))
    return block

def bytoblocks1(byt):
    a = []
    for i in range(len(byt)//255):
        b = byt[255*i:255*(i+1)]
        a.append(b)
    return a
def bytoblocks2(byt):
    a = []
    for i in range(len(byt)//257):
        b = byt[257*i:257*(i+1)]
        a.append(b)
    return a

p = 253184448058558846829292648641146356604525749294150845807324544529232909394816575249581415968278207285558453109547438253228135737433173340801142197898333508751332848245175161901835994425788135637491139934844528262468488105066627947997705283562546556281697626648395348678937757226166713527175998930383944885837
q = 305286158982609699957943631001915717196848799689283466742487875294132658957447490246070959496953642435237728750612526290549245813118403349058105419823823964963420130758075913829759489248696249119018716432952116915964157639888983381875798294068995264726425190772813604848870810904669075720189143167721333273687


e,d,n = keygen(p,q)
print("generated key")

def encryptImage():
    image = Image.open('img2.png')

    image = image.convert("RGB")
    rgb_vals = np.array(image)
    image_bytes = rgb_vals.tobytes()

    #encrypt the image bytes
    encrypted_bytes = encryptftext(pad(image_bytes))

    # save_path = 'encrypted-imagersa.png'

    # ave the encrypted image
    encrypted_image = Image.frombytes("RGB", image.size, encrypted_bytes)
    # encrypted_image.save(save_path)
    with open('encrypted_imagersa.png','wb') as f :
        f.write(encrypted_bytes)
    encrypted_image.show()

    with open('encrypted_imagersa.png','rb') as f :
        encrypted_bytes = f.read()
    decrypted_bytes = decryptftext(encrypted_bytes)

    decrypted_image = Image.frombytes("RGB", image.size, decrypted_bytes)
    decrypted_image.show()
    decrypted_image.save('decrypted_imagersa.png')



def encryptftext(ptext):
    blockarr = bytoblocks1(ptext)
    c = []
    for i in blockarr:
        c.append(encrypt(int.from_bytes(i,byteorder='big'),e,n))
    r = []
    for i in c:
        r.append(i.to_bytes(257,byteorder='big'))
    encrypted_text = b''.join(r)       
    return encrypted_text
    

def decryptftext(ctext):
    blockarr = bytoblocks2(ctext)
    p = []
    for i in blockarr:
        p.append(decrypt(int.from_bytes(i,byteorder='big'),d,n))
    r = []
    for i in p:
        r.append(i.to_bytes(255,byteorder='big'))
    decrypted_text = b''.join(r)  
    return decrypted_text



encryptImage()