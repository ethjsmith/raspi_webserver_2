import time
from pi_switch import RCSwitchSender

snd = RCSwitchSender()
snd.enableTransmit(0)

on =1655303 
off = 1655302
snd.sendDecimal(off,24)

