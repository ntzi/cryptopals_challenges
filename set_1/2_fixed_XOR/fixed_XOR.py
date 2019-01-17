# Solution for the cryptopals crypto challenges, Set 1, Challenge 2
# [link: https://cryptopals.com/sets/1/challenges/2]

#  ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
#  ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

# Apply XOR between two hexadecimal numbers provided in string format.
# Test. [src: https://cryptopals.com/sets/1/challenges/2]
# Input:    "1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965"
# Output:   "746865206b696420646f6e277420706c6179"

#  ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
#  ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

class XOR:
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2

    def xor_hex(self):
        # String to hex string.
        self.number_1 = "0x" + self.number_1
        self.number_2 = "0x" + self.number_2

        # String to integer.
        number_1_int = int(self.number_1, 16)
        number_2_int = int(self.number_2, 16)

        # Hex to binary.
        number_1_binary = bin(number_1_int)
        number_2_binary = bin(number_2_int)

        # Convert binary string to binary integer in order to apply XOR afterward.
        number_1_int = int(number_1_binary[2::])
        number_2_int = int(number_2_binary[2::])

        # Integer to string with binary format.
        number_1_str = "0b" + str(number_1_int)
        number_2_str = "0b" + str(number_2_int)

        # String to integer.
        number_1_int = int(number_1_str, 2)
        number_2_int = int(number_2_str, 2)

        # Logical XOR between binary numbers.
        xor_binary = number_1_int ^ number_2_int

        xor_hexadecimal = hex(xor_binary)

        # Delete the 0x before the number
        xor_hexadecimal = xor_hexadecimal[2::]

        return xor_hexadecimal


if __name__ == '__main__':
    xor = XOR(number_1="1c0111001f010100061a024b53535009181c", number_2="686974207468652062756c6c277320657965")
    result = xor.xor_hex()
    # result = xor_hex("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965")
    print(result)
