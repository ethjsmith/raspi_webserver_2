import os
import sys
# track = ''
def check_music():
	song = os.listdir('/home/pi/music')
	fullist = ''
	for item in song:
		item = item.replace('_','')
		item = item.replace('.mp3','')
		fullist += item + '  '
	return fullist

if len(sys.argv) > 1 and os.path.exists('/home/pi/music/_' + sys.argv[1] + '.mp3'):
	os.system('omxplayer /home/pi/music/_' + sys.argv[1] + '.mp3')
else:
	target = sys.argv[2]
	target = '"' + target + '"'
	body = 'Song not recognized, here is a list of recognized songs : ' + check_music()
	os.system('python /home/pi/emailer.py ' + target + ', "' + body + '"')


