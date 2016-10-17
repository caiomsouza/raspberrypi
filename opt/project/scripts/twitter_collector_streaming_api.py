
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


#Variables that contains the user credentials to access Twitter API
access_token = "PUT_HERE"
access_token_secret = "PUT_HERE"
consumer_key = "PUT_HERE"
consumer_secret = "PUT_HERE"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    #res = stream.filter(track=['Brazil','Pentaho','Micro Strategy'], async=True)

    res = stream.filter(track=['Tableau','Pentaho','Micro Strategy'])

    filename = "/opt/file_mgmt/to_process/output_twitter_" + search_lang + "_" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".json"

    print ("File saved: " + filename)

    # with open('output_pdi.json', 'w') as outfile:
    with open(filename, 'w') as outfile:
     json.dump(res, outfile)
