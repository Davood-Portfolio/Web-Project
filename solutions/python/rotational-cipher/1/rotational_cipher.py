def rotate(text, key):
    pass
def rotate(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            # Determine base (uppercase or lowercase)
            base = ord('A') if char.isupper() else ord('a')
            # Rotate character and wrap using modulo 26
            rotated = (ord(char) - base + key) % 26 + base
            result += chr(rotated)
        else:
            # Keep non-alphabet characters unchanged
            result += char

    return result