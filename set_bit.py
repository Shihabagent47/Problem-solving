def set_bit(number, position):
    return number | (1 << position)

# Example: Set the 2nd bit of 0b0001 (which is 1 in decimal)
number = 1  # binary: 0001
position = 2
result = set_bit(number, position)  # result = 5 (binary: 0101)
print(bin(result))  # Output: 0b101
