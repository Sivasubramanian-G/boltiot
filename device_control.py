from boltiot import Bolt
api_key = "ebf89e2b-fbf8-473a-96c0-2eb3e835620f"
device_id = "BOLT6094118"
mybolt = Bolt( api_key , device_id )
response = mybolt.restart()
print (response)
