file_path = "lengths.txt"  # Replace with the actual path to your file
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