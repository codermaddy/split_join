#!/usr/bin/python3

"""join a set of files into a file; file_split.py split them up;
this is a customizable version of the standard Unix split command-line
utility; because its written in python, it also works in windows and
can be easily modified; because it exports a function, its logic can
also be imported and reused in other applications;"""

import sys
import os

readsize = 1024


def join(fromdir, tofile):
	foutput = open(tofile, 'wb')
	parts = os.listdir(fromdir)
	parts.sort()
	for filename in parts:
		filepath = os.path.join(fromdir, filename)
		fileobj = open(filepath, 'rb')
		while True:
			filebytes = fileobj.read(readsize)
			if not filebytes:
				break
			foutput.write(filebytes)
		fileobj.close()
	foutput.close()		


if __name__ == '__main__':
	if len(sys.argv) == 2 and sys.argv[1] == '-help':
		print("Usage: %s [from-dir-name to-file-name]"%(sys.argv[0]))
	else:
		if len(sys.argv) < 3:
			interactive = True
			fromdir = input("Directory containing the split files ? ")
			tofile = input("Name of file to be created ? ")
		else:
			interactive = False
			fromdir, tofile = sys.argv[1:3]
		absfrom, absto = map(os.path.abspath,[fromdir,tofile])
		print('Joining', absfrom, 'to make', absto)
		try:
			join(fromdir, tofile)
		except:
			print('Error joining files')
			print(sys.exc_info()[0], sys.exc_info()[1])
		else:
			print('Join complete: see', absto)
		if interactive:
			input('Press Enter key to quit')

