'''
Created on Oct 28, 2017

@author: Remy Kaldawy
'''

import tweepy
import json
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

class MyListener(StreamListener):
    
    def on_data(self, data):
        try:
            # Prints the text of the tweet
            
            
            
            jsdata = json.loads(data)
            print(jsdata)
            
            with open('python.json', 'a') as f:
                json.dump(jsdata, f)
                f.write('\n')
                
            #print('Tweet text: ' + jsdata['text'])
 
        # There are many options in the status object,
        # hashtags can be very easily accessed.
            #print(jsdata['hashtags'])
            
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
    
    def on_error(self, status):
        print(status)
        return True

def process_or_store(tweet):
    with open('C:/Users/Remy Kaldawy/Documents/Java/Workspace/test_twitter_analytics/data.json', 'w') as outfile:
        json.dump(tweet, outfile)
    print(json.dumps(tweet))

consumer_key = 'HWkor8wKHkIyBUVZLMBmBHCRt'
consumer_secret = 'HVkLGi8jigRWA0xVcvWJNXSoujtNtp7Bhpjsec6iOmsKNZlwl3'

access_key = '1540121672-Ja4RMTwjQTbKpexmU9BjwXmHJet6Hw4olxH2e55'
access_secret = 'Xsdk6rQ5CFBHaMyFegR63YWxjY5YVeBtAgzoErDaQY750'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)
   
# for friend in tweepy.Cursor(api.friends).items():
#     process_or_store(friend._json)

open('python.json', 'w').close()

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#iphonex'])
