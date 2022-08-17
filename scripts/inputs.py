# Write the solution for "Split the files".
import re

files = ["github", "meta"]

# Create regex for single word and optional trailing punctuation
word_regex = re.compile("\w+[.,!]*")

for file_name in files:
    # Read the file
    f = open("../inputs/split/" + file_name + ".txt", "r")
    long_text = f.read()
    f.close()

    # Split file on words using regex
    words = word_regex.findall(long_text)

    broken = False
    i = 0
    while (not broken) and i < len(words):
        # Join words until string is over 500 bytes (1 char = 1 byte)
        joined = " ".join(words[:i + 1])
        if len(joined) > 500:
            broken = True
            # Join from last word that was under 500 bytes
            under_500 = " ".join(words[:i])
            # Second half of file
            over_500 = " ".join(words[i:])

            # Write halves of files
            out_file_1 = open(file_name + "1.txt", "w")
            out_file_1.write(under_500)
            out_file_1.close()
            out_file_2 = open(file_name + "2.txt", "w")
            out_file_2.write(over_500)
            out_file_2.close()
        i += 1
