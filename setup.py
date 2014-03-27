from twython import Twython
from creds import *

yn = raw_input("Run setup? (y/n)")

if yn == "y":
    twitter = Twython(APP_KEY, APP_SECRET)
    
    auth = twitter.get_authentication_tokens()
    
    OAUTH_TOKEN = auth['oauth_token'] 
    OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
    
    print "Log in to the account you want to tweet from, then go here and find the PIN:"
    print auth['auth_url']
    
    oauth_verifier = raw_input('Enter your pin:')
    
    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    
    final_step = twitter.get_authorized_tokens(oauth_verifier)
    
    FINAL_OAUTH_TOKEN = final_step['oauth_token']
    FINAL_OAUTH_TOKEN_SECRET = final_step['oauth_token_secret']
    
    secrets = "".join(["APP_KEY = '", APP_KEY, "'\n", "APP_SECRET = '", APP_SECRET, "'\n", "FINAL_OAUTH_TOKEN = '", FINAL_OAUTH_TOKEN, "'\n", "FINAL_OAUTH_TOKEN_SECRET = '", FINAL_OAUTH_TOKEN_SECRET, "'\n"])
    with open('creds.py', "w") as  credsfile:
        credsfile.write(secrets)
        credsfile.close()
else:
  print "Type `cat creds.py` to see what your credentials are."
  
    