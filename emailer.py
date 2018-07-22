import smtplib
import sys
import os
print 'I made it here'
fromaddr = os.environ['EMAILER_EMAIL']
toaddrs  = str(sys.argv[1])
bodyofmessage = sys.argv[2]
msg = "\r\n".join([
  "From: " + os.environ['EMAILER_EMAIL'],
  'To:'+toaddrs ,
  "Subject: Automessage",
  "",
  bodyofmessage
  ])
username = os.environ['EMAILER_EMAIL']
password = os.environ['EMAILER_PASSWORD']
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
