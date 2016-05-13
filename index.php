
<!DOCTYPE HTML>
<html lang="en-us">
	<head>
	<meta charset="utf-8">
	<meta name="author" content="Ethan Smith">
	<title>Webserver test site</title>
	<link rel="stylesheet" type="text/css" href="stylesheet.css" media = 'screen' >
	<script type = 'text/javascript'>
	function message(){
	var msg = window.prompt("enter the message you want read!");
	window.alert(msg);
	}
	function playsound(){
	var song = window.prompt("What song would you like to play?");
	
	}
	
	
	</script>

	</head>

	<body>
	Rasberry pi control center<br>
	<button type = 'button' class = 'button' onClick = "<?php exec('python clock.py'); ?>" > Time of day</button><br>
	<button type = 'button' class = 'button'>Weather</button><br>
	<button id = 'messagerbutton' type = 'button' class = 'button' onClick = 'message()' >message</button><br>
	<button id = 'musicbutton' type = 'button' class = 'button' onClick = 'playsound()' >play song</button><br>
		</body>
</html>
