tweethack
=========

Command lining the twitters with twython.  Search twitter and tweet from your command line in 5 hacky steps.

## Super Easy Command Line Tweeting

**1.** Clone this repo

```
git clone https://github.com/silshack/tweethack.git
```

Or use ssh but if you use ssh why are you reading the how to?

**2.** Make sure you've got Twython

```
pip install twython
```

**3.** `cd` into the new directory. Add a file called `creds.py` with your App's key and secret:

```
APP_KEY = 'Your app key here in quotes'
APP_SECRET = 'Your app secret here in quotes'
```


*Note: You'll need to create a new app and get the key and secret from developer.twitter.com and you'll need read and write access enabled to tweet.  You can find how-tos on this all over the place.  Or [let me google that for you](http://iag.me/socialmedia/how-to-create-a-twitter-app-in-8-easy-steps/).*

**4.** Run `setup.py` and follow the instructions to OAuth your favorite Twitter account:

```
python setup.py
```

**5.** Run `tweethack.py`:

```
python tweethack.py
```

You can then search or tweet.  Done.
