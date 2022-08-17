# Write the solution for "Longest Word".
import re

# Open the file
f = open("../inputs/longest.txt", "r")
long_text = f.read()
f.close()

# Create regex for single word
word_regex = re.compile("\w+")
words = word_regex.findall(long_text)

long_len = 0
longest = ""
for word in words:
    if len(word) > long_len:
        long_len = len(word)
        longest = word

# Bold longest word
long_text = re.sub(longest, "**" + longest + "**", long_text)

# Write to file
out_file = open("longest_out.txt", "w")
out_file.write(long_text)
out_file.close()