# Work Log

## Ken Lin

### 5/22/24

- Looked at the implications of obfuscating code. 
- Research one example that we can demo which is [a spinning donut](https://www.a1k0n.net/2006/09/15/obfuscated-c-donut.html)

### 5/23/24

- Added the original donut.c into the examples directory. 
- Started on working on a variation of donut.c in the demos directory. (Not Sure if its fully functional)
- Added the makefile commands in order to compile and run files in demos and examples directory. 
- Added information into README

### 5/24/24

- Added the speed x and speed z variable to donut.c demo to control spinning speed. 
- Tried to add it to the makefile terminal command, but it didn't work. Eric will try to get it working. 
- Fixed Eric's obfuscate.py which didn't copy over the first line of the input file and keeping whitespace. 
- Researched some more obfuscation programs we can run
    - Comments/Docs Stripping
    - Name Mangling
    - Trash Code Insertion

### 5/26/24

- Added comment and docstring stripping to obfuscate.py

### 5/27/24

- Rewrote obfuscate.py to be a obfuscate method and a main method.
- Added trash code insertion based on randomness into the obfuscated code. 
- Update to README and PRESENATION regarding obfuscate.py

### 5/28/24

- Changed obfuscate.py to remove all traces of // and #. It didn't remove those characters before
- Removing whitespace and obfuscating donut.c code into a donut. (demos directory)

### 5/29/24

- Added "File not Found" Error catching into the java program
- Revised Eric's docstring stripping and added comment stripping (both inline and multiple lines)

### 5/30/24

- Fixed multi-line comment stripping in java program. 
- Removed java program's ability to remove string literals

## Eric Wu

### 5/22/24

- Setting up repo/files - class
- Researching code obfuscation in competitions (ioccc) - home

### 5/23/24

- Started writing up the presentation slides - class & home
- Set up our python file a little - home

### 5/24/24

- Continued working on obfuscation python code 
- Fixed Ken's donut.c that had trouble turning arguments into floats with seg fault

### 5/27/24
- Started working on the java implementation of obfuscation, there's a big error
- Updating Presentation with examples of code and formatiing 
- Fixing command usage error in python file

### 5/28/24
- Worked on Java obfuscate code, couldn't get it to work because of taking every line, not each word, checking for Java keywords
- Worked a lot on presentation and adding example into it

### 5/29/24
- Worked on revising donut.c obfuscated demo (lots of errors)
- Edited README to include how to use java program
- Added more to presentation including obfuscated tools, finished example 
