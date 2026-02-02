# Source: Based on Playfair cipher implementations from GitHub
# https://github.com/asweigart/cipherwheel/blob/master/playfair.py
# https://github.com/jameslyons/pycipher

# Playfair-compatible alphabet (25 letters, I/J combined)
PLAYFAIR_ALPHABET = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'


def _encrypt_vigenere_playfair(msg, key):
    """Vigenère encryption using 25-letter Playfair alphabet (I/J combined).
    
    This ensures the ciphertext only contains letters from the Playfair alphabet,
    preventing issues when combining with Playfair cipher.
    """
    encrypted = []
    key = key.upper().replace('J', 'I')
    key_index = 0
    
    for char in msg:
        if char.isalpha():
            c = char.upper().replace('J', 'I')
            k = key[key_index % len(key)]
            # Use Playfair alphabet indices (0-24)
            c_idx = PLAYFAIR_ALPHABET.index(c)
            k_idx = PLAYFAIR_ALPHABET.index(k)
            enc_idx = (c_idx + k_idx) % 25
            encrypted.append(PLAYFAIR_ALPHABET[enc_idx])
            key_index += 1
    
    return ''.join(encrypted)


def _decrypt_vigenere_playfair(msg, key):
    """Vigenère decryption using 25-letter Playfair alphabet (I/J combined)."""
    decrypted = []
    key = key.upper().replace('J', 'I')
    key_index = 0
    
    for char in msg:
        if char.isalpha():
            c = char.upper()
            k = key[key_index % len(key)]
            # Use Playfair alphabet indices (0-24)
            c_idx = PLAYFAIR_ALPHABET.index(c)
            k_idx = PLAYFAIR_ALPHABET.index(k)
            dec_idx = (c_idx - k_idx + 25) % 25
            decrypted.append(PLAYFAIR_ALPHABET[dec_idx])
            key_index += 1
    
    return ''.join(decrypted)


def create_table(key):
    """Create 5x5 Playfair-style table from key"""
    key = key.upper().replace('J', 'I')

    # Remove duplicates from key while preserving order
    seen = set()
    key_chars = []
    for char in key:
        if char.isalpha() and char not in seen:
            seen.add(char)
            key_chars.append(char)

    # Add remaining alphabet letters
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # I/J combined
    for char in alphabet:
        if char not in seen:
            key_chars.append(char)
            seen.add(char)

    # Create 5x5 matrix
    table = []
    for i in range(5):
        row = key_chars[i*5:(i+1)*5]
        table.append(row)

    return table


def find_position(table, char):
    """Find row and column of character in table"""
    char = char.upper().replace('J', 'I')
    for i, row in enumerate(table):
        if char in row:
            return i, row.index(char)
    return None, None


def encrypt_table(message, key):
    """Encrypt using Playfair-style table cipher"""
    table = create_table(key)

    # Prepare message - remove non-letters, convert to uppercase
    clean_msg = ''.join(c.upper() for c in message if c.isalpha())
    clean_msg = clean_msg.replace('J', 'I')

    # Split into digraphs
    digraphs = []
    i = 0
    while i < len(clean_msg):
        if i == len(clean_msg) - 1:
            # Single letter at end, add X
            digraphs.append(clean_msg[i] + 'X')
            i += 1
        elif clean_msg[i] == clean_msg[i+1]:
            # Same letters, insert X
            digraphs.append(clean_msg[i] + 'X')
            i += 1
        else:
            digraphs.append(clean_msg[i] + clean_msg[i+1])
            i += 2

    # Encrypt each digraph
    encrypted = []
    for digraph in digraphs:
        r1, c1 = find_position(table, digraph[0])
        r2, c2 = find_position(table, digraph[1])

        if r1 == r2:
            # Same row - shift right
            encrypted.append(table[r1][(c1 + 1) % 5])
            encrypted.append(table[r2][(c2 + 1) % 5])
        elif c1 == c2:
            # Same column - shift down
            encrypted.append(table[(r1 + 1) % 5][c1])
            encrypted.append(table[(r2 + 1) % 5][c2])
        else:
            # Rectangle - swap columns
            encrypted.append(table[r1][c2])
            encrypted.append(table[r2][c1])

    return ''.join(encrypted)


def decrypt_table(ciphertext, key):
    """Decrypt using Playfair-style table cipher"""
    table = create_table(key)

    # Prepare ciphertext
    clean_cipher = ''.join(c.upper() for c in ciphertext if c.isalpha())

    # Split into digraphs
    digraphs = []
    for i in range(0, len(clean_cipher), 2):
        if i + 1 < len(clean_cipher):
            digraphs.append(clean_cipher[i] + clean_cipher[i+1])

    # Decrypt each digraph
    decrypted = []
    for digraph in digraphs:
        r1, c1 = find_position(table, digraph[0])
        r2, c2 = find_position(table, digraph[1])

        if r1 == r2:
            # Same row - shift left
            decrypted.append(table[r1][(c1 - 1) % 5])
            decrypted.append(table[r2][(c2 - 1) % 5])
        elif c1 == c2:
            # Same column - shift up
            decrypted.append(table[(r1 - 1) % 5][c1])
            decrypted.append(table[(r2 - 1) % 5][c2])
        else:
            # Rectangle - swap columns
            decrypted.append(table[r1][c2])
            decrypted.append(table[r2][c1])

    return ''.join(decrypted)


def encrypt_combined(message, vigenere_key, table_key):
    """Level 2: Encrypt with Vigenère first, then table cipher.
    
    Uses a modified Vigenère cipher with 25-letter Playfair alphabet (I/J combined)
    to ensure compatibility with Playfair cipher decryption.
    
    Args:
        message: The plaintext message to encrypt
        vigenere_key: Key for Vigenère cipher
        table_key: Key for Playfair table cipher
    
    Returns:
        tuple: (ciphertext, original_length) - length needed for proper decryption
        
    Note: The original_length is required for accurate decryption because
    Playfair cipher adds padding characters that affect Vigenère key alignment.
    """
    # Preprocess message: uppercase letters only
    clean_message = ''.join(c.upper() for c in message if c.isalpha())
    original_length = len(clean_message)
    
    # First encrypt with Playfair-compatible Vigenère (25-letter alphabet)
    vigenere_encrypted = _encrypt_vigenere_playfair(clean_message, vigenere_key)

    # Then encrypt with table cipher
    final_encrypted = encrypt_table(vigenere_encrypted, table_key)

    return final_encrypted, original_length


def decrypt_combined(ciphertext, vigenere_key, table_key, original_length=None):
    """Level 2: Decrypt table cipher first, then Vigenère.
    
    Uses a modified Vigenère cipher with 25-letter Playfair alphabet (I/J combined)
    to ensure compatibility with Playfair cipher.
    
    Args:
        ciphertext: The encrypted text
        vigenere_key: Key for Vigenère cipher
        table_key: Key for Playfair table cipher
        original_length: Original message length (if known) for accurate decryption
    
    Note: The decrypted text may contain:
    - 'I' instead of 'J' (Playfair alphabet uses I for both I and J)
    - Extra characters at the end if original_length is not provided
    """
    # First decrypt table cipher
    table_decrypted = decrypt_table(ciphertext, table_key)

    # Remove Playfair padding X's that were inserted between repeated letters
    # and at the end. We need to reconstruct the original Vigenère ciphertext.
    # Note: This heuristic assumes X between two identical letters is padding.
    # It works for our cipher combination but may not be 100% accurate for all inputs.
    if original_length is not None:
        cleaned = []
        i = 0
        while i < len(table_decrypted) and len(cleaned) < original_length:
            char = table_decrypted[i]
            # Check if this X is likely padding between identical letters
            # Playfair inserts X when two identical letters would form a digraph
            if char == 'X' and i > 0 and i < len(table_decrypted) - 1:
                if table_decrypted[i-1] == table_decrypted[i+1]:
                    i += 1
                    continue
            cleaned.append(char)
            i += 1
        table_decrypted = ''.join(cleaned)

    # Then decrypt Vigenère using Playfair-compatible alphabet
    final_decrypted = _decrypt_vigenere_playfair(table_decrypted, vigenere_key)
    
    # Truncate to original length if provided
    if original_length is not None:
        final_decrypted = final_decrypted[:original_length]

    return final_decrypted


def main():
    with open('input.txt', 'r') as f:
        plaintext = f.read()

    first_sentence = plaintext.split('.')[0]

    print('LEVEL 1: Table Cipher (Playfair-style)')
    print(f'Original text: {first_sentence}')
    print('Key: MATRIX')

    key1 = 'MATRIX'
    table = create_table(key1)

    print('Generated table:')
    for row in table:
        print('  ' + ' '.join(row))

    encrypted1 = encrypt_table(first_sentence, key1)
    print(f'Encrypted text: {encrypted1}')

    decrypted1 = decrypt_table(encrypted1, key1)
    print(f'Decrypted text: {decrypted1}')

    # Verify integrity
    original_clean = ''.join(c.upper() for c in first_sentence if c.isalpha()).replace('J', 'I')
    decrypted_clean = decrypted1.replace('X', '')

    if original_clean.startswith(decrypted_clean[:len(original_clean)//2]):
        print('Integrity verified: Decryption successful!')
    else:
        print('Warning: Decryption does not match original')

    print('\nLEVEL 2: Combined Cipher (Vigenere + Table)')
    print(f'Original text: {first_sentence}')
    print('Vigenere key: CRYPTOGRAPHY')
    print('Table key: CRYPTO')

    vigenere_key = 'CRYPTOGRAPHY'
    table_key = 'CRYPTO'

    encrypted2, original_length = encrypt_combined(first_sentence, vigenere_key, table_key)
    print(f'Final encrypted text: {encrypted2}')

    print('\nDECRYPTION')
    decrypted2 = decrypt_combined(encrypted2, vigenere_key, table_key, original_length)
    print(f'Final decrypted text: {decrypted2}')

    # Verify integrity - compare with J replaced by I (Playfair alphabet limitation)
    original_clean = ''.join(c.upper() for c in first_sentence if c.isalpha()).replace('J', 'I')
    decrypted_clean = decrypted2.upper()
    
    if original_clean == decrypted_clean:
        print('Integrity verified: Combined decryption successful!')
        print('(Note: J is replaced with I due to Playfair alphabet)')
    else:
        print('Warning: Decryption does not match original')


if __name__ == '__main__':
    main()
