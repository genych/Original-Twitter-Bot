#importing the python smtp library and logging
import smtplib
import logging

#account information setup
username = "yourbotsemail@gmail.com"
password = "yourpasswordhere"

#setting up logging
logging.basicConfig(filename = "twitterbot.log",level=logging.DEBUG)
logger = logging.getLogger(__name__)

def sendmail(recipient, subject, body):
	
	#the whole pacakge deal, sender, receiver, subject, and body
	message = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (username, recipient, subject, body)
	logger.info("Email message consolidated successfully.")
	
	logger.debug("Setting up SMTP server...")
	#setting smtp server (smtp.google.com) and the smtp port
	mail = smtplib.SMTP("smtp.gmail.com",587)
	
	logger.debug("Broadcasting ehlo...")
	#indentifying this program to the google server as eSMTP (extended smtp)
	mail.ehlo()
	logger.debug("Broadcast successful.")
	
	logger.debug("Starting TLS...")
	#starts "tls", makes all internet activity beyond this point encrypted (important for logger in with username and password)
	mail.starttls()
	logger.debug("TLS started successfully.")
	
	logger.debug("Logging in...")
	#login
	mail.login(username, password)
	logger.debug("Login as %s successful." % (username))
	
	logger.debug("Sending email...")
	#send the email!
	mail.sendmail(username, recipient, message)
	logger.debug("Email sent successfully!")
	
	#close the mail stream
	mail.close()
	logger.info("Mail stream closed.")
