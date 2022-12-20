# Youtube-Study-Buddy

## About The Project
The app is your perfect companion while you binge youtube videos to study and revise. The app helps you in note-taking as well as searching through long video lectures.

- The app takes the Youtube Video URL as input.
- The video, as well as its transcript, is displayed.
- The Time-Stamped Transcript is available too. On clicking the particular time, the app will start playing the video at the specific time-stamp.
- The app also allows you to search a particular content and the time-stamp in the video based on the search query. The app also starts playing at the specific time-stamp on clicking the relevant result you need.
- The app also provides all releveant tools to make notes including highlighting, note editing as well as downloading your notes


## Installation

###### The app is available and can be used at: (currently unavailable due to paid heroku hosting services)
https://youtube-study-buddy.herokuapp.com/

###### Local Installation:

Download the zip folder Youtube Study Buddy App. 
(Link: https://github.com/AnushaNathRoy/Youtube-Study-Buddy/tree/main/Youtube-Study-Buddy%20App)

On terminal write the commands:

```sh
 cd Youtube Study Buddy App
 export FLASK_APP=Main.py
```

Install the dependencies:

```sh
pip install -r requirements.txt
```

Run the app by using command:

```sh
flask run
```

## Using The App

#### Main Page

**Enter Valid Youtube URL:**
Enter a valid Youtube URL starting with https://www.youtube.com/.

**Search in Video:**
Enter search query to search in the video. It can be entered later too.

**Warnings:**
 *Invalid Link! Please try again!* => The link entered is not a valid Youtube URL. Please check if it starts with " https://www.youtube.com/"
*Transcript Not Available :(( Sorry Try Some Other Video.* => Sorry, the transcript is not available for the video entered in this case. You can always enter another video,  

![alt text](https://github.com/AnushaNathRoy/Youtube-Study-Buddy/blob/main/readmeImages/mainmenu.png)
---


#### Navbar Options
**Home button** - Allows you to navigate back to homepage.

**Transcript** - Allows you to view the entire transcript at once.

**Time-Stamped Transcript** - It provides the transcipt time-stamped. Clicking on the particular time-stamp will play the video at the exact time-stamp.

**Search** - This allows you to search for any content in transcript and provides a list of relevant searches. You don't need to type the exact sentence, the search feauture will take care of it and give you all the relevant choices.

![alt text](https://github.com/AnushaNathRoy/Youtube-Study-Buddy/blob/main/readmeImages/navbar.png)
---

#### Study Mode
**Highlight Mode** - It is a toggle button. On switching on the toggle button you will be given an option to enter the hex code of the highlight color that you like. Not entering a hex value will use the default yellow highlight.

**Get Highlighted Text** - On clicking this button all the higlighted text will be copied to your clipboard. You can now easily paste this in the notes editor and make notes easily. 

**Save Notes** - Saving notes will save your notes across various videos. You can open different videos and edit on the same notes. 

**New Note**- This will delete your notes and start a new fresh and clean note.

**Download Notes (MarkDown)** - This will download a markdown of the notes you made.

![alt text](https://github.com/AnushaNathRoy/Youtube-Study-Buddy/blob/main/readmeImages/studymode.png)
---

#### Notes Editor

You can use this to make and edit your notes while studying. The are options to make tables, bold and highlight text and many more!



## Demo
Check out the demo at Demo.md

Link: https://github.com/AnushaNathRoy/Youtube-Study-Buddy/blob/main/Demo.md

## License

MIT

**References:**
[video in demo]: <https://www.youtube.com/watch?v=yOgAbKJGrTA>
[video in demo]: <https://www.youtube.com/watch?v=I4pQbo5MQOs>
   
 
