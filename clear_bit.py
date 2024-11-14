def clear_bit(number, position):
    return number & ~(1 << position)

# Example: Clear the 1st bit of 0b0111 (which is 7 in decimal)
number = 7  # binary: 0111
position = 1
result = clear_bit(number, position)  # result = 5 (binary: 0101)
print(bin(result))  # Output: 0b101
