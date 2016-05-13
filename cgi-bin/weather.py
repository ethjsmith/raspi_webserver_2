import json
import os
import sys
from urllib2 import Request, urlopen, URLError

request = Request('http://api.openweathermap.org/data/2.5/weather?q=Rexburg,us&units=imperial&appid=6cab241c4b4cc4f945f010ec5448902c')

try:
	response = urlopen(request)
	data = json.loads(response.read())
	
	report0 = "The weather today is " + str(data['weather'][0]['main']) + "."
	report1 = " The current temperature is " + str(data['main']['temp']) + " degrees Fahrenheit."
	report2 = " The expected high is " + str(data['main']['temp_min']) + " degrees Fahrenheit,"
	report3 = " and the expected low is " + str(data['main']['temp_max']) + " degrees Fahrenheit."
	report4 = " The current wind speed is " + str(data['wind']['speed']) + " miles per hour."
	fullreport = report0 + report1 + report2 + report3 + report4
	os.system('espeak -a 200 "' + report1 + '"')
	target = sys.argv[1]
	os.system('python /home/pi/emailer.py ' +'"' + target + '"'+ ', "' + fullreport + '"')
except URLError, e:
	print e
