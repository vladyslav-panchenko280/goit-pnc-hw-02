import string
from collections import Counter
from math import gcd
from functools import reduce


def encrypt_vigenere(msg, key):
    """Encrypt using standard Vigenere cipher - key is used only for letters"""
    encrypted_text = []
    key = key.upper()
    key_index = 0

    for char in msg:
        if char.isupper():
            k = key[key_index % len(key)]
            # Standard Vigenere formula: Ei = (Pi + Ki) mod 26
            encrypted_char = chr((ord(char) - ord('A') + ord(k) - ord('A')) % 26 + ord('A'))
            encrypted_text.append(encrypted_char)
            key_index += 1
        elif char.islower():
            k = key[key_index % len(key)]
            # Standard Vigenere formula for lowercase
            encrypted_char = chr((ord(char) - ord('a') + ord(k) - ord('A')) % 26 + ord('a'))
            encrypted_text.append(encrypted_char)
            key_index += 1
        else:
            # Non-alphabetic characters pass through unchanged
            encrypted_text.append(char)

    return "".join(encrypted_text)


def decrypt_vigenere(msg, key):
    """Decrypt using standard Vigenere cipher - key is used only for letters"""
    decrypted_text = []
    key = key.upper()
    key_index = 0

    for char in msg:
        if char.isupper():
            k = key[key_index % len(key)]
            # Standard Vigenere formula: Di = (Ei - Ki + 26) mod 26
            decrypted_char = chr((ord(char) - ord('A') - (ord(k) - ord('A')) + 26) % 26 + ord('A'))
            decrypted_text.append(decrypted_char)
            key_index += 1
        elif char.islower():
            k = key[key_index % len(key)]
            # Standard Vigenere formula for lowercase
            decrypted_char = chr((ord(char) - ord('a') - (ord(k) - ord('A')) + 26) % 26 + ord('a'))
            decrypted_text.append(decrypted_char)
            key_index += 1
        else:
            # Non-alphabetic characters pass through unchanged
            decrypted_text.append(char)

    return "".join(decrypted_text)

# Level 2: Cryptanalysis functions (based on dmamakas2000/cryptanalysis-python)
# Source: https://github.com/dmamakas2000/cryptanalysis-python

def kasiski_examination(ciphertext, min_seq_length=3, max_seq_length=5):
    """Kasiski examination to find likely key length by analyzing repeated sequences"""
    clean_text = ''.join(c.upper() for c in ciphertext if c.isalpha())

    # Find repeated sequences
    repeated_sequences = {}

    for length in range(min_seq_length, max_seq_length + 1):
        for i in range(len(clean_text) - length):
            sequence = clean_text[i:i+length]
            if sequence in repeated_sequences:
                repeated_sequences[sequence].append(i)
            else:
                repeated_sequences[sequence] = [i]

    # Filter only sequences that appear more than once
    repeated_sequences = {k: v for k, v in repeated_sequences.items() if len(v) > 1}

    if not repeated_sequences:
        print('No repeated sequences found')
        return None

    # Calculate distances between repetitions
    distances = []
    print('Repeated sequences found:')
    for seq, positions in sorted(repeated_sequences.items(), key=lambda x: len(x[1]), reverse=True)[:10]:
        print(f'  "{seq}" at positions {positions}')
        for i in range(len(positions) - 1):
            dist = positions[i+1] - positions[i]
            distances.append(dist)

    if not distances:
        return None

    print(f'\nDistances between repetitions: {sorted(set(distances))[:20]}')

    # Calculate GCD of all distances
    overall_gcd = reduce(gcd, distances)

    # Count most common divisors
    divisor_counts = {}
    for dist in distances:
        for divisor in range(2, min(dist + 1, 30)):
            if dist % divisor == 0:
                divisor_counts[divisor] = divisor_counts.get(divisor, 0) + 1

    if divisor_counts:
        # Get top 5 most common divisors
        top_divisors = sorted(divisor_counts.items(), key=lambda x: x[1], reverse=True)[:5]
        print(f'\nMost common divisors: {[f"{d}({c})" for d, c in top_divisors]}')
        most_common_divisor = top_divisors[0][0]
        print(f'Most likely key length (Kasiski): {most_common_divisor}')
        return most_common_divisor

    return overall_gcd if overall_gcd > 1 else None


def calculate_ioc(text):
    """Calculate Index of Coincidence for given text"""
    if len(text) <= 1:
        return 0

    # Remove non-alphabetic characters and convert to uppercase
    clean_text = ''.join(c.upper() for c in text if c.isalpha())

    if len(clean_text) <= 1:
        return 0

    # Count character frequencies
    char_freq = Counter(clean_text)

    # Calculate IoC using formula: Σ(fi * (fi - 1)) / (N * (N - 1))
    ioc = 0
    n = len(clean_text)

    for char in string.ascii_uppercase:
        if char in char_freq:
            fi = char_freq[char]
            ioc += (fi / n) * ((fi - 1) / (n - 1))

    return ioc


def find_key_length_ioc(ciphertext, max_length=20):
    """Find most likely key length using Index of Coincidence method"""
    clean_text = ''.join(c.upper() for c in ciphertext if c.isalpha())

    print('Testing key lengths with Index of Coincidence:')
    print('(English text IoC ≈ 0.065, Random text IoC ≈ 0.038)\n')

    best_length = 1
    best_avg_ioc = 0

    for length in range(1, min(max_length + 1, len(clean_text) // 2)):
        # Split text into groups based on key length
        groups = ['' for _ in range(length)]

        for i, char in enumerate(clean_text):
            groups[i % length] += char

        # Calculate average IoC for all groups
        iocs = [calculate_ioc(group) for group in groups if group]
        avg_ioc = sum(iocs) / len(iocs) if iocs else 0

        print(f'  Key length {length:2d}: avg IoC = {avg_ioc:.4f}')

        # Find length with IoC closest to English (0.065)
        if abs(avg_ioc - 0.065) < abs(best_avg_ioc - 0.065):
            best_avg_ioc = avg_ioc
            best_length = length

    print(f'\nMost likely key length: {best_length} (IoC = {best_avg_ioc:.4f})')
    return best_length


def recover_key(ciphertext, key_length):
    """Recover the key using improved frequency analysis with chi-squared test"""
    clean_text = ''.join(c.upper() for c in ciphertext if c.isalpha())

    # English letter frequency (approximate percentages)
    english_freq = {
        'A': 0.0817, 'B': 0.0150, 'C': 0.0278, 'D': 0.0425, 'E': 0.1270,
        'F': 0.0223, 'G': 0.0202, 'H': 0.0609, 'I': 0.0697, 'J': 0.0015,
        'K': 0.0077, 'L': 0.0403, 'M': 0.0241, 'N': 0.0675, 'O': 0.0751,
        'P': 0.0193, 'Q': 0.0010, 'R': 0.0599, 'S': 0.0633, 'T': 0.0906,
        'U': 0.0276, 'V': 0.0098, 'W': 0.0236, 'X': 0.0015, 'Y': 0.0197,
        'Z': 0.0007
    }

    key = []

    print('Recovering key using chi-squared test...\n')

    for position in range(key_length):
        # Extract every nth character
        group = ''
        for i in range(position, len(clean_text), key_length):
            group += clean_text[i]

        # Try all possible shifts (A-Z) and find best match using chi-squared test
        best_shift = 0
        best_chi_squared = float('inf')

        for shift in range(26):
            # Shift the group
            shifted = ''
            for char in group:
                shifted += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))

            # Calculate chi-squared statistic
            freq = Counter(shifted)
            total = len(shifted)
            chi_squared = 0

            for char in string.ascii_uppercase:
                observed = freq.get(char, 0)
                expected = english_freq[char] * total

                if expected > 0:
                    chi_squared += ((observed - expected) ** 2) / expected

            # Lower chi-squared = better match
            if chi_squared < best_chi_squared:
                best_chi_squared = chi_squared
                best_shift = shift

        # The shift value is the key letter
        key_letter = chr(ord('A') + best_shift)
        key.append(key_letter)
        print(f'  Position {position + 1:2d}: {key_letter} (chi-squared = {best_chi_squared:.2f})')

    return ''.join(key)


def main():
    with open('input.txt', 'r') as f:
        plaintext = f.read()

    key = "CRYPTOGRAPHY"

    print('Level 1 Vigenere Cipher\n')

    encrypted = encrypt_vigenere(plaintext, key)
    print('Encrypted:')
    print(encrypted)
    print()

    decrypted = decrypt_vigenere(encrypted, key)
    print('Decrypted:')
    print(decrypted)
    print()

    print('Level 2 Vigenere Cipher Cryptanalysis\n')

    # Method 1: Kasiski Examination
    print('Method 1: Kasiski Examination')
    key_length_kasiski = kasiski_examination(encrypted)
    print()

    # Method 2: Friedman Test (Index of Coincidence)
    print('Method 2: Friedman Test (Index of Coincidence)')
    key_length_ioc = find_key_length_ioc(encrypted)
    print()

    # Compare results and select key length
    print('Comparison:')
    print(f'  Kasiski method: {key_length_kasiski}')
    print(f'  Friedman test:  {key_length_ioc}')

    # Use IoC result as it's generally more reliable
    key_length = key_length_ioc
    if key_length_kasiski and key_length_kasiski == key_length_ioc:
        print(f'\n  Both methods agree! Key length = {key_length}')
    else:
        print(f'\n  Using Friedman test result: {key_length}')
    print()

    recovered_key = recover_key(encrypted, key_length)
    print(f'Recovered key: {recovered_key}')
    print(f'Original key:  {key}\n')

    decrypted_recovered = decrypt_vigenere(encrypted, recovered_key)
    print('Decrypted with recovered key:')
    print(decrypted_recovered[:300] + '...\n')


if __name__ == '__main__':
    main()