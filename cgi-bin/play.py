#!/usr/bin/env python
import os
import sys
def parse (mssg):
	ary = mssg.split('_')
	return ary
var song = parse(sys.argv[1])
os.system('omxplayer /webserver/music/' + song + '.mp3')
