from PIL import Image
import random

def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path).convert("RGBA")
    pixels = list(image.getdata())

    random.seed(key)
    random.shuffle(pixels)  # Swap pixel positions randomly

    # Apply XOR to scramble colors
    encrypted_pixels = [
        ((r ^ key) % 256, (g ^ key) % 256, (b ^ key) % 256, a)
        for (r, g, b, a) in pixels
    ]

    encrypted_img = Image.new("RGBA", image.size)
    encrypted_img.putdata(encrypted_pixels)
    encrypted_img.save(output_path)
    print(f"Encrypted image saved as {output_path}")

def decrypt_image(input_path, output_path, key):
    image = Image.open(input_path).convert("RGBA")
    encrypted_pixels = list(image.getdata())

    # Reverse XOR
    decrypted_pixels = [
        ((r ^ key) % 256, (g ^ key) % 256, (b ^ key) % 256, a)
        for (r, g, b, a) in encrypted_pixels
    ]

    # Reverse shuffle
    random.seed(key)
    indices = list(range(len(decrypted_pixels)))
    random.shuffle(indices)

    unshuffled_pixels = [None] * len(decrypted_pixels)
    for i, idx in enumerate(indices):
        unshuffled_pixels[idx] = decrypted_pixels[i]

    decrypted_img = Image.new("RGBA", image.size)
    decrypted_img.putdata(unshuffled_pixels)
    decrypted_img.save(output_path)
    print(f"Decrypted image saved as {output_path}")
