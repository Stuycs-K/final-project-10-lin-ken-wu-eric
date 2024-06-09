[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/ecp4su41)
# THIS DOCUMENT IS REQUIRED
## Group Info

10-Lin-Ken-Wu-Eric

## Overview

Our project is all about code obfuscation. In this project, we will: 

- Why Code Obfuscation is important 
- Show some examples of obfuscated code and their funciton
- Create and show two program made to obfuscate *YOUR* code using different techniques
- Demo new and variations of obfuscated code. 

## Instructions

### Examples 

Our project would include 2 examples of obfuscated code that perform various functions. Because both of the code is written in C, you would need to compile the code first. 

```
make compile
```

The compile command compiles the C code for both examples that we have. 

One of the examples that we have is a spinning donut. Running the following command would bring up that animation in the terminal. 

```
make donut
```

The second example is one of the winners from the 2018 IOCCC. There are ten panels that are in total. You can run: 

```
./prog
```

This would display the first panel. Replace the `prog` with any number from 1-9 inclusive. The file `prog` is the first panel.

You can also run:

```
make parrot
```

This would put all of the ten panels together into one animation/loop on the terminal.

>[!NOTE]
> Keep in mind both examples are a continuous loop. There is instructions at the bottom of the README to exit this state. 

### Programs

One of the programs that we created is a python program that obfuscate python code. This program obfuscates code using comment/docstring stripping and trash code insertion. 

To run the program:

```
make pyObfuscate ARGS="test.py"
```

>[!NOTE]
> Replace `test.py` with the name of the file you want to obfuscate. Keep in mind that the new file would have the prefix `obfuscated` + the name of your file. The obfuscated file should be able to run. 

Another program we created is a Java program that can obfuscate Java files. This program obfuscates code using comment/docstring stripping, remove whitespace, variable name decoding and trash code insertion. 

To run the program, you must compile the java file and then use it:
```
make compile
```

```
make javaObfuscate ARGS="Test.java"
```

>[!NOTE]
> Replace `Test.java` with the name of the file you want to obfuscate. Keep in mind that the new file would have the prefix `obfuscated` + the name of your file. The obfuscated file might be unable to run. The Python Program has more advanced trash code insertion compared to the Java program. 

### Demos

There are 2 demos that we have created. Some of them are new, while others uses the preexisting code from the examples as a template. These demos are also written in C and Java, so you would need to compile them first. 

```
make compile
```

> [!NOTE]
> There will be warnings after compiling the C file but it doesn't affect outcome of the code at all. 

One of the demos is the donut code. We modified the code from the example in order to perform another function. Running the following command would bring up that animation. You need to put two integers as arguments to change the speed.

```
make donut ARGS="int1 int2" 
```
>[!NOTE]
> The first integer controls the rotation in the x direction while the second integer controls rotation in the z direction.

Another demo is our obfuscation of some recursion code. You have to first compile the code.

```
make compile
```

To actually run the code, enter this:

```
java (recursionFile)
```

>[!NOTE]
> recursionFile refers to the files in /demos

> [!NOTE]
> Some files are executable with some being an infinite loop. Running `CTRL + C` would exit all of the executable files. Other files would write new files. 

> [!WARNING]
> You need to have GCC (GNU Compiler Collection) which allows you to compile the C code. This is required for all out code to run.

### Video 
https://drive.google.com/drive/folders/1UVSG7h2QS9Pq9hB9XRQE56GoPNhzAg5T?usp=sharing
