
#testing of the erasure coding
#We will do 4-2 Erasure coding


from base64 import b64decode
import sys
from decimal import *
import numpy as np


sys.setrecursionlimit(10000)
getcontext().prec = 20000


def encode(data):
    enc = data.encode("latin-1")
    # print(enc)
    data_int = int.from_bytes(enc, "little")
    return data_int


def decode(enc):
    dec = enc.to_bytes((enc.bit_length() + 7) // 8, "little")
    data = dec.decode("latin-1")
    return data


def create_parity_block(content):
    """
    p1 = a + b + c + d
    p2 = a + 4b + 6c + 8d
    """
    p1 = 0
    p2 = 0
    for i in range(len(content)):
        p1 += int(Decimal(content[i]))
        p2 += int(Decimal(content[i] * (i+1)*2))


    return p1,p2


def find_inverse(n):
    det = abs((Decimal(n[0][0]) * Decimal(n[1][1])) - (Decimal(n[0][1]) * Decimal(n[1][0])))
    n[0][0], n[1][1] = n[1][1] / det, n[0][0] / det
    n[0][1], n[1][0] = -1 * n[0][1] / det, -1 * n[1][0] / det
    return n


def find_missing(val,p1,p2):
    max_val = max(val)
    max_val = max([max_val,p1,p2])
    getcontext().prec = len(str(max_val)) * 50
    missing_val = [i for i in range(len(val)) if val[i] == 0]
    if len(missing_val) == 1:
        x = p1-sum(val)
        val[missing_val[0]] = x
    elif len(missing_val) == 2:
        c1 = Decimal(p1 - sum(val))
        v = [((i+1) * 2) * val[i] for i in range(len(val))]
        c2 = Decimal(p2 - sum(v))
        C = [[c1],[c2]]
        A = [[Decimal(1.0),Decimal(1.0)]]
        l = [Decimal((i+1)*2) for i in missing_val]
        # A = [[float(1.0),float(1.0)]]
        # l = [float((i+1)**2) for i in missing_val]
        A.append(l)
        inv_A = find_inverse(A)
        # A = np.array(A)
        # # print(A)
        # inv_A = list(np.linalg.inv(A))
        # A = np.array(A)
        # print(A)
        # inv_A = list(np.linalg.inv(A))
        
        # inv_A[0] = list(inv_A[0])
        # inv_A[1] = list(inv_A[1])
        # print(inv_A)


        A1 = []
        for i in inv_A:
            a = []
            for j in i:
                a.append(Decimal(j))
            A1.append(a)


        inv_A = A1
        # print(A1)
        X = [0,0]
        getcontext().prec = len(str(max_val)) * 1000
        X[0] = (inv_A[0][0] * C[0][0]) + (inv_A[0][1] * C[1][0])
        X[1] = (inv_A[1][0] * C[0][0]) + (inv_A[1][1] * C[1][0]) 
        val[missing_val[0]] = int(X[0])
        val[missing_val[1]] = int(X[1])
    else:
        return None


    return val


def find(content,p1,p2):
    """ 
    The content will have few missing entries and
    this will return all the content using
    Erasure Coding
    """
    enc_content = []
    for i in content:
        if i == "":
            enc_content.append(0)
        else:
            enc_content.append(encode(str(i)))
    
    if enc_content.count(0) > 2 :
        return None
    new_content = find_missing(enc_content,p1,p2)
    # print(new_content)
    for i in range(len(new_content)):
        new_content[i] = decode(new_content[i])


    return new_content
