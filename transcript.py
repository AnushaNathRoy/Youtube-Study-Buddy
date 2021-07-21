# libraries and import
import json
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse
import urllib.parse
import pandas as pd

#recieves video_url and search query 
video_url=input("Enter Youtube Video URL: ")
search_query = input("Enter what you want to search: ")

#gets a list of words that need to be searched
search_words=[]
search_words = search_query.split(" ")
print(search_words)

video_url=urlparse(video_url)
query_data = urllib.parse.parse_qs(video_url.query)
youtube_id = query_data['v'][0]

transcript = YouTubeTranscriptApi.get_transcript(youtube_id)
transcript_search_data=[]
transcript_text=""
transcript_line=""
for line in transcript:
	transcript_line+=line['text'].replace("\n","")
	transcript_text+=transcript_line
	for word in search_words:
		print("")


print(transcript_text)
# https://www.youtube.com/watch?v=I4pQbo5MQOs
