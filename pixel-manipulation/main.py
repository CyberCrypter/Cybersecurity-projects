from encryptor import encrypt_image, decrypt_image

def main():
    print("=== Image Encryption Tool ===")
    print("1. Encrypt an image")
    print("2. Decrypt an image")

    choice = input("Choose an option (1/2): ").strip()

    input_path = input("Enter input image path: ")
    output_path = input("Enter output image path: ")
    
    try:
        key = int(input("Enter encryption/decryption key (integer): "))
    except ValueError:
        print("Invalid key! Must be an integer.")
        return

    if choice == "1":
        encrypt_image(input_path, output_path, key)
    elif choice == "2":
        decrypt_image(input_path, output_path, key)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
