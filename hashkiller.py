#!/usr/bin/python

import hashlib

print("""\nWelcome the Hash Paradise :) 
      
        This program is hash cracker with wordlist
        Supported hash types : MD5, SHA1, SHA256, SHA224, SHA384, SHA512                   

github @mustafacin \n\n""")


hash = raw_input("Input your hash : ")
wordlist = raw_input("Input your wordlist : ")

dosya = open(wordlist,"r")
icerik=dosya.read()
dosya.close()
sayac = 0

for i in str(len(hash)):
    if str(i) in str(32):
    	print("\nYour hash is MD5 \n")
        for x in icerik.splitlines():
            cikti = hashlib.md5(x).hexdigest()
            if str(cikti) in str(hash):
                print(str(hash)," md5 is cracked !!!",str(x))
                print("\n")
                sayac = 1
                break
        break       

    if str(i) in str(40):
    	print("\nYour hash is SHA1 \n")
        for x in icerik.splitlines():
            cikti = hashlib.sha1(x).hexdigest()
            if str(cikti) in str(hash):
                print(str(hash)," sha1 is cracked !!!",str(x))
                print("\n")
                sayac = 1
                break
        break 



    if str(i) in str(64):
    	print("\nYour hash is SHA256 \n")
        for x in icerik.splitlines():
            cikti = hashlib.sha256(x).hexdigest()
            if str(cikti) in str(hash):
                print(str(hash)," sha256 is cracked !!!",str(x))
                print("\n")
                sayac = 1
                break
        break     	

    

    if str(i) in str(56):
    	print("\nYour hash is SHA224 \n")
        for x in icerik.splitlines():
            cikti = hashlib.sha224(x).hexdigest()
            if str(cikti) in str(hash):
                print(str(hash)," sha224 is cracked !!!",str(x))
                print("\n")
                sayac=1
                break
        break 

    
    

    if str(i) in str(96):
    	print("\nYour hash is SHA384 \n")
        for x in icerik.splitlines():
            cikti = hashlib.sha384(x).hexdigest()
            if str(cikti) in str(hash):
                print(str(hash)," sha384 is cracked !!!",str(x))
                print("\n")
                sayac=1
                break
        break 

    if str(i) in str(128):
    	print("\nYour hash is SHA512 \n")
        for x in icerik.splitlines():
            cikti = hashlib.sha512(x).hexdigest()
            if str(cikti) in str(hash):
                print(str(hash)," sha512 is cracked !!!",str(x))
                print("\n")
                sayac = 1
                break
        break 

    else:
    	print("This hash value is unsupported")

    



if str(sayac) in str(0):
	print("Not Find this wordlist")
