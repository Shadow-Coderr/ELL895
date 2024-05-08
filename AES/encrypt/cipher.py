from . import transform
from .utils import bytesToMatrix, intToMatrix, matrixToBytes
import time


class AES:
    """
    AES cipher class.
    - Encrypts plaintext using the AES algorithm.
    - CBC mode is used for encryption.
    - The key and IV are provided by the user and must be 16 bytes long.

    """

    def __init__(self, key, iv, verbose=True):
        self.key = key
        self.iv = iv
        self.verbose = verbose

        # Check if the key and IV are 16 bytes long
        if len(key) != 16 or len(iv) != 16:
            raise ValueError("Key and IV must be 16 bytes long.")

        self._expanded_key = transform.keyExpansion(key)
        self._expanded_key_matrix = [
            intToMatrix(self._expanded_key[i : i + 4]) for i in range(0, 44, 4)
        ]

    def encrypt(self, plaintext):
        """
        Encrypts the plaintext using the AES algorithm in CBC mode.

        """
        plaintext = self._pad(plaintext)
        if self.verbose:
            print("Number of blocks: ", len(plaintext) // 16)
            start = time.time()

        ciphertext = []
        prev = self.iv
        for i in range(0, len(plaintext), 16):
            block = plaintext[i : i + 16]
            block = self._xor(block, prev)
            prev = self._encrypt_block(block)
            ciphertext.append(prev)
            if self.verbose and i % (16 * (len(plaintext) // 320)) == 0:
                print(
                    "Progress: ",
                    round(i / len(plaintext) * 100, 2),
                    "%",
                    "\tTime: ",
                    round(time.time() - start, 4),
                    "s",
                )

        return b"".join(ciphertext)

    # Private methods

    def _encrypt_block(self, plaintext):
        """
        Encrypts a single block of plaintext using the AES algorithm.

        """
        state = bytesToMatrix(plaintext)
        state = transform.addRoundKey(state, self._expanded_key_matrix[0])

        for i in range(1, 10):
            state = transform.subBytes(state)
            state = transform.shiftRows(state)
            state = transform.mixColumns(state)
            state = transform.addRoundKey(state, self._expanded_key_matrix[i])

        state = transform.subBytes(state)
        state = transform.shiftRows(state)
        state = transform.addRoundKey(state, self._expanded_key_matrix[10])

        return matrixToBytes(state)

    def _xor(self, a, b):
        """
        XORs two byte strings.

        """
        return bytes(x ^ y for x, y in zip(a, b))

    def _pad(self, plaintext):
        """
        Pads the plaintext to be a multiple of 16 bytes.

        """
        pad_len = 16 - len(plaintext) % 16
        return plaintext + bytes([pad_len] * pad_len)
