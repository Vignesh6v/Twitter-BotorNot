import csv
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import ConfigParser
import pprint
import time


pp = pprint.PrettyPrinter(indent=4)
config = ConfigParser.ConfigParser()
config.read('credentials.txt')

consumer_key = config.get("TWITTER","consumer_key")
consumer_secret = config.get("TWITTER","consumer_secret")
access_token = config.get("TWITTER","access_token")
access_token_secret = config.get("TWITTER","access_token_secret")

oauth = OAuth(access_token, access_token_secret,consumer_key, consumer_secret)
twitter = Twitter(auth=oauth)

#tweets = twitter.statuses.user_timeline(screen_name="Adele", count = 2)



def getData(usernames,counter):
    for username in usernames:
        if username.startswith('"') and username.endswith('"'): username = username[1:-1]
        if counter == 850:
            time.sleep(1000)
            counter=0
        try:
            tweets = twitter.statuses.user_timeline(screen_name=username, count = 100)
            counter+=1
            #pp.pprint(tweets)
            print len(tweets)
            data = dataFormat(tweets,username)
            with open('test_tweets.csv','a') as c:
                wr = csv.writer(c, quoting=csv.QUOTE_ALL)
                wr.writerow(data)

            c.close()
        except Exception as e:
            print username,e

    print 'done'


def dataFormat(tweets,username):
    created_at =[]
    texts = []
    in_reply = 0
    total_usrmention = 0
    fav_count = 0
    retweet_count = 0
    for tweet in tweets:
        if 'created_at' in tweet:
            created_at.append(''.join(tweet['created_at']).encode('utf-8').strip())
        if (('in_reply_to_screen_name' in tweet) and (tweet['in_reply_to_screen_name'] is not None)):
            in_reply += 1
        if 'text' in tweet:
            texts.append(''.join(tweet['text']).encode('utf-8').strip())
        if 'entities' in tweet and tweet['entities']['user_mentions']:
            total_usrmention +=len(tweet['entities']['user_mentions'])
        if 'favorite_count' in tweet and tweet['favorite_count'] > 0:
            fav_count +=1
        if 'retweet_count' in tweet and tweet['retweet_count'] > 0:
            retweet_count +=1
    data = [username,in_reply,retweet_count,fav_count,total_usrmention,created_at,texts]
    return data

userList = []

with open('usertext.txt','rU') as f:
    for line in f:
        userList += line.strip(),

print userList
counter = 0
getData(userList,counter)
