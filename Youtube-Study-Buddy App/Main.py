from flask import Flask
from flask import send_from_directory
from flask import Flask, request, render_template
import json
from youtube_transcript_api import YouTubeTranscriptApi
import csv
from urllib.parse import urlparse
from fuzzywuzzy import fuzz
import urllib.parse
from random import randint
from random import seed
import datetime
import pandas as pd
import os

app = Flask(__name__, static_folder='app/lib/static')
app._static_folder = os.path.abspath("static/")
url=""
@ app.route('/static/<path:filename>')
def static_load(filename):
	seed=(1)
	root_dir = os.path.dirname(os.getcwd())
	return send_from_directory(os.path.join(root_dir, 'static'), filename)       
	# return send_from_directory("static",filename)
@ app.route('/static/css/<path:filename>')
def static_load_css(filename):
	root_dir = os.path.dirname(os.getcwd())
	return send_from_directory(os.path.join(root_dir, 'static','css'), filename) 

@app.route('/',methods=["GET", "POST"])
def hello():
	v=randint(0,999)
	main=1
	return render_template('index.html',version=v,m=main)

@app.route('/response', methods=['GET','POST'])
def response():
	seed=(1)
	v=randint(0,999)
	if request.method == 'POST':
		url = request.form.get("url")
		video_url=urlparse(url)
		query_data = urllib.parse.parse_qs(video_url.query)
		site = video_url.netloc
		if(site!="www.youtube.com"):
			invalid=1
			return render_template("index.html", invalid=invalid, version=v)
		youtube_id = query_data['v'][0]

		search_query = request.form.get("search")
		search_words = []
		search_words = search_query.split(" ")
		
		try:
			transcript = YouTubeTranscriptApi.get_transcript(youtube_id)
		except:
			linvalid=1
			return render_template("index.html", linvalid=linvalid, version=v)

		transcript_search_data=[]
		transcript_text=""
		transcript_line=""
		for line in transcript:
			transcript_line+=line['text'].replace("\n"," ")
			transcript_text+=transcript_line
			line["start"] = str(datetime.timedelta(seconds=int(line["start"])))
			rank = fuzz.partial_ratio(search_query.lower(),transcript_line.lower())
			for word in search_words:
				if (transcript_line.find(word) != -1):
					rank+=50
			line['rank'] = rank

		with open ('transcript_csv.csv','w') as w:
			fieldnames = transcript[0].keys()
			wwrite = csv.DictWriter(w,fieldnames=fieldnames)
			wwrite.writeheader()
			wwrite.writerows(transcript)

		csv_data = pd.read_csv("transcript_csv.csv")
		sorted_csv_data = csv_data.sort_values(by=["rank"], ascending=False)
		sorted_csv_data.to_csv("transcript_sorted.csv",index=False)

		w.close()

		r = open("transcript_sorted.csv","r")
		data=list(csv.DictReader(r))

		return render_template("index.html",transcript_content=transcript_text,video_urlp=youtube_id,transcript_data=transcript,transcript_datas = data,version=v,urlv=url)

if __name__ == '__main__':
	app.run()
	app.config["DEBUG"] = True