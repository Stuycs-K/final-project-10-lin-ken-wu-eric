import sys
import re

fileName = sys.argv[1]
obfuscatedFileName = "obfuscated" + fileName

with open(fileName, "r") as file:
    with open(obfuscatedFileName, "w") as newFile:
        for line in file: 
          newLine = ""
          for char in line:
            if char.isspace():
              newLine += char
            else:
               newLine += char # Temp For Obfuscating Later
    
          newFile.write(newLine)  
