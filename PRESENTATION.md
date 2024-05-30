## What is code obfuscation?

First, let's take a look at the word obfuscation, which means to make something difficult to understand. Code obfuscation means to make code difficult to understand or compile. 

## Why is code obfuscation important?

Hiding your code is very important because in the worst case scenario that your code is stolen by bad actors, then you wouldn't want them to know how it works. It will make it difficult for them to understand how your code works and how to compile it to use it for their own benefit. If the hackers eventually do crack the code, it will take them a long time, which may be enough time to catch them.

Essentially, it will hinder the ability of hackers who steal code to understand your code. 

HOWEVER, it is important to note that code obfuscation does not help increase the security of your code AT ALL. Keeping your data safe is your own responsibility and code obfuscation does not hide your data; it only makes your code unreadable. 

## What are the different methods you can use to obfuscate code? 

There are so many ways to make your code unreadable, complex, and hard to understand. 

- Removing context by changing names

One way is by renaming all of your variables, function names, and parameters to single letters instead of their intended use. This will make your code harder to understand if there are no good naming conventions. 

- Removing whitespace

Removing whitespace is one of the easiest ways to make code harder to understand. However, some coding languages may prevent the full ability of this. In Python, indentations are necessary to actually make code function. 

- Trash Code Insertion

By inserting trash code, it adds more chaos and randomness to the logic and meaning of the code, if it can be somewhat understood. For example, adding recursive functions to code focused on the volumes of shapes is completely irrelevant.

- Comments/Docstring Stripping

Removing the comments in code and removing docstrings will essentially remove any insight on the logic of the code.

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
<!-- ```java
class SavingsAccount extends BankAccount {
private double interestRate;
private int withdrawCount;

public SavingsAccount(String name, double initialDeposit, double interestRate)throws Exception {
    super(name, initialDeposit);
    if (interestRate <= 0)
       throw new Exception("Interest rate must be greater than 0");
    this.interestRate = interestRate;
}
public void addInterest() throws Exception {
    this.deposit(getBalance() * interestRate);
}

public void withdraw(double amount) throws Exception {
        withdrawCount++;
        if (amount <= 0) {
            withdrawCount--;
            throw new Exception("Balance is negative");
        }
        if (withdrawCount > 6)
            throw new Exception("You have withdrawn 6 times already");
        super.withdraw(amount);
}

public int getWithdrawCount() {
    return withdrawCount;
}
}
``` -->

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

<!-- ```java
class Ju extends Po {
private double ab;
private int ba;

public Ju(String a, double b, double c)throws Exception {
    super(a, b);
    if (c <= 0)
       throw new Exception("IkludGVyZXN0IHJhdGUgbXVzdCBiZSBncmVhdGVyIHRoYW4gMCI=");
    this.c = c;
}
public void hh() throws Exception {
    this.jk(ya() * ab);
}

public void ht(double rt) throws Exception {
        ba++;
        if (rt <= 0) {
            ba--;
            throw new Exception("QmFsYW5jZSBpcyBuZWdhdGl2ZQ==");
        }
        if (ba > 6)
            throw new Exception("WW91IGhhdmUgd2l0aGRyYXduIDYgdGltZXMgYWxyZWFkeQ==");
        super.ht(rt);
}

public int zz() {
    return ba;
}
}
``` -->
The only problem here is that this file extends from another file, so all files would have to be obfuscated. Also, the strings were turned into base64 to throw off the hackers. 

Next, let's remove all the whitespaces from this Java file.
```java
public class Pol { public static void main(String a[]) {System.out.println(b(4));} public static int b(int i) {if (i == 0){return 0;} else return b(i - 1) + 2;}}
```

Now, let's add random code to throw the hackers off.

```java
public class Pol { public static void main(String a[]) {System.out.println(b(4));} public static double loo(double p){return p;} public static int b(int i) {if (i == 0){return 0;} else return b(i - 1) + 2;}} public static double che(double a, double b){return a * b;} public static double paw(double a, double b){ return 0.5 * a * b;} public static String aasdfjEIF(String alsdjlfIWFWJLDVNCX){String i = "lJFVIej82348"; return alsdjlfIWFWJLDVNCX + i + kwjeifaiiozI34324;}
```

<!-- ```java
class Ju extends Po {private double ab; private int ba;public Ju(String a, double b, double c)throws Exception {super(a, b);if (c <= 0)throw new Exception("IkludGVyZXN0IHJhdGUgbXVzdCBiZSBncmVhdGVyIHRoYW4gMCI=");this.c = c;
}


public void hh() throws Exception {
    this.jk(ya() * ab);
}

public void ht(double rt) throws Exception {
        ba++;
        if (rt <= 0) {
            ba--;
            throw new Exception("QmFsYW5jZSBpcyBuZWdhdGl2ZQ==");
        }
        if (ba > 6)
            throw new Exception("WW91IGhhdmUgd2l0aGRyYXduIDYgdGltZXMgYWxyZWFkeQ==");
        super.ht(rt);
}

public int zz() {
    return ba;
}
}
``` -->


Although the code may be very obvious as for its function, larger projects will find obfuscation necessary. In addition, the context of the code is fully hidden.

- In the donut example shown in donut.c, the code is shaped in a donut. If someone just took the code and saw it in the donut shape, it'd take longer to piece together because of the difference in whitespace. 

## Demos:

Looking at our demos, the first one is the donut. We added a small feature to change the speed of the rotating donut, and tried to manually obfuscate it by messing with whitespace because of the flexibility of coding in C. 

Next, let's take a look at programs made by other people.

- A really simple online python obfuscator tool is [Oxyry Python Obfuscator](https://pyob.oxyry.com/). It does docstring/comment stripping and it changes the names of functions and variables to something not readable. 

## Programs:

##### Python Docstring/Comment Stripping + Trash Code Insertion 

Our Python program allows you to obfuscate a python file by docstring and comment stripping and inserting trash code.

Docstring and comment stripping makes code less readable. This is because these features provide insight into the purpose and logic of the code. Without these, it would make it harder for hackers to deciper what you are trying to achieve. 

Trash code insertion basically just adds random code that is literally gibberish to make the code more meaningless.

##### Java Name Mangling + Comment Stripping + Removing whitespaces

Our Java program allows you to obfuscate a Java file by removing newlines/whitespaces, removes comments, and name mangles.

Removing newlines will make the code way less readable, removing comments removes the insight of the code, and changing variable names removes the context of each function and the general code.

<!-- ## Our Tool:

In our tool, you can obfuscate any python file using our makefile. The key behind our tool is turning the strings into a different base that isn't human-readable.  -->
