from boltiot import Bolt
import requests, json, time

def trigger_integromat_webhook():
    URL = ""
    response = requests.request("GET", URL)
    print (response.text)

api_key = ""
device_id = ""
mybolt = Bolt( api_key , device_id )
max = 1024
min = 500

while True:
    print ("while loop")
    response = mybolt.analogRead('A0')
    data = json.loads(response)
    print ("Sensor value is :"+str(data['value']))
    try:
        sensor_value = int(data['value'])
        if sensor_value > max or sensor_value < min:
            print ("before trigger")
            trigger_integromat_webhook()
            print ("After trigger")
    except Exception as e:
        print ("error")
        print (e)
    time.sleep(5)

