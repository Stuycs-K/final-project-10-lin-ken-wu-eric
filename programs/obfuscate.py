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
            junk_code += f'{indent}{var_name} = {r1}\n'
        else:
            op = random.choice(['+', '-', '*', '/', '%'])
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

def junkmachine(code):
    lines = []
    for line in code.split('\n'):
        if line.strip():
            lines.append(line)

    whitespaces = []

    for line in lines:
        whitespace = 0
        for char in line:
            if char.isspace():
                whitespace += 1
            else:
                break
    
        whitespaces.append(whitespace)

    print(whitespaces)
    obfuscated_code = ""
    
    for i in range(len(lines)):
        line = lines[i]
        obfuscated_code += line + "\n"
        
        if random.random() < 0.5:  
            if (i + 1 == len(whitespaces)):
                obfuscated_code += junkgenerator(random.randint(10, 30), whitespaces[i])
            elif (whitespaces[i] < whitespaces[i + 1]):
                obfuscated_code += junkgenerator(random.randint(10, 30), whitespaces[i + 1])
            else :
                obfuscated_code += junkgenerator(random.randint(10, 30), whitespaces[i])

    return obfuscated_code

def obfuscate(file):
    code = file.read()

    lines = []
    for line in code.split('\n'):
        if line.strip():
            lines.append(line)
    
    obfuscated_code = ""
    singleComment = False
    multipleComment = False

    for i in range(len(lines)): 
        singleComment = False
        line = lines[i] 
        j = 0  
        while j < len(line):  
            char = line[j]

            if singleComment:
                if char == '\n':
                    singleComment = False
            elif multipleComment:
                if char == '"' and line[j:j+3] == '"""':
                    multipleComment = False
                    j += 2 
                elif char == "'" and line[j:j+3] == "'''":
                    multipleComment = False
                    j += 2 
            elif char == '#':
                singleComment = True
            elif char == '"' and line[j:j+3] == '"""':
                multipleComment = True
                j += 2 
            elif char == "'" and line[j:j+3] == "'''":
                multipleComment = True
                j += 2
            elif char == '\n':
                obfuscated_code += char
                if not singleComment and not multipleComment:
                    if random.random() < 0.2:  
                        junk_code = junkgenerator(random.randint(10, 30), whitespaces[i])
                        obfuscated_code += junk_code
            else:
                if not singleComment and not multipleComment:
                    obfuscated_code += char

            j += 1
        
        obfuscated_code += "\n"

    return junkmachine(obfuscated_code)

def main():
    if len(sys.argv) != 2:
        print('Usage: python obfuscator.py ARGS="<filename>"')
        sys.exit(1)

    fileName = sys.argv[1]
    if not os.path.isfile(fileName):
        print("File not found. Make sure PATH is correct")
        sys.exit(1)

    with open(fileName, "r") as file:
        obfuscatedCode = obfuscate(file)
        obfuscatedFileName = "obfuscated" + fileName
        with open(obfuscatedFileName, "w") as newFile:
            newFile.write(obfuscatedCode)

if __name__ == "__main__":
    main()