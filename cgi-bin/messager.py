import sys
import os
def parse (mssg):

	ary = mssg.split('_')
	
	
	return ary
def read (msg):
        for i in range(0,len(msg)):
                os.system('espeak "' + msg[i] + '"')
msg = sys.argv[1]
read(parse(msg))