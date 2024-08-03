from collections import Counter

binary_string = "111111110000000011010100111111111111111110111001000000001011100111010100110101001"

interval_length = 8  # Length of each interval

# Split the binary string into intervals
intervals = [binary_string[i:i+interval_length] for i in range(0, len(binary_string), interval_length)]

# Count the frequency of each interval and sort by frequency in descending order
interval_counts = Counter(intervals)
sorted_intervals = sorted(interval_counts.items(), key=lambda x: x[1], reverse=True)

# Extract the intervals with highest frequency
most_repeated_intervals = [interval for interval, _ in sorted_intervals]

print(most_repeated_intervals)