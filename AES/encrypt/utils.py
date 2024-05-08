import os
from functools import lru_cache

# Galois Field (GF) operations
# GF(2^8) with irreducible polynomial x^8 + x^4 + x^3 + x + 1
# Elements are represented as 8-bit binary numbers


@lru_cache(maxsize=256)  # automatically create the lookup table for mul2
def mul2(a):
    """
    Multiply a number by 2 (i.e., x) in Galois Field GF(2^8).

    """
    if (a & (1 << 7)) == 0:
        ans = a << 1
        ans = ans & 0xFF
        return ans

    ans = a << 1
    ans = ans & 0xFF
    temp = 0b00011011
    ans = ans ^ temp
    return ans


def GFadd(*args):
    """
    Performs addition in the Galois Field (GF) by XORing all the arguments.

    """
    ans = 0
    for a in args:
        ans ^= a
    return ans


def GFmul(a, b):
    """
    Multiply two numbers in Galois Field GF(2^8).

    """
    ans = 0
    for i in range(8):
        if (b & (1 << i)) != 0:
            temp = a
            for _ in range(i):
                temp = mul2(temp)
            ans = GFadd(ans, temp)
    return ans


# AES utility functions


def bytesToMatrix(byte_array):
    """
    Convert a 16-byte array into a 4x4 matrix.

    """
    matrix = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            matrix[j][i] = byte_array[i * 4 + j]
    return matrix


def matrixToBytes(matrix):
    """
    Convert a 4x4 matrix into a 16-byte array.

    """
    byte_array = ""
    for i in range(4):
        for j in range(4):
            byte_array += hex(matrix[j][i])[2:].zfill(2)
    return bytes.fromhex(byte_array)


# fmt: off
def intToMatrix(int_array):
    """
    Split 4 integers(32-bit) into a 4x4 matrix (4x4x8 = 128 bits = 16 bytes).

    """
    matrix = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        matrix[0][i], matrix[1][i], matrix[2][i], matrix[3][i] = int_array[i].to_bytes( 4, "big")
    return matrix
# fmt: on


# helper functions for encryptImage
def getSavePath(filepath):
    """
    Generate the path to save the encrypted image by prepending "enc_" to the filename
    and changing the extension to ".png".

    """
    filename = os.path.basename(filepath)
    new_filename = "enc_" + filename
    new_filename = os.path.splitext(new_filename)[0] + ".png"
    directory = os.path.dirname(filepath)
    save_path = os.path.join(directory, new_filename)
    return save_path
