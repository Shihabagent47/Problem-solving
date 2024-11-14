def flip_bit(number, position):
    return number ^ (1 << position)

# Example: Flip the 1st bit of 0b0101 (which is 5 in decimal)
number = 5  # binary: 0101
position = 1
result = flip_bit(number, position)  # result = 7 (binary: 0111)
print(bin(result))  # Output: 0b111
