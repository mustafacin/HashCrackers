#!/usr/bin/python

import hashlib,argparse,sys

try:
	ap = argparse.ArgumentParser()
	ap.add_argument("-w","--wordlist", required=True, help = "wordlist yolunu giriniz.")
	args = ap.parse_args()

except:
	print("\nExample : python md5hashcracker.py -w /usr/share/wordlists/rockyou.txt\n")

args = ap.parse_args()
dosya=open(args.wordlist,"r")
icerik=dosya.read()
dosya.close()

y = raw_input("hash degerini giriniz : ")

for i in icerik.splitlines():
	z = hashlib.md5(i).hexdigest()
	if str(z) in str(y):
		print("\n"+str(y)+"  hash cracked !!!  : "+str(i)+"\n")
                
