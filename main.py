
# "aaabb" → "a3b2"
# "abc" → "a1b1c1"
# "" → ""
def string_compress(string):
    print("Compressing string", string)

    # Remove unnecessary spaces
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
def string_decompress(string):
    print("Decompressing string", string)

    # Remove unnecessary spaces
    string = string.strip()

    decompressed_string = ""
    string_length = len(string)

    # Ideally the format contains letter and a number. Number can be different kinds of length.
    string_char_index = 0
    # Iterate through all the string
    while string_char_index < len(string):
        current_letter = string[string_char_index]
        string_char_index += 1

        # Find the number of times character will be repeated (number). Check if it is more than one character long.
        number_string = ""
        while string_char_index < string_length and string[string_char_index].isdigit():
            number_string += string[string_char_index]
            string_char_index += 1

        # Check if number is defined
        if not number_string:
            print("The string doesn't have a correct format (letter and number): a3")
            print("Decompressed string", decompressed_string)
            return decompressed_string

        # Convert number to int and add to decompressed string
        current_number = int(number_string)
        for _ in range(current_number):
            decompressed_string += current_letter

    print("Decompressed string", decompressed_string)
    return decompressed_string

def main():
    string_compress("aaabb")
    string_compress("abc")
    string_compress("")
    string_compress("a")
    string_compress("a" * 1000)
    string_compress("ab" * 500)

    string_decompress("a10b2")
    string_decompress("a1b1c1")
    string_decompress("")

if __name__ == '__main__':
    main()