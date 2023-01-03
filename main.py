
import requests
from flask import Flask, render_template
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
#from dotenv import load_dotenv
#import os


app = Flask(__name__)
#load_dotenv(".env")
SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'datasource-373523-383f8cf8a396.json' #str(os.getenv("file_json"))
VIEW_ID = '281180695' #str(os.getenv("view_id"))


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

	return prefix_google


def initialize_analyticsreporting():
  credentials = ServiceAccountCredentials.from_json_keyfile_name(
      KEY_FILE_LOCATION, SCOPES)
  analytics = build('analyticsreporting', 'v4', credentials=credentials)

  return analytics


def get_report(analytics):
  return analytics.reports().batchGet(
      body={
        'reportRequests': [
        {
          'viewId': VIEW_ID,
          'dateRanges': [{'startDate': '30daysAgo', 'endDate': 'today'}],
          'metrics': [{'expression': 'ga:pageviews'}],
          'dimensions': []
        }]
      }
  ).execute()


def get_visitors(response):
  visitors = 0 # in case there are no analytics available yet
  for report in response.get('reports', []):
    columnHeader = report.get('columnHeader', {})
    metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])

    for row in report.get('data', {}).get('rows', []):
      dateRangeValues = row.get('metrics', [])

      for i, values in enumerate(dateRangeValues):
        for metricHeader, value in zip(metricHeaders, values.get('values')):
          visitors = value

  return str(visitors)

@app.route('/visitors')

def visitors():
  analytics = initialize_analyticsreporting()
  response = get_report(analytics)
  visitors = get_visitors(response)

  return render_template('visitors.html', visitors=str(visitors))

if __name__ == '__main__':
	app.run()
        

	