# Solution for the cryptopals crypto challenges, Set 1, Challenge 3
# [link: https://cryptopals.com/sets/1/challenges/3]

#  ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
#  ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

# Given a hex encoded string (eg: 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736), which
# has been XOR'd against a single character, finds the key and decrypts the message.
# In order to find the correct key a scoring function has been developed.
# This scoring function finds the correct key by evaluating the output message based on the relative frequency
# the characters occur in the English language.

#  ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
#  ----- ----- ----- ----- ----- ----- ----- ----- ----- -----


# Import Challenge 2
import sys
sys.path.insert(0, '../2_fixed_XOR')
import fixed_XOR

import codecs
import string
import math
import re
from collections import Counter


class XorCipher():
    def __init__(self, ciphered_string):
        self.ciphered_string = ciphered_string
        return


    def decipher(self):
        # Find the key to decipher the string.
        key = self.find_key()
        # Decipher the string using the found key.
        deciphered_string = self.decipher_with_key(key=key)

        return deciphered_string


    # Hex to ASCII
    def hex_to_ascii(self, hex_string):
        ascii_string = codecs.decode(hex_string, 'hex').decode()

        return ascii_string


    # ASCII to Hex.
    def ascii_to_hex(self, ascii_string):
        # Encode to byte stream.
        ascii_string = ascii_string.encode()

        hex_string = codecs.encode(ascii_string, "hex").decode()

        return hex_string


    # Adjust the size of the key to equal the size of the string that needs to be ciphered.
    def adjust_cipher_key(self, string_input, key):
        if len(key) < len(string_input):
            # Describes how many times is 'string_input' bigger than the 'key'.
            key_times = math.ceil(len(string_input) / len(key))
            full_key = ''.join([key] * key_times)
            # Cut the unused characters at the end.
            key = full_key[0:len(string_input)]

        return key


    # Score the deciphered string.
    # The biggest the score the most possible to have it successfully deciphered.
    def score(self, string_input):
        # Relative frequency in the English language. Source: https://en.wikipedia.org/wiki/Letter_frequency
        relative_letter_frequency = {
            "a": 8.167,
            "b": 1.492,
            "c": 2.782,
            "d": 4.253,
            "e": 12.702,
            "f": 2.228,
            "g": 2.015,
            "h": 6.094,
            "i": 6.966,
            "j": 0.153,
            "k": 0.772,
            "l": 4.025,
            "m": 2.406,
            "n": 6.749,
            "o": 7.507,
            "p": 1.929,
            "q": 0.095,
            "r": 5.987,
            "s": 6.327,
            "t": 9.056,
            "u": 2.758,
            "v": 0.978,
            "w": 2.360,
            "x": 0.150,
            "y": 1.974,
            "z": 0.074
        }
        # Lowercase the string.
        string_input = string_input.lower()
        # The bigger the score the most possible it is for the input_string to be deciphered.
        score = 0

        # Create a regular expression with only the letters of the alphabet.
        regex = re.compile('[^a-zA-Z]')
        # Delete all the non-alphabet letters in the string.
        string_input = regex.sub('', string_input)

        letter_counter = Counter(string_input)

        for letter in letter_counter:
            # The score of the string is the sum of the relative frequency in the English language of each letter.
            score += relative_letter_frequency[letter]

        return score


    # Decipher a string with a key.
    # The key must be a single character.
    def decipher_with_key(self, key):
        # Convert character to ascii encoding.
        character_in_ascii = self.ascii_to_hex(ascii_string=key)

        # Adjust the size of the key to equal the size of the string that needs to be ciphered.
        character_in_ascii = self.adjust_cipher_key(string_input=ciphered_string, key=character_in_ascii)

        # Get the logical XOR between the input string and a character. Both string and character are in hex.
        # xor = xor_hex.xor_hex(number_1=self.ciphered_string, number_2=character_in_ascii)
        xor_init = fixed_XOR.XOR(number_1=self.ciphered_string, number_2=character_in_ascii)
        xor = xor_init.xor_hex()

        # Get the text of the XORed string.
        deciphered_string = self.hex_to_ascii(hex_string=xor)

        return deciphered_string


    # Finds the correct key to decipher the input string.
    # The key is one of the characters of the english alphabet.
    # It tests all the lowercase characters using the scoring function self.score()
    def find_key(self):
        max_score = 0
        for character in string.ascii_lowercase:
            # Decipher the ciphered string with an alphabet character.
            deciphered_string = self.decipher_with_key(key=character)

            # Calculate the score of the string. The score represents the possibility of the string being decoded.
            score = self.score(string_input=deciphered_string)

            # Keep the key with the highest score. This is the correct key to decipher the string.
            if max_score < score:
                max_score = score
                key = character

        return key





if __name__ == '__main__':
    ciphered_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

    xor_cipher = XorCipher(ciphered_string=ciphered_string)
    deciphered_string = xor_cipher.decipher()
    # We can also decipher the string if we already know the key by directly providing it. Eg:
    # deciphered_string = xor_cipher.decipher_with_key(key="x")

    print("Deciphered Message: ", deciphered_string)
