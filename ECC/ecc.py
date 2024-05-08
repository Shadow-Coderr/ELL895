import copy
from PIL import Image
import numpy as np

import math
import random
def add(P,Q,a,p):
    # print(P)
    (x1,y1) = P
    (x2,y2) = Q
    if (P == (math.inf,math.inf)):
        return Q
    if (Q == (math.inf,math.inf)):
        return P

    if(P==Q):
        if (p%(2*y1) == 0):
            return (math.inf,math.inf)
        l = ((3*x1*x1+a)%p)*pow(2*y1,-1,p)
    else:
        if (p%(x2-x1) == 0):
            return (math.inf,math.inf)
        l = ((y2-y1)%p)*pow(x2-x1,-1,p)
    
    l = l%p
    xr = l*l%p -x1-x2
    xr = xr%p
    yr = (l*(x1-xr)%p - y1)%p
    return (xr,yr)

def sub(P,Q,a,p):
    (x1,y1) = P
    (x2,y2) = Q
    Q = (x2,-y2)
    return add(P,Q,a,p)

# def mul(P,k,a,p):
#     r = P
#     for i in range (0,k-1):
#         r = add(P,r,a,p)

#     return r
def mul(temp,n,a,p):
    res=0
    first = True
    while n > 0:
        if n & 1 == 1:
            if first:
                res = temp
                first = False
            else:
                res=add(temp,res,a,p)
        temp=add(temp,temp,a,p)
        n >>= 1
    return res
# print(mul((16,5),8,9,23))
# print(mul((2,2),203,0,211))


def modular_sqrt(a, p):

    def legendre_symbol(a, p):
        ls = pow1(a, (p - 1) // 2, p)
        return -1 if ls == p - 1 else ls
    
    if legendre_symbol(a, p) != 1:
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return p
    elif p % 4 == 3:
        return pow1(a, (p + 1) // 4, p)
    s = p - 1
    e = 0
    while s % 2 == 0:
        s //= 2
        e += 1
    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1
    x = pow1(a, (s + 1) // 2, p)
    b = pow1(a, s, p)
    g = pow1(n, s, p)
    r = e

    while True:
        t = b
        m = 0
        for m in range(r):
            if t == 1:
                break
            t = pow1(t, 2, p)

        if m == 0:
            return x

        gs = pow(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m

# Python3 program to implement Shanks Tonelli
# algorithm for finding Modular Square Roots 

# utility function to find pow(base, 
# exponent) % modulus 
def pow1(base, exponent, modulus): 

	result = 1
	base = base % modulus
	while (exponent > 0): 
		if (exponent % 2 == 1):
			result = (result * base) % modulus; 
		exponent = int(exponent) >> 1
		base = (base * base) % modulus

	return result



def koblitz_mapping(m,k,p,a,b):
    # print(1)
    for i in range(1,k):
        # print(i)
        x=m*k + i
        y=pow1(x,3,p) + a*x + b
        y%=p
        y=modular_sqrt(y,p)
        if(y!=None):
           return (x,y)
    return (-1,-1)



def encrypt(M,Pb,G,a,p):
    k = 41
    C1 = mul(G,k,a,p)
    # print(C1,"hi")
    # print(M)
    C2 = add(M,mul(Pb,k,a,p),a,p)
    return (C1,C2)

def decrypt(C1,C2,nb,a,p):
    return sub(C2,mul(C1,nb,a,p),a,p)

# print(add((3,10),(9,7),1,23))
# print(encrypt((112,26),(197,167),(2,2),0,257))
# print(decrypt((136,128),(246,174),101,0,257))

p =  0xE95E4A5F737059DC60DFC7AD95B3D8139515620F
a = 0x340E7BE2A280EB74E2BE61BADA745D97E8F7C300
b= 0x1E589A8595423412134FAA2DBDEC95C8D8675E58
G= (0xBED5AF16EA3F6A4F62938C4631EB5AF7BDBCDBC3,0x1667CB477A1A8EC338F94741669C976316DA6321)
n= 0xE95E4A5F737059DC60DF5991D45029409E60FC09
nb = random.randint(1,n-1)
k = 50
Pb  = mul(G,nb,a,p)

# print(p)
mlength = p//k-1
blocksize = mlength.bit_length()//8

def pad(block):
    a = len(block)%blocksize

    for i in range(0,blocksize-a):
        block+=(bytes([blocksize-a]))
    return block

def bytoblocks1(byt):
    a = []
    for i in range(len(byt)//blocksize):
        b = byt[blocksize*i:blocksize*(i+1)]
        a.append(b)
    return a


deciphlen = (p.bit_length()//8)*4
def bytoblocks2(byt):
    a = []
    for i in range(len(byt)//deciphlen):
        b = byt[deciphlen*i:deciphlen*(i+1)]
        a.append(b)
    return a


def encryptImage():
    image = Image.open('img2.png')

    image = image.convert("RGB")
    rgb_vals = np.array(image)
    image_bytes = rgb_vals.tobytes()

    #encrypt the image bytes
    encrypted_bytes = encryptftext(pad(image_bytes))
    print("encrypted the image")

    # save_path = 'encrypted-imagersa.png'

    # ave the encrypted image
    encrypted_image = Image.frombytes("RGB", image.size, encrypted_bytes)
    # encrypted_image.save(save_path)
    with open('encrypted-imageecc.png','wb') as f :
        f.write(encrypted_bytes)
    encrypted_image.show()

    with open('encrypted-imageecc.png','rb') as f :
        encrypted_bytes = f.read()
    print("encrypted image opened")
    decrypted_bytes = decryptftext(encrypted_bytes)

    decrypted_image = Image.frombytes("RGB", image.size, decrypted_bytes)
    decrypted_image.show()
    decrypted_image.save('decrypted-imageecc.png')

def encryptftext(ptext):
    blockarr = bytoblocks1(ptext)
    c = []
    # print(k)
    for i in blockarr:
        c.append(koblitz_mapping(int.from_bytes(i,'big'),k,p,a,b))
    print("Found all the points")
    r = []
    for i in c:
        r.append(encrypt(i,Pb,G,a,p))
    b1 = []
    print("Encrypted all the points")
    for i in r:
        b1.append(i[0][0].to_bytes(p.bit_length()//8,'big'))
        b1.append(i[0][1].to_bytes(p.bit_length()//8,'big'))
        b1.append(i[1][0].to_bytes(p.bit_length()//8,'big'))
        b1.append(i[1][1].to_bytes(p.bit_length()//8,'big'))
    return b''.join(b1)

def decryptftext(ctext):
    blockarr = bytoblocks2(ctext)
    c = []

    for i in range(len(blockarr)):
        c.append([int.from_bytes(blockarr[i][0:deciphlen//4],'big'),
        int.from_bytes(blockarr[i][deciphlen//4:deciphlen//2],'big'),
        int.from_bytes(blockarr[i][deciphlen//2:3*deciphlen//4],'big'),
        int.from_bytes(blockarr[i][3*deciphlen//4:deciphlen],'big')])
    d = []
    
    for i in range(len(c)):
        C1 = (c[i][0],c[i][1])
        C2 = (c[i][2],c[i][3])
        d.append(decrypt(C1,C2,nb,a,p)[0]//k)
    e = []
    print("points found after decryption")
    
    blocksize = mlength.bit_length()//8
    for i in d:
        e.append(i.to_bytes(blocksize,'big'))
    print("bytes found after decryption")
    return b''.join(e)
    
encryptImage()