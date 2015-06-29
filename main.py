#import necessary python modules
import logging
from time import sleep

#importing my own local modules
from checktime import checktime
import tweetretriever
from mail import sendmail
from dms import getNewDMs
from tweet import tweet

#setting program to log in a file called twitterbot.log, outputting at the debug level
logging.basicConfig(filename="twitterbot.log",level=logging.DEBUG)
logger = logging.getLogger(__name__)

tweettimes = [10,20]

emailrecipient = ""
emailsubject = "Twitter Bot Status Update"
emailbody = ""

while True:

	print "To Terminate this process, you must either kill the Python process on this system entirely, or reboot the computer"
	print "DO NOT JUST CLICK THE \'X\'"

	#clear the log file for new writing so it never gets to be too big
	log = open("twitterbot.log", "w")
	log.truncate()
	log.close()
	logger.info("Created new log file.")

	logger.debug("Tweet times set in main.py are %s:00 and %s:00." % (tweettimes[0], tweettimes[1]))
	
	#Getting new tweets, emailing number of tweets left
	logger.info("Getting online tweets...")
	onlineTweets = tweetretriever.getOnlineTweets("yoururlhere(I used pastebin, if you do the same you can put the raw url here)")

	logger.info("Getting past tweets...")
	pastTweets = tweetretriever.getPastTweets()

	logger.info("Comparing online and past tweets...")
	newTweets = tweetretriever.newTweets(onlineTweets, pastTweets)
	
	if newTweets != None and newTweets != []:
		emailsubject = "Twitter Bot Status Update"
		emailbody += "%s new Tweets left in database:\n\n%s" % (len(newTweets), newTweets)
		logger.info("%s new tweets were retrieved." % len(newTweets))	
	else:
		emailsubject = "TWITTER BOT DATABASE ERROR"
		emailbody += "No new tweets left in database! Add more ASAP!"
		logger.error("No new tweets left in database!")
	
	#setting next tweet
	nextTweet = newTweets[0]
	logger.debug("Set next tweet to \'%s\'" % nextTweet)

	logger.debug("Sending annual email to %s..." % emailrecipient)
	#sending annual email to myself to make sure everything is running smoothly
	sendmail(emailrecipient, emailsubject, emailbody)
	
	logger.info("Checking time...")
	#checktime sleeps until the given hours in the parameters
	checktime(tweettimes[0],tweettimes[1])
	
	#these are for debugging
	#print "sleeping"
	#sleep(30)

	logger.info("Tweeting...")
	#emailrecipient is needed because if there is a tweet error, it will send to that email
	tweet(nextTweet, emailrecipient)
	
	logger.info("Adding Tweet to pasttweets.txt...")
	#adding tweet that was just tweeted to past tweets
	tweetretriever.writeToPastTweets(nextTweet)
	
	logger.info("Checking for new DMs...")
	#check DMs
	newDMs = getNewDMs()
	
	#set up DMs to be sent in email
	emailbody = "@youraccount has %s new DMs.\n\n" % (len(newDMs))
	for x in newDMs:
		emailbody += x + "\n"
	
	emailbody += "\n"
