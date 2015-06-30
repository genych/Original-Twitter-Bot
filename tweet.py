#tweepy is the twitter library I am using, and have installed on this rpi
import tweepy
import logging
from mail import sendmail
from sys import exit

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

#setting up with OAuth using the various keys
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def tweet(statusupdate, erroremail):
	
	if len(statusupdate) > 140:
		raise Exception("Status message is too long!")
		# that's it. you'll get error message and program will be terminated. should be try-except block or (better) simple check and maybe truncating message
		logger.error("Status message was too long!\n\nStatus:\n%s" % statusupdate)
		sendmail(erroremail, "TWEET ERROR", "Status update for @youraccount has not been posted, update was too long.\n\nStatus:\n%s" % statusupdate)
		
	try:
		result = api.update_status(status=statusupdate)

		logger.info("Status updated:\n\'%s\'" % statusupdate)
		print "Status updated:\n\'%s\'" % (result.text)
	except IOError:
		exit()		# what?! no logging, no warnings, just (╯°□°）╯ ︵ ┻━┻ ? this isn't good
	except Exception as ex:
		logger.error("ERROR TWEET WAS NOT POSTED: "+str(ex))
		sendmail(erroremail, "TWEET ERROR", "Status update for @youraccount has not been posted, reason given: "+str(ex))
