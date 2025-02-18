
# "aaabb" → "a3b2"
# "abc" → "a1b1c1"
# "" → ""
def string_compress(string):
    print("Compressing string", string)

    string = string.strip()

    compressed_string = ""
    string_length = len(string)
    current_char_index = 0

    current_compressed_char = ""
    current_compressed_char_count = 0

    # Check if string has enough length. Define first letter
    if string_length >= 1:
        current_compressed_char = string[0]
    else:
        return compressed_string

    # Look at string characters one by one
    while current_char_index != string_length:
        # If new letter is found, write old to answer and save new one
        if current_compressed_char != string[current_char_index]:
            # Saved part of a compressed string as answer
            compressed_string += current_compressed_char + str(current_compressed_char_count)

            # Start saving part of a new string
            current_compressed_char = string[current_char_index]
            current_compressed_char_count = 1
        # Character is the same. Add to the count
        elif current_compressed_char == string[current_char_index]:
            current_compressed_char_count += 1

        current_char_index += 1

    # Program finished. Finish writing last character
    compressed_string += current_compressed_char + str(current_compressed_char_count)

    print("Compressed string", compressed_string)
    return compressed_string

# "a3b2" → "aaabb"
# "a1b1c1" → "abc"
# "" → ""
def string_decompress():
    print("Decompressing string")

def main():
    string_compress("aaabb")
    string_compress("abc")
    string_compress("")

if __name__ == '__main__':
    main()