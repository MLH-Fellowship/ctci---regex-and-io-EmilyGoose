# Write the solution for "Filter Vowels".
import re

# Open the file
f = open("../inputs/vowels.txt", "r")
long_text = f.read()
f.close()

# Create regex for matching single vowel and find matches
word_regex = re.compile("[aeiou]")
vowels = word_regex.findall(long_text)

# Append count to filename
out_file = open("vowels-" + str(len(vowels)) + ".txt", "w")
out_file.write(long_text)
out_file.close()
