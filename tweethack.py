from twython import Twython
from creds import *


twitter = Twython(APP_KEY, APP_SECRET,
                  FINAL_OAUTH_TOKEN, FINAL_OAUTH_TOKEN_SECRET)


quit = ""
  
while quit != True:
  exit = ""
  tos = raw_input("Would you like to tweet, search, or exit? (tweet, search or quit)  ")
  if tos == "tweet":
    print "Let's tweet from the command line!"
    
    while exit != True:
      tweet = raw_input("What would you like to tweet?  ")
      twitter.update_status(status = tweet)
      exit = raw_input("Type exit to quit or press enter to Tweet again.  ")
      if exit == "exit":
        exit = True
  elif tos == "search":
    print "Let's search from the command line!"
    
    while exit != True:
      query = raw_input("What would you like to search? ")
      twitter.search(q=query, result_type='popular')
      exit = raw_input("Type exit to quit or press enter to search again.  ")
      if exit == "exit":
        exit = True