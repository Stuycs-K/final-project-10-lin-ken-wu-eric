import sys
import os
import re
import random

def obfuscate(code):
    obfuscated_code = ""
    singleComment = False
    multipleComment = False

    i = 0
    while i < len(code):
        char = code[i]

        if singleComment:
            if char == '\n':
                singleComment = False
        elif multipleComment:
            if char == '"' and code[i:i+3] == '"""':
                multipleComment = False
                i += 2 
            elif char == "'" and code[i:i+3] == "'''":
                multipleComment = False
                i += 2 
        elif char == '#':
            singleComment = True
        elif char == '"' and code[i:i+3] == '"""':
            multipleComment = True
            i += 2 
        elif char == "'" and code[i:i+3] == "'''":
            multipleComment = True
            i += 2
        else:
            obfuscated_code += char

        i += 1

    return obfuscated_code

def main():
    if len(sys.argv) != 2:
        print('Usage: python obfuscator.py ARGS="<filename>"')
        sys.exit(1)

    fileName = sys.argv[1]
    if not os.path.isfile(fileName):
        print("File not found. Make sure PATH is correct")
        sys.exit(1)

    with open(fileName, "r") as file:
        code = file.read()
        obfuscatedCode = obfuscate(code)
        obfuscatedFileName = "obfuscated" + fileName
        with open(obfuscatedFileName, "w") as newFile:
            newFile.write(obfuscatedCode)

if __name__ == "__main__":
    main()