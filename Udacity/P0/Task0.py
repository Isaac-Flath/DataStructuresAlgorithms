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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

# Destructured assignment
inb_text, outb_text, text_time = texts[0]
inb_call, outb_call, call_time, call_duration = calls[0]

print(f"First record of texts, {inb_text} texts {outb_text} at time {text_time}")
print(f"Last record of calls, {inb_call} calls {outb_call} at time {call_time}, lasting {call_duration} seconds")
