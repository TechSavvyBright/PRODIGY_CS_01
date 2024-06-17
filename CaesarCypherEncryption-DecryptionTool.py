import getpass
import sys
import time

def caesar_cipher(sentence, shift, action):
    result = ""
    for word in sentence.split():
        for char in word:
            if char.isalpha():
                ascii_value = ord(char)
                if action == 'E':
                    shifted_ascii_value = ascii_value + shift
                else:
                    shifted_ascii_value = ascii_value - shift
                    if shifted_ascii_value < ord('a') and char.islower():
                        shifted_ascii_value += 26
                    elif shifted_ascii_value < ord('A') and char.isupper():
                        shifted_ascii_value += 26
                shifted_char = chr(shifted_ascii_value)
                result += shifted_char
            else:
                result += char
        result += " "
    return result.strip()

def main():
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()
    if choice in ['E', 'D']:
        if choice == 'E':
            sentence = input("Please input your message to encrypt: ")
            try:
                shift = int(getpass.getpass("Enter your Shift value: "))
            except Exception:
                shift = int(input("Enter your Shift value: "))
        else:
            sentence = input("Please input your encrypted message to decrypt: ")
            try:
                shift = int(getpass.getpass("Enter your Shift value: "))
            except Exception:
                shift = int(input("Enter your Shift value: "))
                        
        print("Processing: [0%]", end="")
        sys.stdout.flush()
        time.sleep(0.5)
        
        output = caesar_cipher(sentence, shift, choice)
        
        for i in range(1, 101):
            print(f"\rProcessing: [{i}%]", end="")
            sys.stdout.flush()
            time.sleep(0.01)
        
        if choice == 'E':
            print(f"\rEncrypted text: {output}")
        else:
            print(f"\rDecrypted text: {output}")
    else:
        print("Invalid choice. Please enter E or D.")

if __name__ == "__main__":
    main()
