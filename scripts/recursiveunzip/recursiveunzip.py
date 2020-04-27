#!/usr/bin/python
import filetype
import os, argparse


def get_type(input_file):
	"""
	Uses the module filetype to check the Magic Number of the input_file variable
	and returns the type
	"""
	archive_types= ["gzip", "x-tar", "zip"]
	type = filetype.guess(input_file)
	try:
		type = (type.mime).split("/")[1]
		if type and type in archive_types:
			return type
		else:
			return False
	except:
		print("Last file is {}".format(input_file))
		print("Is this what you where looking for?")
		os.system("cat {}".format(input_file))
		exit()



def uncompress(file):
	"""
	Takes input file, finds the type of compressed file using get_type function
	and attempts to decompress it using system
	"""
	file_type = file["file_type"]
	file = file["file"]
	if file_type == "gzip":
		# gunzip seemed to have an issue unless the file had the .gz extension
		# on my system
		if ".gz" not in file:
			os.system("mv {} {}".format(file, file+".old.gz"))
			file = file + ".old.gz"
		print("gunzipping {}".format(file))
		os.system("gunzip {}".format(file))
	elif file_type == "x-tar":
		print("tar xtracting {}".format(file))
		os.system("tar xvf {}".format(file))
	elif file_type == "zip":
		print("unzip {}".format(file))
		# echo y to acknowledge the prompt that unzip displays
		os.system("echo y | unzip {}".format(file))
	else:
		print("unknown compression")

def find_new_file(old_file):

	for (dirpath, dirname, filenames) in os.walk("./"):
		for file in filenames:
			if file != old_file and get_type(file):
				return {"file": file, "file_type": get_type(file)}


def arguments():
	parser = argparse.ArgumentParser(description='Recusively decompress')
	parser.add_argument('--directory', '-D', help='The directory with the recursively compressed file', default="./")
	return parser.parse_args()


directory = arguments().directory
os.chdir(directory)
new_file = find_new_file("")

while new_file:
		uncompress(new_file)
		old_file = new_file["file"]
		os.system("rm {}".format(old_file))
		new_file = find_new_file(old_file)
		if not new_file["file_type"]:
			print("Last file is {}".format(new_file["file"]))
			break
			
print("No more files to extract")
