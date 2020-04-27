#!/usr/bin/python
"""
Author: Khalu
A simple script to brute force a zip file that is password protected.
Requires a password file like rockyou.txt
"""

from zipfile import ZipFile
import argparse



def arguments():
	parser = argparse.ArgumentParser(description='Brute Force a zip file password')
	parser.add_argument('--wordlist', '-w', help='The wordlist for brute forcing')
	parser.add_argument('--zipfile',  '-f', help='The target zip file')
	return parser.parse_args()



def crack_zip(input_file, word_list):
	with ZipFile(input_file) as zf:
		with open(word_list) as f:
			pwlist = f.readlines()
		for pw in pwlist:
			pw = pw.strip()
			try:
				zf.extractall(pwd=pw)
				print("password for {} is {}").format(input_file, pw)
				exit()
			except:
				continue


args = arguments()
crack_zip(args.zipfile, args.wordlist)
print("No passwords found")
