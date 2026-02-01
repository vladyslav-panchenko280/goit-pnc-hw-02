from math import ceil

# Source: Based on popular implementations from GitHub
# https://gist.github.com/maazrk/8850d897f601492758c15dec21a054ee
# https://github.com/sukhdev01/Implementation-of-Transposition-Cipher


def encrypt_columnar(message, key):
    """
    Level 1: Simple Columnar Transposition Cipher Encryption

    Algorithm:
    1. Remove spaces from message
    2. Create a matrix with width = len(key)
    3. Fill matrix row by row with message characters
    4. Pad with 'X' if needed
    5. Sort columns based on alphabetical order of key letters
    6. Read column by column to get ciphertext
    """
    # Remove spaces and convert to uppercase
    message = message.replace(' ', '').upper()
    key = key.upper()

    # Calculate number of rows needed
    num_cols = len(key)
    num_rows = ceil(len(message) / num_cols)

    # Pad message with 'X' if needed
    message = message.ljust(num_rows * num_cols, 'X')

    # Create matrix and fill row by row
    matrix = []
    for row in range(num_rows):
        start = row * num_cols
        end = start + num_cols
        matrix.append(list(message[start:end]))

    # Create column order based on alphabetical sorting of key
    key_order = sorted(range(len(key)), key=lambda k: key[k])

    # Read columns in sorted order
    ciphertext = []
    for col_index in key_order:
        for row in matrix:
            ciphertext.append(row[col_index])

    return ''.join(ciphertext)


def decrypt_columnar(ciphertext, key):
    """
    Level 1: Simple Columnar Transposition Cipher Decryption

    Algorithm:
    1. Calculate matrix dimensions
    2. Determine column order from key
    3. Fill columns in sorted order
    4. Read row by row to get plaintext
    """
    ciphertext = ciphertext.replace(' ', '').upper()
    key = key.upper()

    # Calculate matrix dimensions
    num_cols = len(key)
    num_rows = ceil(len(ciphertext) / num_cols)

    # Create column order
    key_order = sorted(range(len(key)), key=lambda k: key[k])

    # Create empty matrix
    matrix = [['' for _ in range(num_cols)] for _ in range(num_rows)]

    # Fill matrix column by column in key order
    char_index = 0
    for col_index in key_order:
        for row in range(num_rows):
            if char_index < len(ciphertext):
                matrix[row][col_index] = ciphertext[char_index]
                char_index += 1

    # Read row by row
    plaintext = []
    for row in matrix:
        plaintext.extend(row)

    return ''.join(plaintext)


def encrypt_double_columnar(message, key1, key2):
    """
    Level 2: Double Columnar Transposition Cipher

    Algorithm:
    1. Apply first columnar transposition with key1
    2. Apply second columnar transposition with key2 on result
    """
    intermediate = encrypt_columnar(message, key1)
    final_ciphertext = encrypt_columnar(intermediate, key2)
    return final_ciphertext


def decrypt_double_columnar(ciphertext, key1, key2):
    """
    Level 2: Double Columnar Transposition Cipher Decryption

    Algorithm:
    1. Apply decryption with key2 first (reverse order)
    2. Apply decryption with key1 on result
    """
    intermediate = decrypt_columnar(ciphertext, key2)
    plaintext = decrypt_columnar(intermediate, key1)
    return plaintext




def main():
    # Read input text
    with open('input.txt', 'r') as f:
        plaintext = f.read().strip()

    # Take first sentence for demonstration
    first_sentence = plaintext.split('.')[0]

    print('LEVEL 1: Simple Columnar Transposition Cipher')
    print(f'Original text: {first_sentence}')
    print('Key: SECRET')

    # Level 1: Simple transposition
    key1 = 'SECRET'
    encrypted1 = encrypt_columnar(first_sentence, key1)
    print(f'Encrypted text: {encrypted1}')

    decrypted1 = decrypt_columnar(encrypted1, key1)
    print(f'Decrypted text: {decrypted1}')

    # Verify integrity
    original_clean = first_sentence.replace(' ', '').upper()
    decrypted_clean = decrypted1.rstrip('X')
    if original_clean == decrypted_clean:
        print('Integrity verified: Decryption successful!')
    else:
        print('Warning: Decryption does not match original')

    print('\nLEVEL 2: Double Columnar Transposition Cipher')
    print(f'Original text: {first_sentence}')
    print('Key 1: SECRET')
    print('Key 2: CRYPTO')

    # Level 2: Double transposition
    key1 = 'SECRET'
    key2 = 'CRYPTO'
    encrypted2 = encrypt_double_columnar(first_sentence, key1, key2)
    print(f'Final encrypted text: {encrypted2}')

    print('\nDECRYPTION')
    decrypted2 = decrypt_double_columnar(encrypted2, key1, key2)
    print(f'Final decrypted text: {decrypted2}')

    # Verify integrity
    decrypted_clean2 = decrypted2.rstrip('X')
    if original_clean == decrypted_clean2:
        print('Integrity verified: Double decryption successful!')
    else:
        print('Warning: Decryption does not match original')


if __name__ == '__main__':
    main()
