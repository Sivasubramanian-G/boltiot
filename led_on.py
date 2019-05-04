from boltiot import Bolt
api_key = ""
device_id = ""
mybolt = Bolt( api_key , device_id )
response = mybolt.digitalWrite('0','HIGH')
print (response)
