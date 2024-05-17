import re

with open('matrix.txt', 'r') as file:
    lines = file.readlines()

# Extract dimensions and matrix data
n, m = map(int, lines[0].rstrip().split())
matrix = lines[1:n + 1]

# Transpose the matrix
decoded_list = list(zip(*matrix))

# Join transposed characters into a string
decoded_string = ''.join([''.join(row) for row in decoded_list])

# Remove unwanted characters and non-alphanumeric words
unwanted_chars = set(map(ord, '!@#$%^&*()-=+[]{}|;:,.<>?/~`'))
translation_table = str.maketrans('', '', ''.join(map(chr, unwanted_chars)))
decoded_string = decoded_string.translate(translation_table)
decoded = re.sub(r'\b[^a-zA-Z0-9]+\b', r' ', decoded_string)

# Print only the decoded message (without prefix)
print(decoded.strip())