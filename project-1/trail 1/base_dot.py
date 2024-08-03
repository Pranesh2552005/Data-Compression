from collections import Counter
import re
file_path = 'textdoc.txt'  # Replace with the actual path to your file
# Open the file in binary read mode

with open(file_path, 'rb') as file:
    binary_data = file.read()
# Convert the binary data to a string of 0's and 1's
binary_string = ''.join(format(byte, '08b') for byte in binary_data)
# Now, the binary data represented as 0's and 1's is stored in the 'binary_string' variable'
def generate_binary_strings(length):
    binary_strings = []
    
    for i in range(2**length):
        binary_string = format(i, '0' + str(length) + 'b')
        binary_strings.append(binary_string)
    return binary_strings



max_length = 8   #Maximum length of binary strings

result_list = []
for length in range(1, max_length + 1):
    binary_strings = generate_binary_strings(length)
    result_list.extend(binary_strings)  #result_list
print(result_list)

interval_length = 8 # Length of each interval

# Split the binary string into intervals
intervals = [binary_string[i:i+interval_length] for i in range(0, len(binary_string), interval_length)]

# Count the frequency of each interval and sort by frequency in descending order
interval_counts = Counter(intervals)
sorted_intervals = sorted(interval_counts.items(), key=lambda x: x[1], reverse=True)

# Extract the intervals with highest frequency
most_repeated_intervals = [interval for interval, _ in sorted_intervals]
first_list = most_repeated_intervals
second_list = result_list
# Create a dictionary to map the first list elements to the second list elements
replacement_dict = dict(zip(first_list, second_list))

# Function to replace sequences in the binary string
def replace_sequence(match):
    return replacement_dict[match.group()]

# Create a regular expression pattern from the first list elements
pattern = re.compile('|'.join(map(re.escape, first_list)))

# Replace the sequences using the custom function


new_binary_string = pattern.sub(replace_sequence, binary_string)
print(most_repeated_intervals)
print(new_binary_string)
print(len(new_binary_string))
print(binary_string)
print(len(binary_string))

