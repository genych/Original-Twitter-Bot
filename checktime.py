#importing datetime, time.sleep, and logging
from datetime import datetime
from time import sleep
import logging

#setting up logging
logging.basicConfig(filename = "twitterbot.log", level=logging.DEBUG)
logger = logging.getLogger(__name__)

#sleeptime function, basically just prints amount of time the system sleeps between tweets in a certain fashion
def sleeptime(hoursleft, minutesleft, seconds):
	return "sleeping for %s hours and %s minutes (%s seconds)" % (hoursleft, minutesleft, seconds)

#findseconds function, does some simple (yet repetitive) math
def findseconds(hoursleft, minutesleft):
	return hoursleft*3600 + minutesleft*60

#the main function of this file
def checktime(timeNumberOne, timeNumberTwo):
	
	#set tweet times
	tweettimes = [timeNumberOne,timeNumberTwo]
	logger.debug("Tweet times are %s:00 and %s:00" % (tweettimes[0], tweettimes[1]))
	
	logger.info("Resetting current time...")
	#resetting current date and time
	now = datetime.now()
	
	#prints current time
	print "Currrent time is %s:%s" % (now.hour, now.minute)
	logger.info("Current time is %s:%s" % (now.hour, now.minute))
	
	#assigning minutesleft, as it is always the same no matter the hour
	minutesleft = 60-now.minute
	
	#if it's the correct hour for tweettimes[0] but incorrect minute
	if now.hour == tweettimes[0]:
		hoursleft = (tweettimes[1]-now.hour)-1
		seconds = findseconds(hoursleft, minutesleft)
		
		print sleeptime(hoursleft, minutesleft, seconds)
		
		logger.debug(sleeptime(hoursleft, minutesleft, seconds))
		
		sleep(seconds)
		
	#if it's the correct hour for tweettimes[1] but incorrect minute
	elif now.hour == tweettimes[1]:
		hoursleft = ((4-(now.hour-tweettimes[1]))+tweettimes[0])-1
		seconds = findseconds(hoursleft, minutesleft)
		
		print sleeptime(hoursleft, minutesleft, seconds)
		
		logger.debug(sleeptime(hoursleft, minutesleft, seconds))
		
		sleep(seconds)
		
	#if the hour is in-between tweettimes[0] and tweettimes[1]
	elif now.hour > tweettimes[0] and now.hour < tweettimes[1]:
		
		hoursleft = (tweettimes[1]-now.hour)-1
		seconds = findseconds(hoursleft, minutesleft)
		print sleeptime(hoursleft, minutesleft, seconds)
			
		logger.debug(sleeptime(hoursleft, minutesleft, seconds))
			
		sleep(seconds)
			
	#if the hour is earlier than tweettimes[0]
	elif now.hour < tweettimes[0]:
		
		hoursleft = (tweettimes[0]-now.hour)-1
		seconds = findseconds(hoursleft, minutesleft)
		print sleeptime(hoursleft, minutesleft, seconds)
			
		logger.debug(sleeptime(hoursleft, minutesleft, seconds))
			
		sleep(seconds)
			
	#if the hour is later than tweettimes[1]
	elif now.hour > tweettimes[1]:
		
		hoursleft = ((4-(now.hour-tweettimes[1]))+tweettimes[0])-1
		seconds = findseconds(hoursleft, minutesleft)
		print sleeptime(hoursleft, minutesleft, seconds)
			
		logger.debug(sleeptime(hoursleft, minutesleft, seconds))
			
		sleep(seconds)
