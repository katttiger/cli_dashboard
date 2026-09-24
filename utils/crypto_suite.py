def ceasar_cipher(text, shift, decrypt=False):
    if decrypt:
        shift = -shift
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char)-start+shift) % 26+start)
        else:
            result += char
    return result


def vigenere_cipher(text, key, decrypt=False):
    result = ""
    key = key.upper()
    key_index = 0
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index % len(key)]) - ord('A')
            if decrypt:
                shift = -shift
            result += chr((ord(char) - start + shift) % 26 + start)
            key_index += 1
        else:
            result += char
    return result


def encrypt_decrypt():
    print("\n--- CRYPTOGRAPHY SUITE v1.0 ---")

    while True:
        print("\n[1] Caesar Cipher   [2] Vigenere Cipher    [3] Exit")
        choice = input("Select Method > ").strip()

        if choice == '3':
            return "Returning to main command center..."

        try:
            if choice == '1':
                text = input("Enter text: ")
                shift = int(input("Enter shift (number): "))
                mode = input("Encrypt or Decrypt? (e/d): ").lower()
                result = ceasar_cipher(text, shift, decrypt=(mode == 'd'))
                print(f"RESULT: {result}")
            elif choice == '2':
                text = input("Enter text: ")
                key = input("Enter key: ")
                mode = input("Encrypt or Decrypt? (e/d)")
                result = vignere_cipher(text, key, decrypt=(mode == 'd'))
            else:
                print("Invalid selection")
        except Exception as e:
            print(f"Error processing cipher: {e}")
