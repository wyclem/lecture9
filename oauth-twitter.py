
from requests_oauthlib import OAuth1Session
import secrets
import json
import sys
import codecs 

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)


client_key = secrets.api_key
client_secret = secrets.api_secret

resource_owner_key = secrets.access_token
resource_owner_secret = secrets.access_token_secret

protected_url = 'https://api.twitter.com/1.1/account/settings.json'

oauth = OAuth1Session(client_key,
                          client_secret=client_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret)

protected_url = 'https://api.twitter.com/1.1/search/tweets.json'
params = {'q':'food'}
r = oauth.get(protected_url, params=params)


r_dict = json.loads(r.text)
for tweet in r_dict["statuses"]:
    print(tweet['user']['name'] + ":")
    print(tweet['text'])
    print("--------------")

