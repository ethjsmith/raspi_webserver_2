import smtplib
import sys
print 'I made it here'
fromaddr = 'ethanmailserverbot@gmail.com'
toaddrs  = str(sys.argv[1])
bodyofmessage = sys.argv[2]
msg = "\r\n".join([
  "From: ethanmailserverbot@gmail.com",
  'To:'+toaddrs ,
  "Subject: Automessage",
  "",
  bodyofmessage
  ])
username = 'ethanmailserverbot@gmail.com'
password = 'botsdontneedpasswords'
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
