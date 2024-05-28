import sys
import os
import re
import random

def obfuscate(code):
    obfuscated_code = ""
    comment = False
    docstring = False
    for i in range(len(code)):
        char = code[i]
        if comment:
            if char == '\n':
                comment = False
                obfuscated_code += char
        elif docstring:
            if char == '"' and code[i - 1] != '\\':
                docstring = False
            obfuscated_code += char
        elif char == '#':
            comment = True
            obfuscated_code += char
        elif char == '"' and code[i - 1] != '\\':
            docstring = True
            obfuscated_code += char
        elif char.isspace():
            obfuscated_code += char
        else:
            obfuscated_code += chr(ord(char) + 1)
        
        # Trash Code Insertion
        if random.random() < 0.25:
            trash_code = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=random.randint(5, 15)))
            obfuscated_code += trash_code

    return obfuscated_code

def main():
    if len(sys.argv) != 2:
        print("Usage: make pyObfuscate <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print("File not found:", filename)
        sys.exit(1)

    with open(filename, "r") as file:
        code = file.read()
        obfuscated_code = obfuscate(code)

    obfuscated_filename = "obfuscated" + filename
    with open(obfuscated_filename, "w") as new_file:
        new_file.write(obfuscated_code)

if __name__ == "__main__":
    main()
