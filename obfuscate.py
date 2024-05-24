import sys
import re

fileName = sys.argv[1]
obfuscatedFileName = "obfuscated" + sys.argv[1]

with open(fileName, "r") as file:
  line = file.readline()
  with open(obfuscatedFileName, "w") as newFile:
    while (line):
      line.strip()
      line = file.readline()
      # print(line)
      newLine = re.search("^[A-Z]*$",line)
      newFile.write(line)
