from collections import Counter
import re
file_path = "C:\\Users\\prane\\Desktop\\Sample Report.pdf"  # Replace with the actual path to your file
# Open the file in binary read mode
def file_to_binary(file_path):
    try:
        with open(file_path, 'rb') as file:
            binary_data = file.read()
            binary_string = ''.join(format(byte, '08b') for byte in binary_data)
            return binary_string
    except FileNotFoundError:
        print("File not found.")
        return None

# Replace 'your_file_path_here' with the actual path to the file you want to convert
binary_string = file_to_binary(file_path)


#print(binary_string)
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
    result_list.extend(binary_strings)

interval_length = 8  # Length of each interval
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

# Count the lengths of the strings in the result list
lengths_of_result_strings = [len(replacement_dict[sequence]) for sequence in intervals]

# Write the lengths directly to a text file without spaces
with open("lengths.txt", "w") as file:
    file.write("".join(str(length) for length in lengths_of_result_strings))

print(len(new_binary_string))
#print(len(first_list))

