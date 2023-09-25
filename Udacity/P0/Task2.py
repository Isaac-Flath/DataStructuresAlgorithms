"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('./Udacity/P0/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('./Udacity/P0/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

from collections import defaultdict

# Simplify dictionary key initializations
phone_numbers = defaultdict(lambda: 0)

# Calculate total call time for each phone number
for call in calls:
    phone_numbers[call[0]] += int(call[3])
    phone_numbers[call[0]] += int(call[3])

# Find phone number with the largest call time
max_val = 0
for phone_number,time in phone_numbers.items():
    if time > max_val:
        max_val = time
        out_number = phone_number

# Print answer
print(f"{out_number} spent the longest time, {max_val} seconds, on the phone during September 2016.")

