# raspi_webserver_2

This is pretty old and outdated, but used to run a webserver on a raspberry PI which was interacted with VIA email

pretty cool huh? you can look around at the files to see what it's(limited) functionality was

probably not everything works anymore. don't bother trying to use the email creds, as they've changed...

## Email login

Credentials should be stored in environment variables.

Username: os.environ['EMAILER_EMAIL']
Password: os.environ['EMAILER_PASSWORD']
