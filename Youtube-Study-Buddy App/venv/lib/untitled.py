@app.route('/, methods=["GET", "POST"]')
def hello_world():
    return 'Hi from Flask!'

def urldata(video_url):
	video_url=urlparse(video_url)
	query_data = urllib.parse.parse_qs(video_url.query)
	site = video_url.netloc
	if(site!="www.youtube.com"):
		print("Please Enter a Valid Youtube URL")
		exit()
	youtube_id = query_data['v'][0]



def urldata(video_url):
	video_url=urlparse(video_url)
	query_data = urllib.parse.parse_qs(video_url.query)
	site = video_url.netloc
	if(site!="www.youtube.com"):
		print("Please Enter a Valid Youtube URL")
	youtube_id = query_data['v'][0]

errors = ""
    if request.method == "POST":
        video_url = None
        try:
            video_url = float(request.form["Type Valid Youtube URL:"])
        except:
            errors += "<p> {!r} Please type URL</p>\n".format(request.form["Type Valid Youtube URL:"])


        if video_url is not None:
            result = urldata(video_url)
            return '''
                <html>
                    <body>
                        <p>The result is {result}</p>
                        <p><a href="/">Click here to calculate again</a>
                    </body>
                </html>
            '''.format(result=result)

            return '''
			<html>
			    <body>
			        {errors}
			        <p>Enter your numbers:</p>
			        <form method="post" action=".">
			            <p><input name="Type Valid Youtube URL:" /></p>
			            <p><input type="submit" value="Transcript" /></p>
			        </form>
			    </body>
			</html>
		'''.format(errors=errors)