import os
import sys
def checkMusic():
	song = os.listdir('C:/Users/admin/Desktop/webserver/music')
	fullist = ''
	for item in song:
		item = item.replace('_','')
		item = item.replace('.mp3','')
		fullist += item + '  '
	return fullist
print checkMusic()
