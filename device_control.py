from boltiot import Bolt
api_key = ""
device_id = ""
mybolt = Bolt( api_key , device_id )
response = mybolt.restart()
print (response)
