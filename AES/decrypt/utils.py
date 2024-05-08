import numpy as np

invSBox = [
    0x52,
    0x09,
    0x6A,
    0xD5,
    0x30,
    0x36,
    0xA5,
    0x38,
    0xBF,
    0x40,
    0xA3,
    0x9E,
    0x81,
    0xF3,
    0xD7,
    0xFB,
    0x7C,
    0xE3,
    0x39,
    0x82,
    0x9B,
    0x2F,
    0xFF,
    0x87,
    0x34,
    0x8E,
    0x43,
    0x44,
    0xC4,
    0xDE,
    0xE9,
    0xCB,
    0x54,
    0x7B,
    0x94,
    0x32,
    0xA6,
    0xC2,
    0x23,
    0x3D,
    0xEE,
    0x4C,
    0x95,
    0x0B,
    0x42,
    0xFA,
    0xC3,
    0x4E,
    0x08,
    0x2E,
    0xA1,
    0x66,
    0x28,
    0xD9,
    0x24,
    0xB2,
    0x76,
    0x5B,
    0xA2,
    0x49,
    0x6D,
    0x8B,
    0xD1,
    0x25,
    0x72,
    0xF8,
    0xF6,
    0x64,
    0x86,
    0x68,
    0x98,
    0x16,
    0xD4,
    0xA4,
    0x5C,
    0xCC,
    0x5D,
    0x65,
    0xB6,
    0x92,
    0x6C,
    0x70,
    0x48,
    0x50,
    0xFD,
    0xED,
    0xB9,
    0xDA,
    0x5E,
    0x15,
    0x46,
    0x57,
    0xA7,
    0x8D,
    0x9D,
    0x84,
    0x90,
    0xD8,
    0xAB,
    0x00,
    0x8C,
    0xBC,
    0xD3,
    0x0A,
    0xF7,
    0xE4,
    0x58,
    0x05,
    0xB8,
    0xB3,
    0x45,
    0x06,
    0xD0,
    0x2C,
    0x1E,
    0x8F,
    0xCA,
    0x3F,
    0x0F,
    0x02,
    0xC1,
    0xAF,
    0xBD,
    0x03,
    0x01,
    0x13,
    0x8A,
    0x6B,
    0x3A,
    0x91,
    0x11,
    0x41,
    0x4F,
    0x67,
    0xDC,
    0xEA,
    0x97,
    0xF2,
    0xCF,
    0xCE,
    0xF0,
    0xB4,
    0xE6,
    0x73,
    0x96,
    0xAC,
    0x74,
    0x22,
    0xE7,
    0xAD,
    0x35,
    0x85,
    0xE2,
    0xF9,
    0x37,
    0xE8,
    0x1C,
    0x75,
    0xDF,
    0x6E,
    0x47,
    0xF1,
    0x1A,
    0x71,
    0x1D,
    0x29,
    0xC5,
    0x89,
    0x6F,
    0xB7,
    0x62,
    0x0E,
    0xAA,
    0x18,
    0xBE,
    0x1B,
    0xFC,
    0x56,
    0x3E,
    0x4B,
    0xC6,
    0xD2,
    0x79,
    0x20,
    0x9A,
    0xDB,
    0xC0,
    0xFE,
    0x78,
    0xCD,
    0x5A,
    0xF4,
    0x1F,
    0xDD,
    0xA8,
    0x33,
    0x88,
    0x07,
    0xC7,
    0x31,
    0xB1,
    0x12,
    0x10,
    0x59,
    0x27,
    0x80,
    0xEC,
    0x5F,
    0x60,
    0x51,
    0x7F,
    0xA9,
    0x19,
    0xB5,
    0x4A,
    0x0D,
    0x2D,
    0xE5,
    0x7A,
    0x9F,
    0x93,
    0xC9,
    0x9C,
    0xEF,
    0xA0,
    0xE0,
    0x3B,
    0x4D,
    0xAE,
    0x2A,
    0xF5,
    0xB0,
    0xC8,
    0xEB,
    0xBB,
    0x3C,
    0x83,
    0x53,
    0x99,
    0x61,
    0x17,
    0x2B,
    0x04,
    0x7E,
    0xBA,
    0x77,
    0xD6,
    0x26,
    0xE1,
    0x69,
    0x14,
    0x63,
    0x55,
    0x21,
    0x0C,
    0x7D,
]
invSBox = np.array(invSBox)
invSBox = np.reshape(invSBox, (16, 16))
# print(invSBox)
sBox = [
    [99, 124, 119, 123, 242, 107, 111, 197, 48, 1, 103, 43, 254, 215, 171, 118],
    [202, 130, 201, 125, 250, 89, 71, 240, 173, 212, 162, 175, 156, 164, 114, 192],
    [183, 253, 147, 38, 54, 63, 247, 204, 52, 165, 229, 241, 113, 216, 49, 21],
    [4, 199, 35, 195, 24, 150, 5, 154, 7, 18, 128, 226, 235, 39, 178, 117],
    [9, 131, 44, 26, 27, 110, 90, 160, 82, 59, 214, 179, 41, 227, 47, 132],
    [83, 209, 0, 237, 32, 252, 177, 91, 106, 203, 190, 57, 74, 76, 88, 207],
    [208, 239, 170, 251, 67, 77, 51, 133, 69, 249, 2, 127, 80, 60, 159, 168],
    [81, 163, 64, 143, 146, 157, 56, 245, 188, 182, 218, 33, 16, 255, 243, 210],
    [205, 12, 19, 236, 95, 151, 68, 23, 196, 167, 126, 61, 100, 93, 25, 115],
    [96, 129, 79, 220, 34, 42, 144, 136, 70, 238, 184, 20, 222, 94, 11, 219],
    [224, 50, 58, 10, 73, 6, 36, 92, 194, 211, 172, 98, 145, 149, 228, 121],
    [231, 200, 55, 109, 141, 213, 78, 169, 108, 86, 244, 234, 101, 122, 174, 8],
    [186, 120, 37, 46, 28, 166, 180, 198, 232, 221, 116, 31, 75, 189, 139, 138],
    [112, 62, 181, 102, 72, 3, 246, 14, 97, 53, 87, 185, 134, 193, 29, 158],
    [225, 248, 152, 17, 105, 217, 142, 148, 155, 30, 135, 233, 206, 85, 40, 223],
    [140, 161, 137, 13, 191, 230, 66, 104, 65, 153, 45, 15, 176, 84, 187, 22],
]
sBox = np.array(sBox)


def keyExpansion(key):
    """
    Expand the 4-word key into a 44-word key.

    """
    rcon = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]

    expanded_key = [0] * 44
    for i in range(4):
        expanded_key[i] = int.from_bytes(key[4 * i : 4 * i + 4], "big")

    for i in range(4, 44):
        temp = expanded_key[i - 1]
        if i % 4 == 0:
            temp = (temp & 0xFFFFFF) << 8 | temp >> 24
            t2 = sBox[temp >> 28][temp >> 24 & 0x0F].item() << 24
            t2 |= sBox[temp >> 20 & 0x0F][temp >> 16 & 0x0F].item() << 16
            t2 |= sBox[temp >> 12 & 0x0F][temp >> 8 & 0x0F].item() << 8
            t2 |= sBox[temp >> 4 & 0x0F][temp & 0x0F].item()
            temp = t2 ^ rcon[i // 4 - 1] << 24
        expanded_key[i] = expanded_key[i - 4] ^ temp

    return expanded_key


def mul2(a):
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
    ans = 0
    for a in args:
        ans ^= a
    return ans


def GFmul(a, b):
    ans = 0
    for i in range(8):
        if (b & (1 << i)) != 0:
            temp = a
            for _ in range(i):
                temp = mul2(temp)
            ans = GFadd(ans, temp)
    return ans


def addRoundKey(state, round_key):
    return np.bitwise_xor(state, round_key).tolist()


def invMixCol(state):
    const_mat = [[14, 11, 13, 9], [9, 14, 11, 13], [13, 9, 14, 11], [11, 13, 9, 14]]
    new_state = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            sum = 0
            for k in range(4):
                sum ^= GFmul(const_mat[i][k], state[k][j])
            new_state[i][j] = sum
    return new_state


def invShiftRow(state):
    new_state = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            new_state[i][j] = state[i][(j - i) % 4]
    # print(new_state)
    return new_state


def invSubBytes(state):
    new_state = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(len(state)):
        for j in range(len(state[0])):
            x = state[i][j] >> 4
            y = state[i][j] & 15
            new_state[i][j] = invSBox[x][y]
    return new_state


def bytesToMatrix(byte_array):
    matrix = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            matrix[j][i] = byte_array[i * 4 + j]
    return matrix


def intToMatrix(int_array):
    matrix = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        matrix[0][i], matrix[1][i], matrix[2][i], matrix[3][i] = int_array[i].to_bytes(
            4, "big"
        )
    return matrix


def matrixToBytes(matrix):
    byte_array = ""
    for i in range(4):
        for j in range(4):
            byte_array += hex(matrix[j][i])[2:].zfill(2)
    return bytes.fromhex(byte_array)


def unpad(plaintext):
    pad_len = 16 - len(plaintext) % 16
    return plaintext + bytes([pad_len] * pad_len)


def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))
