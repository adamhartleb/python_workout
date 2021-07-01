def hex_output(hex_humber):
    decimal_number = 0
    for index, digit in enumerate(reversed(hex_humber)):
        decimal_number += int(digit, 16) * 16**index
    
    return decimal_number

print(hex_output("123"))