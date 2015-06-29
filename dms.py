import tweepy
import logging

#capture warnings in the log
logging.captureWarnings(True)

#set up logging
logging.basicConfig(filename = "twitterbot.log",level=logging.DEBUG)
logger = logging.getLogger(__name__)

#all the important keys and tokens needed to authenticate myself as @txisntbigger
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def getNewDMs():

	#declare dms as a list
	dms = []

	logger.info("Retrieving new direct messages...")
	#for each direct message...
	for x in api.direct_messages():
		#set username and message to the correct values
		username = x.sender_screen_name
		message = x.text
		
		#append the username and message to the dms list
		dms.append("%s: %s" % (username, message))

	return dms
	logger.debug("%s new DMs retrieved." % len(dms))
