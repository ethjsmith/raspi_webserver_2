# This is the overseer file for the rasberry PI
import imaplib
import os
import time
from email.parser import Parser
import subprocess

       

def get_email():
        stat,count = srvr.select('inbox')
	stat,data = srvr.fetch(int(count[0]),'(RFC822)')
	email = Parser().parsestr(data[0][1])
	if email.is_multipart():
		for payload in email.get_payload():
			bod = payload.get_payload()
			#print bod[0]
			
	else:
		bod = email.get_payload()
	sub = email['subject']
	sender = email['from']
        print sub
	bod2 = bod[13:len(bod)-6]
	driver(sub,bod2,sender)
	                      

def music_player(number):
	os.system('omxplayer /home/pi/music/_' + number + '.mp3')

def check():
	stat,count = srvr.select('inbox')
        unread = srvr.search(None,"UnSeen")
        if unread[1][0] == "":
                pass
        else:
                get_email()

def parse (msg):
	ary = msg.split(' ')
	return ary
def read (msg):
        for i in range(0,len(msg)):
                os.system('espeak -a 200 "' + msg[i] + '"')
        
def driver(subject,body,sender):
	subject = subject.lower()
        if subject == "clock":
                os.system("python clock.py")
                print "clock is running"
        elif subject == "weather":
		subprocess.Popen(['python','weatherV2.py',sender, '&'])
                #os.system("python weatherV2.py")
        elif subject  == "message":
                read(parse(body))
	elif subject == 'play':
		subprocess.Popen(['python','music_manager.py',body.lower(),sender, '&'])
        else:
                print "No valid message"
		print subject,body


                 
                

srvr = imaplib.IMAP4_SSL('imap.gmail.com',993)
username = 'ethanmailserverbot'
password = 'botsdontneedpasswords'
end = time.time() + 60*10
repeat = True
srvr.login(username,password)
while repeat:
	
	
	
        check()
	if time.time() >= end:
		srvr.close()
        	srvr.logout()
		break
	