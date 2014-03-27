# -*- coding: utf-8 -*-
from twython import Twython

import os
import time
import sys
import time
import cleverbottwo
import eliza
import datetime
from random import choice, randint
from creds import *
#import any other natual processing libs


"""Serialize function. Writes the last_reply_id to the file ~/.twitter_last_reply"""
def cleanup(last_id):
  try:
    filename = os.environ.get("HOME",'')+os.sep+'.twitter_last_reply'
    f = file(filename, 'w')
    f.write(last_id)
    f.close()
  except IOError:
    print "[!] ERROR could not open", filename


#These are the keys from the twitter tools for python library.
CONSUMER_KEY = 'uS6hO2sV6tDKIOeVjhnFnQ'
CONSUMER_SECRET = 'MEYTOS97VvlHX7K1rwHPEqVpTSqZ71HtvoK4sVuYk'

# input your bot handle
handle = "@silshack"

clock = datetime.datetime.now()

doctor = eliza.eliza()

doctorisms = ["  Mmkay?",  "  Hmmm?", "  :/", " :)", "  I mean...."]

statuses = [u'    (╯°□°）╯︵ ┻━┻)',
            u'I drifted off there for a bit....Ƹ̵̡Ӝ̵̨̄Ʒ', 
            u'¯\_(ツ)_/¯   wah wahh',
            u'Time for a fish: .·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>',
            u'I wish I owned a little cabin somewhere. __̴ı̴̴̡̡̡ ̡͌l̡̡̡ ̡͌l̡*̡̡ ̴̡ı̴̴̡ ̡̡͡|̲̲̲͡͡͡ ̲▫̲͡ ̲̲̲͡͡π̲̲͡͡ ̲̲͡▫̲̲͡͡ ̲|̡̡̡ ̡ ̴̡ı̴̡̡ ̡͌l̡̡̡̡.___',
            u'HANDS OFF MY SERVERS  ̿\̵͇̿̿\з=(◕_◕)=ε/̵͇̿̿/',
            u'ˁ˚ᴥ˚ˀ   That is all.',
            u'()==[:::::::::::::>',
            u'▇ ▅ █ ▅ ▇ ▂ ▃ ▁ ▁ ▅ ▃ ▅ ▅ ▄ ▅ ▇']
            

if __name__ == "__main__":

  #anyone talking to us?
  last_id_replied = ''
  speaker_id = ''
  message_id = ''
  
  #we serialize into a file in ~/.twitter_last_reply. check if this file is present and read value.
  last_file = os.environ.get("HOME",'')+os.sep+'.twitter_last_reply'
  if os.path.exists(last_file):
    try:
      id_file=file(last_file , 'r')
      id = id_file.readline()
      last_id_replied = id.strip()
      print "[+] Read last_reply_id", last_id_replied
    except IOError:
      print"[!] Could not read ", last_file
  else: print"[!] Didn't find ~/.twitter_last_reply file.. starting fresh prince"

  #twitter client to post. Posting requires oAuth schutff
  twitter = Twython(APP_KEY, APP_SECRET, FINAL_OAUTH_TOKEN, FINAL_OAUTH_TOKEN_SECRET)
  
  #our cleverbot instance
  cbot=cleverbottwo.Session()
  #main loop. Just keep searching anyone talking to us
  while True:
    try:
      mentions = twitter.search(q=handle, since_id=last_id_replied)['statuses']
      if not mentions:
        print "No one talking to us now...", time.ctime()
      for mention in mentions[:3]:
        #cut our handle out 
        message = mention['text'].replace(handle , '')
        message_id = mention['id']
        speaker = mention['user']['screen_name']
        
        speaker_id = str(mention['user']['id'])
        print "[+] Something named "+speaker+" is saying "+message
        
        # If it's not the bot speaking:
        if speaker != handle[1:]:
          # follow the user
          twitter.create_friendship(screen_name = speaker, follow = "true")
          #clever_response = cbot.Ask(message)
          clever_response = doctor.respond(message.strip())
          reply = '@%s %s' % (speaker, clever_response + choice(doctorisms)) 
          print "[+] Replying " , reply
          twitter.update_status(status=reply, in_reply_to_status_id = message_id)
        #update last_id_replied
        last_id_replied=str(int(message_id) + 1)
        cleanup(last_id_replied)

      print "Last message_id was ", message_id
      print "[Zzz] Slumber...\n"
      time.sleep(10)
      hour = clock.hour
      if randint(1, 10000) < 416:
        if hour > 10 and time.hour < 24:
          zzz = "z" * randint(1,10) + "." * randint(1,25)
          twitter.update_status(status==zzz)
        stat = choice(statuses)
        print "Soooo bored.  Saying something random now:"
        print stat
        twitter.update_status(status=stat)

    except KeyboardInterrupt:
      print"[!] Cleaning up. Last speaker_id was ", speaker_id, ".  Last message_id was ", message_id
      cleanup(last_id_replied)
      sys.exit()
      
