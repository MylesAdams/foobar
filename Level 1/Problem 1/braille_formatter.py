def format(bump_str):
    print(len(bump_str))
    print()
    line1, line2, line3 = [], [], []
    for i in range(0, len(bump_str), 6):
        line1.append(bump_str[i])
        line1.append(bump_str[i+3])
        line1.append(" ")

        line2.append(bump_str[i+1])
        line2.append(bump_str[i+4])
        line2.append(" ")

        line3.append(bump_str[i+2])
        line3.append(bump_str[i+5])
        line3.append(" ")

    print(*line1, sep='')
    print(*line2, sep='')
    print(*line3, sep='')


print()
format("000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110")

# The quick brown fox jumps over the lazy dog