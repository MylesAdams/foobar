# Map of all letters (upper and lowercase) needed.
# Upper and lowercase mapped to increase speed, rather than use isupper
letters = {" " : "000000",
           "a" : "100000", "b" : "110000", "c" : "100100", "d" : "100110", "e" : "100010", "f" : "110100", "g" : "110110", "h" : "110010",
           "i" : "010100", "j" : "010110", "k" : "101000", "l" : "111000", "m" : "101100", "n" : "101110", "o" : "101010", "p" : "111100", "q" : "111110",
           "r" : "111010", "s" : "011100", "t" : "011110", "u" : "101001", "v" : "111001", "w" : "010111", "x" : "101101", "y" : "101111", "z" : "101011",
           "A" : "000001100000", "B" : "000001110000", "C" : "000001100100", "D" : "000001100110", "E" : "000001100010", "F" : "000001110100", "G" : "000001110110", "H" : "000001110010",
           "I" : "000001010100", "J" : "000001010110", "K" : "000001101000", "L" : "000001111000", "M" : "000001101100", "N" : "000001101110", "O" : "000001101010", "P" : "000001111100", "Q" : "000001111110",
           "R" : "000001111010", "S" : "000001011100", "T" : "000001011110", "U" : "000001101001", "V" : "000001111001", "W" : "000001010111", "X" : "000001101101", "Y" : "000001101111", "Z" : "000001101011"}


def answer(plaintext):
    braille = ""

    # Append the braille encoding of each letter to the return string
    for i in range(0, len(plaintext)):
        braille += letters[plaintext[i]]

    return braille


# print(answer("code") + "\n")
# print(answer("Braille") + "\n")
# print(answer("The quick brown fox jumps over the lazy dog") + "\n")

print(answer("code") == "100100101010100110100010")
print(answer("Braille") == "000001110000111010100000010100111000111000100010")
print(answer("The quick brown fox jumps over the lazy dog") == "000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110")
