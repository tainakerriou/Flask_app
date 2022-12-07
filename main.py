
from flask import Flask
import logging

app = Flask(__name__)

@app.route('/', methods=["GET"])

def hello_world():
	prefix_google = """
	<!-- Google tag (gtag.js) -->
	<script async
	src="https://www.googletagmanager.com/gtag/js?id=UA-251027646-1"></script>
	<script>
	window.dataLayer = window.dataLayer || [];
	function gtag(){dataLayer.push(arguments);}
	gtag('js', new Date());
	gtag('config', 'UA-251027646-1');
	</script>
	<button class="button button1">Green</button>
	"""
	return prefix_google + "Hello World"


@app.route('/logger', methods=["GET"])

def printlog():
	prefix_google = """
	<!-- Google tag (gtag.js) -->
	<script async
	src="https://www.googletagmanager.com/gtag/js?id=UA-251027646-1"></script>
	<script>
	window.dataLayer = window.dataLayer || [];
	function gtag(){dataLayer.push(arguments);}
	gtag('js', new Date());
	gtag('config', 'UA-251027646-1');
	</script>
	<body>
	<center>
		<h1>Hello Luis</h1>
		<b>Print your message in the console</b>
		<br><br>
		<div class="container">
		<div>
		<label>Write here:</label>
		<input id="textbox" type="text" size="40">
		</div>
		<button id="Send">Send it
			</button>
	<script>
	const element = document.getElementById("Send");
	element.addEventListener("click", myFunction);
	 
	function myFunction() {
    console.log(document.getElementById("textbox").value);
	}

	</script>
	"""
	print('log in Deta')
	logging.warning('Watch out bébé!')
	return prefix_google 
