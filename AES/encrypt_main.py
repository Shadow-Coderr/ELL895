import os

from PIL import Image
import numpy as np

from encrypt.cipher import AES
from encrypt.utils import getSavePath


def encryptImage(filepath):
    image = Image.open(filepath)

    image = image.convert("RGB")
    rgb_vals = np.array(image)
    image_bytes = rgb_vals.tobytes()

    key = "0e1571c947d9e8590cb7add6af7f6798"
    key = bytes.fromhex(key)

    iv = "04dcdc79931ccbd76a2f3fc94dc936ae"
    iv = bytes.fromhex(iv)

    # Create an AES cipher object with the key and IV
    cipher = AES(key, iv)

    # Encrypt the image bytes
    encrypted_bytes = cipher.encrypt(image_bytes)

    save_path = getSavePath(filepath)

    # save the encrypted image
    encrypted_image = Image.frombytes("RGB", image.size, encrypted_bytes)
    encrypted_image.save(save_path)

    encrypted_image.show()


if __name__ == "__main__":
    filepath = "image.png"
    encryptImage(filepath)
