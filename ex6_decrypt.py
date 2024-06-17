

input_string = "e8dd=h>k"


i = 0

output_string = ""
for c in input_string:
    new_char = chr(ord(c)-i)
    output_string += new_char
    i += 1

print(output_string)
