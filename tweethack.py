from twython import Twython
from creds import *


twitter = Twython(APP_KEY, APP_SECRET,
                  FINAL_OAUTH_TOKEN, FINAL_OAUTH_TOKEN_SECRET)

exit = ""

print "Let's tweet from the command line!"

while exit != True:
  tweet = raw_input("What would you like to tweet? ")
  twitter.update_status(status = tweet)
  exit = raw_input("Type exit to quit or press enter to Tweet again")
  if exit == "exit":
    exit = True