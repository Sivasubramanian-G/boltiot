import tweepy
import tweetconf as conf
import json, time
from boltiot import Bolt

# Dictionary storing credentials

config = {
"consumer_key" : conf.consumer_key,
"consumer_secret" : conf.consumer_secret,
"access_token" : conf.access_token,
"access_token_secret" : conf.access_token_secret
}

# Method to authenticate user via Tweepy and return API object

def get_api_object(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

mybolt = Bolt(conf.bolt_cloud_api_key, conf.device_id)
temperature_threshold = 59
while True:
    print ("Reading data from the sensor")
    response = mybolt.analogRead('A0')
    print ("sensor data : "+response)
    data = json.loads(response)
    print (data['value'])
    try:
        sensor_value = int(data['value'])
        if sensor_value > temperature_threshold:
            print ("Temperature has crossed the threshold.")
            # call get_api_object to authenticate user and get the API object
            api_object = get_api_object(config)
            # store the tweet message in variable
            tweet = ("Twitter app : Temperature has crossed the threshold.")
            # post the tweet on your twitter account using the update_status method.
            status = api_object.update_status(status = tweet)
    except Exception as e:
        print ("An error occured ",e)
    time.sleep(10)
