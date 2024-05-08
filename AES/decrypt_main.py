from decrypt.cipher import final_aes_decrypt
from PIL import Image
import numpy as np
# from dotenv import load_dotenv
import os

# load_dotenv()


def decrypt_image(image_path):
    image = Image.open(image_path)
    image = image.convert("RGB")
    rgb_vals = np.array(image)
    encrypted_bytes = rgb_vals.tobytes()

    key = "0e1571c947d9e8590cb7add6af7f6798"
    key = bytes.fromhex(key)

    # load the IV from the environment variable
    iv = "04dcdc79931ccbd76a2f3fc94dc936ae"
    iv = bytes.fromhex(iv)

    decrypted_bytes = final_aes_decrypt(encrypted_bytes, key, iv)
    save_path = f"dec_{image_path}"
    decrypted_image = Image.frombytes("RGB", image.size, decrypted_bytes)
    decrypted_image.save(save_path)

    decrypted_image.show()


if __name__ == "__main__":
    filepath = "enc_image.png"
    decrypt_image(filepath)
