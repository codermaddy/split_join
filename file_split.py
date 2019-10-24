#!/usr/bin/python3

"""split a file into a set of parts; file_join.py puts them together;
this is a customizable version of the standard Unix split command-line
utility; because its written in python, it also works in windows and
can be easily modified; because it exports a function, its logic can
also be imported and reused in other applications;"""

import os,sys

kb = 1024
mb = 1024*1024
chunksize = 5*mb

def split(fromfile, todir, chunksize=chunksize):
	if not os.path.exists(todir):
		os.mkdir(todir)
	else:
		for fname in os.listdir(todir):
			os.remove(os.path.join(todir, fname))
	partnum = 0
	finput = open(fromfile,'rb')
	while True:
		chunk = finput.read(chunksize)
		if not chunk: break
		partnum += 1
		filename = os.path.join(todir,('part%04d'%partnum))
		with open(filename,'wb') as fileobj:
			fileobj.write(chunk)
	finput.close()
	assert partnum <= 9999, 'No. of parts must be less than 10000'
	return partnum	

if __name__ == '__main__':
	if len(sys.argv) == 2 and sys.argv[1] == '-help':
		print("Usage: %s [file-to-split target-dir [chunksize]]"%(sys.argv[0]))
	else:
		if len(sys.argv) < 3:
			interactive = True
			fromfile = input("File to be split ? ")
			todir = input("Directory to store part files ? ")
		else:
			interactive = False
			fromfile, todir = sys.argv[1:3]
			if len(sys.argv) == 4: chunksize = int(sys.argv[3])
		absfrom, absto = map(os.path.abspath,[fromfile,todir])
		print('Splitting',absfrom,'to',absto,'by',chunksize)
		try:
			parts = split(fromfile,todir,chunksize)
		except:
			print('Error during split')
			print(sys.exc_info()[0],sys.exc_info()[1])
		else:
			print('Split finished:',parts,'parts are in',absto)
			if interactive: input('Press Enter key')  