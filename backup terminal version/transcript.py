# libraries and import
import json
import json
from youtube_transcript_api import YouTubeTranscriptApi
import csv
from urllib.parse import urlparse
from fuzzywuzzy import fuzz
import urllib.parse
import pandas as pd

#recieves video_url and search query 
video_url=input("Enter Youtube Video URL: ")
search_query = input("Enter what you want to search: ")


video_url=urlparse(video_url)
query_data = urllib.parse.parse_qs(video_url.query)
site = video_url.netloc
if(site!="www.youtube.com"):
	print("Please Enter a Valid Youtube URL")
	exit()
youtube_id = query_data['v'][0]

search_words = []
search_words = search_query.split(" ")

transcript = YouTubeTranscriptApi.get_transcript(youtube_id)
transcript_search_data=[]
transcript_text=""
transcript_line=""
for line in transcript:
	transcript_line+=line['text'].replace("\n","")
	transcript_text+=transcript_line
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

ch = input("Do you want to print the transcript?(Y/N)")
if(ch=='Y' or ch =='y'):
	print(transcript_text)
# https://www.youtube.com/watch?v=I4pQbo5MQOs

'''

requirements:
pip install python-Levenshtein
pip install fuzzywuzzy
pip install youtube_transcript_api
pip install pandas

'''
