compile:
	@gcc -o donutExample donut.c -lm 
	@javac Recursion.java
	@javac obRecursion.java
	@javac obRecursion2.java
	@javac obRecursion3.java

donut: donutExample
	@./donutExample $(ARGS)

clean:
	@rm -f *.o *.class 2> /dev/null || true