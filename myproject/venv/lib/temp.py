from flask import Flask
from flask import Flask, request, render_template
import json
from youtube_transcript_api import YouTubeTranscriptApi
import csv
from urllib.parse import urlparse
from fuzzywuzzy import fuzz
import urllib.parse
import pandas as pd

app = Flask(__name__)


@app.route('/',methods=["GET", "POST"])
def hello():
	return render_template('index.html')

@app.route('/response', methods=['GET','POST'])
def response():
	if request.method == 'POST':
		url = request.form.get("url")
		video_url=urlparse(url)
		query_data = urllib.parse.parse_qs(video_url.query)
		site = video_url.netloc
		if(site!="www.youtube.com"):
			return "Please Enter a Valid Youtube URL"
		youtube_id = query_data['v'][0]

		transcript = YouTubeTranscriptApi.get_transcript(youtube_id)
		transcript_search_data=[]
		transcript_text=""
		transcript_line=""
		for line in transcript:
			transcript_line+=line['text'].replace("\n"," ")
			transcript_text+=transcript_line

		return render_template("index.html",transcript_content=transcript_text)

if __name__ == '__main__':
	app.run()
	app.config["DEBUG"] = True