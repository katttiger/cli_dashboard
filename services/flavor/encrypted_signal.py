import random
import string


def get_encrypted_signal():
    fragments = [
        " [DATA CORRUPTED] ",
        " <SIGNAL WEAK> ",
        " {CLASSIFIED} ",
        " //OVERRIDE_ACTIVE// ",
        " [SENDER UNKNOWN] "
    ]

    hex_chars = string.ascii_uppercase+"0123456789"
    random_hex = ''.join(random.choices(hex_chars, k=8))

    fragment = random.choice(fragments)

    glitch_text = f"0x{random_hex} >> {fragment} << {random_hex[::-1]}"
    return glitch_text
