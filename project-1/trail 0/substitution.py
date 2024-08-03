binary_string = "11111111000000001101010011111111111111111011100100000000"
first_list = ['11111111', '00000000', '11010100', '10111001']
second_list = ['0', '1', '00', '01', '10', '11', '000', '001', '010', '011', '100', '101', '110', '111', '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']

# Create a dictionary to map the first list elements to the second list elements
replacement_dict = dict(zip(first_list, second_list))

# Function to replace sequences in the binary string
def replace_sequence(match):
    return replacement_dict[match.group()]

import re

# Create a regular expression pattern from the first list elements
pattern = re.compile('|'.join(map(re.escape, first_list)))

# Replace the sequences using the custom function
new_binary_string = pattern.sub(replace_sequence, binary_string)

print(new_binary_string)
