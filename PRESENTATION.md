## What is code obfuscation?

First, let's take a look at the word obfuscation, which means to make something difficult to understand. Code obfuscation means to make code difficult to understand or compile. 

## Why is code obfuscation important?

Hiding your code is very important because in the worst case scenario that your code is stolen by bad actors, then you wouldn't want them to know how it works. It will make it difficult for them to understand how your code works and how to compile it to use it for their own benefit. If the hackers eventually do crack the code, it will take them a long time, which may be enough time to catch them.

Essentially, it will hinder the ability of hackers who steal code to understand your code. 

HOWEVER, it is important to note that code obfuscation does not help increase the security of your code AT ALL. Keeping your data safe is your own responsibility and code obfuscation does not hide your data; it only makes your code unreadable. 

## What are the different methods you can use to obfuscate code? 

There are so many ways to make your code unreadable, complex, and hard to understand. 

- Name Mangling

One way is by renaming all of your variables, function names, and parameters to single letters instead of their intended use. This will make your code harder to understand if there are no good naming conventions. 

- Removing whitespace

Removing whitespace is one of the easiest ways to make code harder to understand. However, some coding languages may prevent the full ability of this. In Python, indentations are necessary to actually make code function. 

- Trash Code Insertion

- Comments/Docs Stripping

## Examples:

- The primary example we will use is code in Java, for a simple savings account:
```java
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
```

[add the different ways this code can be edited]

- In the donut example shown in donut.c, the code is shaped in a donut. If someone just took the code and saw it in the donut shape, it'd take longer to piece together because of the difference in whitespace. 



## Programs:

##### Docstring and Comment Stripping + Trash Code Insertion ()

Docstring and Comment Stripping makes code less readable. This is, because these features provide insight into the purpose and logic of the code. Without these, it would make it harder for hackers to deciper what you are trying to achieve. 

Trash code insertion ...

##### Java obfuscate

## Demos:

Looking at our demos, the first one is the donut. 

Next, let's take a look at programs made by other people (we could use pyarmor, proguard,...)

<!-- ## Our Tool:

In our tool, you can obfuscate any python file using our makefile. The key behind our tool is turning the strings into a different base that isn't human-readable.  -->
