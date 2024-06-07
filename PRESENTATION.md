## What is code obfuscation?

```
Obfuscate:
    - To render obscure, unclear, or unintelligible. 
    - To bewilder (someone)
```

Therefore, code obfuscation is the process of making code difficult to understand or compile.
Obfuscating code generally doesn't affect its functionality unless there are syntax errors introduced. For example, Python needs proper whitespace. 

## Why is code obfuscation important?

Hiding your code is very important because in the worst case scenario that your code is stolen by bad actors, then you wouldn't want them to know how it works. It will make it difficult for them to understand how your code works and how to compile it to use it for their own benefit. If the hackers eventually do crack the code, it will take them a long time, which may be enough time to catch them.

Essentially, it will hinder the ability of hackers who steal code to understand your code and modify it.  

> [!WARNING]
> HOWEVER, it is important to note that code obfuscation does not help increase the security of your code AT ALL. Keeping your data safe is your own responsibility and code obfuscation does not hide your data; it only makes your code unreadable. 

## What are the different methods you can use to obfuscate code? 

There are so many ways to make your code unreadable, complex, and hard to understand. 

- Removing context by changing names

One way is by renaming all of your variables, function names, and parameters to single letters instead of their intended use. This will make your code harder to understand if there are no good naming conventions. 

- Removing whitespace

Removing whitespace is one of the easiest ways to make code harder to understand. However, some coding languages may prevent the full ability of this. In Python, indentations are necessary to actually make code function. 

In C, you can put all of your code in the same line. It would make it harder to read. 

- Trash Code Insertion

By inserting trash code, it adds more chaos and randomness to the logic and meaning of the code, if it can be somewhat understood. For example, adding recursive functions to code focused on the volumes of shapes is completely irrelevant.

Junk code also don't affect the program's functionality in any way. They just increase the time complexity of the program. In some cases, it would make it hard to find the actual content or lines of code that is of use. 

- Comments/Docstring Stripping

Removing the comments in code and removing docstrings will essentially remove any insight on the logic of the code. It makes it harder for developers to understand this topic especially if they are unfamiliar with this.

Comments are also a good way to debug your code and for future use. It would take a lot longer for you to go back and try to re-understand all of the code. 

- String Extraction and Decoding

You can extract all the strings from the file and decode it in any cipher. Each string can be encoded using different ciphers to increase the complexity. In addition, you can add multiple layers to this process. A common encryption algorithm is base64, or you can use more complex ones such as RSA. 

This process can be somewhat reversed, but it would involved time. It would involve having the key generated or retrieved during runtime which makes static analysis more challenging.

Keep in mind, these obfuscation techniques, as they get more complicated, can introduced unintentional bugs and would increase development time. Code obfuscation is to help obscure your code, but not harm it. 

## Examples:

- The primary example we will use is code in Java, for recursion:
```java
public class Recursion {
    public static void main(String args[]) {
      System.out.println(bunnyEars(4));
    }
    
    public static int bunnyEars(int bunnies) {
            if (bunnies == 0){
                return 0;
            }
                return bunnyEars(bunnies - 1) + 2;
        }
}
```

First, let's change change some of the variable names. The following result would be: 
```java
public class Pol {
    public static void main(String a[]) {
      System.out.println(b(4));
    }
    
    public static int b(int i) {
            if (i == 0){
                return 0;
            }
                return b(i - 1) + 2;
        }
}
```

The only problem here is that this file extends from another file, so all files would have to be obfuscated. Also, the strings were turned into base64 to throw off the hackers. 

Next, let's remove all the whitespaces from this Java file.
```java
public class Pol { public static void main(String a[]) {System.out.println(b(4));} public static int b(int i) {if (i == 0){return 0;} else return b(i - 1) + 2;}}
```

Now, let's add random code to throw the hackers off.

```java
public class Pol { public static void main(String a[]) {System.out.println(b(4));} public static double loo(double p){return p;} public static int b(int i) {if (i == 0){return 0;} else return b(i - 1) + 2;}} public static double che(double a, double b){return a * b;} public static double paw(double a, double b){ return 0.5 * a * b;} public static String aasdfjEIF(String alsdjlfIWFWJLDVNCX){String i = "lJFVIej82348"; return alsdjlfIWFWJLDVNCX + i + kwjeifaiiozI34324;}
```

Although the code may be very obvious as for its function, larger projects will find obfuscation necessary. In addition, the context of the code is fully hidden, but it still runs fully. It would be even more effective if we add random print statements of the dummy functions. 

>[!NOTE]
> This example is under ```demos```.

- In the donut example shown, the code is shaped in a donut. If someone just took the code and saw it in the donut shape, it'd take longer to piece together because of the difference in whitespace. 

- In the parrot example shown, the initial code is formatted to the words "Undead Parrot". When the function is ran, there will be an animation of a parrot as a result of executable code. 

For more great examples of obfuscated code in C, we recommend you to check out [Yusuke Endoh](https://www.youtube.com/c/yusukeendoh), the world's number one International Obfuscated C Code Contest (IOCCC) competitor!

## Demos:

Looking at our demos, the first one is the donut. We added a small feature to change the speed of the rotating donut(in the x direction and the z direction), and tried to manually obfuscate it by messing with whitespace because of the flexibility of coding in C. 

Next, let's take a look at programs made by other people.

- A really simple online python obfuscator tool is [Oxyry Python Obfuscator](https://pyob.oxyry.com/). It does docstring/comment stripping and it changes the names of functions and variables to something not readable. 

## Programs:

##### Python Docstring/Comment Stripping

Our Python program allows you to obfuscate a python file by docstring and comment stripping.

Docstring and comment stripping makes code less readable. This is because these features provide insight into the purpose and logic of the code. Without these, it would make it harder for hackers to deciper what you are trying to achieve. 

Trash code insertion basically just adds a lot of random code that is literally gibberish to make the code more meaningless. They are in the form of assignment and operation. We are just assignment variable of random letters mashed together with a number or two. 

Operation just uses a variable, pre-existing or not, and performing one of the four basic operations. The trash code is unrelated to the rest of the program and shouldn't hinder the functionality. 

##### Java Change Names to Base64 + Comment Stripping + Removing whitespaces

Our Java program allows you to obfuscate a Java file by removing newlines/whitespaces, removes comments, and renames a lot of things.

Removing newlines will make the code way less readable, removing comments removes the insight of the code, and changing variable names removes the context of each function and the general code. 

>[!NOTE]
> Using our java obfuscation program will only work with standalone files that only use Java keywords, which means you can't have other classes unless you edit the program.

<!-- ## Our Tool:

In our tool, you can obfuscate any python file using our makefile. The key behind our tool is turning the strings into a different base that isn't human-readable.  -->
