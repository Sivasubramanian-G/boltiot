import mailconf as conf
from boltiot import Email, Bolt
import json, time

minimum_limit = 350
maximum_limit = 600

mybolt = Bolt (conf.API_KEY, conf.DEVICE_ID)
mailer = Email (conf.MAILGUN_API_KEY, conf.SANDBOX_URL, conf.SENDER_EMAIL, conf.RECIPIENT_EMAIL)

while True:
    print ("Reading sensor value")
    response = mybolt.analogRead ('A0')
    data = json.loads (response)
    print ("Sensor value is: "+ str(data['value']))
    try:
        sensor_value = int (data['value'])
        if (sensor_value > maximum_limit or sensor_value < minimum_limit):
            print ("Making request to Mailgun to send an email")
            response = mailer.send_email("Alert ","The current temperature sensor value is " +str(sensor_value)+"  "+str((100*sensor_value)/1024))
            response_text = json.loads(response.text)
            print ("Response received from Mailgun is: "+str(response_text['message']))
    except Exception as e:
        print ("Error occured: Below are the details")
        print (e)
    time.sleep (10)
