import mailconf as conf
import twilioconf as sconf
from boltiot import Email, Sms, Bolt
import json, time

minimum_limit = 600
maximum_limit = 1024

mybolt = Bolt (conf.API_KEY, conf.DEVICE_ID)
mailer = Email (conf.MAILGUN_API_KEY, conf.SANDBOX_URL, conf.SENDER_EMAIL, conf.RECIPIENT_EMAIL)
sms = Sms(sconf.SID, sconf.AUTH_TOKEN, sconf.TO_NUMBER, sconf.FROM_NUMBER)

while True:
    print ("Reading sensor value")
    response = mybolt.analogRead ('A0')
    data = json.loads (response)
    print ("Sensor value is: "+ str(data['value']))
    try:
        sensor_value = int (data['value'])
        if (sensor_value > maximum_limit or sensor_value < minimum_limit):
            print ("Making request to Mailgun and twilio to send an email and a message")
            response = mailer.send_email("Alert ","The current light sensor value is " +str(sensor_value))
            responsesms = sms.send_sms("The current light sensor value is " +str(sensor_value))
            response_text = json.loads(response.text)
            print ("Response received from Twilio is: "+str(responsesms))
            print ("Status of SMS at Twilio is: "+str(responsesms.status))
            print ("Response received from Mailgun is: "+str(response_text['message']))
    except Exception as e:
        print ("Error occured: Below are the details")
        print (e)
    time.sleep (10)
