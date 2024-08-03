from collections import Counter
import re


binary_string = "11111111000000001101010011111111111111111011100100000000"

max_length = 8  

def generate_binary_strings(length):
    binary_strings = []
    
    for i in range(2**length):
        binary_string = format(i, '0' + str(length) + 'b')
        binary_strings.append(binary_string)
    return binary_strings

result_list = []
for length in range(1, max_length + 1):
    binary_strings = generate_binary_strings(length)
    result_list.extend(binary_strings)  #result_list
#print(result_list)

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
new_binary_string = pattern.sub(replace_sequence, binary_string)
# Replace the sequences using the custom function
print(new_binary_string)
print(len(binary_string))
