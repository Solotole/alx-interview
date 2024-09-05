#!/usr/bin/python3
"""method that determines if a given data set
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """confirming if valid UTF-8 encoding"""
    num_bytes = 0

    # Masks to check the pattern of the leading byte
    mask1 = 1 << 7
    mask2 = 1 << 6
    for num in data:
        # Only the least significant 8 bits of the number matter
        byte = num & 0xFF

        # If we are expecting continuation bytes
        if num_bytes > 0:
            if not (byte & mask1 and not (byte & mask2)):
                return False
            num_bytes -= 1
        else:
            # Determine how many bytes are needed for this UTF-8 character
            if (byte & mask1) == 0:
                # 1-byte character (0xxxxxxx)
                continue
            elif (byte & 0xE0) == 0xC0:
                num_bytes = 1
            elif (byte & 0xF0) == 0xE0:
                num_bytes = 2
            elif (byte & 0xF8) == 0xF0:
                num_bytes = 3
            else:
                # Invalid leading byte
                return False
    return num_bytes == 0
