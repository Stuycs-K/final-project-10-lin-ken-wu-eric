import sys
import re

def obfuscate(args):
  with open(args, "r") as file:
    line = file.readline()
    with open(obfuscatedFileName, "w") as newFile:
      while (line):
        line.strip()
        line = file.readline()
        print(line)
        newLine = re.search("^[A-Z]*$",line)
        newFile.write(line)
      
if __name__ == "__main__":
    args = sys.argv
    globals()[args[1]](*args[2:])