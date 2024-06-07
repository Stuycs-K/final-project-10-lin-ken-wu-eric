import sys
import os
import re
import random
import string

def junkminion(length, current_indent):
    indent = " " * current_indent
    junk_code = ''
    for _ in range(length):
        rand_type = random.choice(['assignment', 'operation'])
        if rand_type == 'assignment':
            var_name = ''.join(random.choices(string.ascii_letters, k=1) + random.choices(string.ascii_letters + string.digits, k=9))
            r1 = random.randint(0, 999)
            r2 = random.randint(0, 999)
            junk_code += f'{indent}{var_name} = {r1} * {r2}\n'
        else:
            op = random.choice(['+', '-', '*', '/'])
            var1 = ''.join(random.choices(string.ascii_letters, k=5))
            var2 = ''.join(random.choices(string.ascii_letters, k=5))
            junk_code += f'{indent}{var1} = {random.randint(0, 999)} {op} {var2}\n'
    return junk_code

def junkgenerator(num, current_indent):
    code = ''
    for _ in range(num):
        length = random.randint(10, 30)
        code += "\n" + junkminion(length, current_indent) + "\n"
    return code

def obfuscate(code):
    obfuscated_code = ""
    singleComment = False
    multipleComment = False
    current_indent = 0

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
        elif char == '\n':
            obfuscated_code += char
            if not singleComment and not multipleComment:
                current_indent = len(re.match(r'^\s*', code[i+1:]).group(0))
                if random.random() < 0.2:  
                    junk_code = junkgenerator(random.randint(10, 30), current_indent)
                    obfuscated_code += junk_code
        else:
            if not singleComment and not multipleComment:
                obfuscated_code += char

        i += 1

    if random.random() < 0.5:  
        obfuscated_code += junkgenerator(random.randint(10, 30), current_indent)

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