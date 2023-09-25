"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('./Udacity/P0/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('./Udacity/P0/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

out_calls, in_calls, _, _ = list(zip(*calls))
out_text, in_text, _ = list(zip(*texts))

phone_numbers = out_calls + in_calls + out_text + in_text

print(f"There are {len(set(phone_numbers))} different telephone numbers in the records.")