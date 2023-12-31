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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
out_calls, in_calls, _, _ = list(zip(*calls))
out_text, in_text, _ = list(zip(*texts))

phone_numbers = set(in_calls + out_text + in_text)    

telemarketers = [call for call in set(out_calls) if call not in phone_numbers]

print("These numbers could be telemarketers: ")
for telemarketer in sorted(telemarketers):
    print(telemarketer)
