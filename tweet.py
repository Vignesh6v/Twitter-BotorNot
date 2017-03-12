import csv
import tweepy
import ConfigParser


config = ConfigParser.ConfigParser()
config.read('credentials.txt')

consumer_key = config.get("TWITTER","consumer_key")
consumer_secret = config.get("TWITTER","consumer_secret")
access_token = config.get("TWITTER","access_token")
access_token_secret = config.get("TWITTER","access_token_secret")




auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def getData(usernames):
    for username in usernames:
        user = api.get_user(username)
        print username
        data = dataFormat(user)
        # print data
        with open('userData.csv','a') as f:
            wr = csv.writer(f, quoting=csv.QUOTE_ALL)
            wr.writerow(data)

    print 'done'

def dataFormat(user):
    status = user.status if hasattr(user, 'status') else ''
    name = ''.join(user.name).encode('utf-8').strip() if hasattr(user, 'name') else ''
    location = ''.join(user.location).encode('utf-8').strip() if hasattr(user, 'location') else ''
    description = ''.join(user.description).encode('utf-8').strip() if hasattr(user, 'description') else ''
    #url = ''.join(user.url).encode('utf-8').strip() if hasattr(user, 'url') else ''
    data = [user.id,user.id_str,user.screen_name,location,description,user.url,user.followers_count,user.friends_count,user.listed_count,user.created_at,user.favourites_count,user.verified,user.statuses_count,user.lang,status,user.default_profile,user.default_profile_image,user.has_extended_profile,name]
    return data


userList = []
with open('userList.txt') as f:
    for line in f:
        userList += line.strip(),

print userList
getData(userList)
