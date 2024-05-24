def decode(arg1, arg2):
    with open(arg1, "rb") as f:
        cipher = f.read()
    
        key = open(arg2)
        key = key.read()
    
        keyIndex = 0
        results = ""
    
        for i in range(len(cipher)):
            a = format(cipher[i], '02x')
            b = (ord(chr(int(a, 16))) ^ ord(key[keyIndex]))
            results += chr(b)
            if (keyIndex == len(key) - 1):
                keyIndex = 0
            else:
                keyIndex += 1

    print(results)