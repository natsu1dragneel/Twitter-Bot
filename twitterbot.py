import tweepy as tp
import time, os


#login into twitter api                               #provide it yourself
consumer_key=''                                                      
consumer_secret=''
access_token=''
access_secret=''

auth=tp.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api=tp.API(auth)

#iterates the folder content
os.chdir('')
for folder_name in os.listdir('.'):
    api.update_with_media(folder_name)                          #api.update_status be used for text based content
    time.sleep(3600)
