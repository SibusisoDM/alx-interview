#!/usr/bin/python3

def validUTF8(data):
    # Number of bytes in the current character
    num_bytes = 0

    for num in data:
        # Check if the current number is a continuation byte
        if num & 0b11000000 == 0b10000000:
            # If there's no character to continue, it's invalid
            if num_bytes == 0:
                return False
            num_bytes -= 1
        else:
            # New character, so check the number of bytes it occupies
            if num_bytes > 0:
                return False
            if num & 0b10000000 == 0:
                num_bytes = 0  # Single byte character
            elif num & 0b11100000 == 0b11000000:
                num_bytes = 1  # Two byte character
            elif num & 0b11110000 == 0b11100000:
                num_bytes = 2  # Three byte character
            elif num & 0b11111000 == 0b11110000:
                num_bytes = 3  # Four byte character
            else:
                return False  # Invalid start byte

    # If there are still bytes left, it's invalid
    return num_bytes == 0

# Test cases
data1 = [197, 130, 1]  # Represents a valid two-byte character followed by an ASCII character
data2 = [235, 140, 4]  # Represents an invalid three-byte character followed by ASCII characters

print(validUTF8(data1))  # Output: True
print(validUTF8(data2))  # Output: False

