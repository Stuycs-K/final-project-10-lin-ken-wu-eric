pyObfuscate: 
	@python3 obfuscate.py $(ARGS)

clean:
	@rm -f *.o server client 2> /dev/null || true