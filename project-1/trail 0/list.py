def generate_binary_strings(length):
    binary_strings = []
    
    for i in range(2**length):
        binary_string = format(i, '0' + str(length) + 'b')
        binary_strings.append(binary_string)
    
    return binary_strings

max_length = 8  # Maximum length of binary strings

result_list = []
for length in range(1, max_length + 1):
    binary_strings = generate_binary_strings(length)
    result_list.extend(binary_strings)

print(result_list)



