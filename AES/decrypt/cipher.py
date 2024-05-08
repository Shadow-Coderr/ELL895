import decrypt.utils as dec


def AES_decrypt(enc_msg, key):

    round_key = dec.keyExpansion(key)
    round_key = [dec.intToMatrix(round_key[i : i + 4]) for i in range(0, 44, 4)]
    enc_msg = dec.bytesToMatrix(enc_msg)
    enc_msg = dec.addRoundKey(enc_msg, round_key[10])
    # print(dec.matrixToBytes(enc_msg).hex())
    for i in range(1, 11):
        enc_msg = dec.invShiftRow(enc_msg)
        enc_msg = dec.invSubBytes(enc_msg)
        enc_msg = dec.addRoundKey(enc_msg, round_key[10 - i])
        if i != 10:
            enc_msg = dec.invMixCol(enc_msg)
    return dec.matrixToBytes(enc_msg)


def final_aes_decrypt(cipher, key, iv):
    cipher = dec.unpad(cipher)
    xr = iv
    bytes_arr = []
    for i in range(0, len(cipher), 16):
        enc_msg = cipher[i : i + 16]
        init_msg = enc_msg
        enc_msg = AES_decrypt(enc_msg, key)
        enc_msg = dec.xor(xr, enc_msg)
        bytes_arr.append(enc_msg)
        xr = init_msg
    return b"".join(bytes_arr)


if __name__ == "__main__":
    key = bytes.fromhex("0f1571c947d9e8590cb7add6af7f6798")
    plaintext = bytes.fromhex("0123456789abcdeffedcba9876543210")
    ciphertext = bytes.fromhex("ff0b844a0853bf7c6934ab4364148fb9")
    AES_decrypt(ciphertext, key).hex()
    print(plaintext == AES_decrypt(ciphertext, key))
