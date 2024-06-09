compile:
	@gcc -o donutExample donut.c -lm 
	@gcc -o prog prog.c
	@./prog > 1.c
	@gcc -o 1 1.c
	@./1 > 2.c
	@gcc -o 2 2.c
	@./2 > 3.c
	@gcc -o 3 3.c
	@./3 > 4.c
	@gcc -o 4 4.c
	@./4 > 5.c
	@gcc -o 5 5.c
	@./5 > 6.c
	@gcc -o 6 6.c
	@./6 > 7.c
	@gcc -o 7 7.c
	@./7 > 8.c
	@gcc -o 8 8.c
	@./8 > 9.c
	@gcc -o 9 9.c

donut: donutExample
	@./donutExample

parrot: prog
	@while :; do \
		./prog | tee prog_next.c; \
		gcc prog_next.c -o ./prog; \
		sleep 0.1; \
	done

clean:
	@rm -f *.o *.class prog donutExample 1 2 3 4 5 6 7 8 9 2> /dev/null || true