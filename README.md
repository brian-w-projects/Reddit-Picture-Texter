# redditPictureTexter
# Text yourself pictures from any subreddit at set intervals of time

<h2>Overview:</h2>
<p>This program uses Twilio to text your cell phone pictures from any subreddit at set 
times of your choosing. Program can be modified to your liking.</p>

<h2>Schedule</h2>
<p>This program uses, and includes, the schedule class. Please read the schedule readme
for information on how this program works and how to add/remove times</p>

<h2>Reddit Grabber</h2>
<p>This class assists with organizing and combining all the elements used by the main
redditsender program. Running the main program will allow you to save/load these
Reddit Grabber files for easy organization. </p>

<h2>Reddit Sender</h2>
<p>In order to get this program up and running, you will need to supply various pieces of
information to the top of the program. Descriptions of these pieces of information is
below.</p>

<h4>ACCOUNT_SID, AUTH_TOKEN, TWILIO_NUMBER, MY_NUMBER:</h4>
<p>This information requires an account on twilio.com. Sign up for a free account and look
on your profile for all of the indicated information. Before you can begin texting yourself
you will need to verify your number by entering a verification code.</p>

<h4>MY_CLIENT_ID, MY_CLIENT_SECRET, USER_AGENT:</h4>
<p>Beginning with the recently released praw 4, you will need to provide three pieces of
information to the praw constructor to grab information off of reddit. The client
information requires that you register a develop app with reddit. Information can 
be found here, at reddit's github: https://github.com/reddit/reddit/wiki/OAuth2</p>

<p> The user agent information is an identier used by Reddit to ensure you are not making 
too many requests. Select any suitable long random array of characters. </p>
