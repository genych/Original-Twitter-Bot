#import urlopen from the url library, and logging
# avoid useless comments

from urllib import urlopen
import logging

logging.basicConfig(filename = "twitterbot.log",level=logging.DEBUG)
logger = logging.getLogger(__name__)

def getOnlineTweets(url):

	#raw list of tweets from the webpage specified
	# rawlist = urlopen(url).read()

	#splitting each line (tweet) into the list tweetlist
	# tweetlist = rawlist.splitlines()
	
	return urlopen(url).readlines()		# should work
	# return is a last operation in functions. all other will be ingored, so too late for logging
	logger.debug("Online tweets retrieved successfully.")

def getPastTweets():
	# same as getOnlineTweets
	pastTweets = open("Tweets/pasttweets.txt", "r")
	
	rawlist = pastTweets.read()

	tweetlist = rawlist.splitlines()

	return tweetlist
	logger.debug("Past tweets retrieved successfully.")
	# too late for closing file
	pastTweets.close()
	
def newTweets(onlineTweets, pastTweets):
		
	# addTweet = True
	# newTweets = []
		
	# for x in onlineTweets:
	# 	for y in pastTweets:
	# 		if x == y:
	# 			addTweet = False
			
	# 	if addTweet == True:
	# 		newTweets.append(x)
	# 	else:
	# 		addTweet = True
			
	# return newTweets

	return [tweet for tweet in onlineTweets if tweet not in pastTweets]
	# also this is even easier (and faster) with sets instead of lists.
	logger.debug("New tweets successfully compared, results are: \n%s" % (newTweets))
	
def writeToPastTweets(statusupdate):

	pastTweets = open("Tweets/pasttweets.txt", "a")

	pastTweets.write(statusupdate+"\n")

	pastTweets.close()

	logger.debug("The tweet \'"+statusupdate+"\' was added to pasttweets.txt")
