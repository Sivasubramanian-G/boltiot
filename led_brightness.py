from boltiot import Bolt
api_key = ""
device_id = ""
mybolt = Bolt( api_key , device_id )
response = mybolt.analogWrite('0','100')
print (response)
