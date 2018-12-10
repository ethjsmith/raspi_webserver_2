# raspi_webserver_2

My original raspberry pi webserver (v2 lol ) which was basically my own attempy to make an Alexa device. check out my repo rpi_lightserver for something that's a little more fleshed out, and actually integrates with an Alexa device! 
pretty cool huh? you can look around at the files to see what it's(limited) functionality was
probably not everything works anymore. 
## features

Turn lights on or off
use clock to have the device read out the current time
use weather to have the devices read out what the weather is today (temparature) 
the play function was a work in progress and isn't fully implimented
message can take a message as a parameter, and read it aloud.

## running
I used "screen" with the project which can be used to start a window with ssh that will stay open when you quit the ssh session
`sudo apt install screen`

then to run :
`screen python -m CGIHTTPServer 8000`


## Email login

Creds are stored in environment variables!

Username: os.environ['EMAILER_EMAIL']
Password: os.environ['EMAILER_PASSWORD']
