from boltiot import Bolt
import requests, json, time

def get_bitcoin_price():
    URL = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
    response = requests.request("GET", URL)
    response = json.loads(response.text)
    current_price = response["USD"]
    return current_price

api_key = "ebf89e2b-fbf8-473a-96c0-2eb3e835620f"
device_id = "BOLT6094118"
mybolt = Bolt( api_key , device_id )

while True:
    print ("while loop")
    price = get_bitcoin_price()
    print (price)
    if price > 5750:
        buzzer = mybolt.analogWrite('0','100')
        print (buzzer)
        time.sleep(0.005)
        buzzer = mybolt.analogWrite('0','0')
        print (buzzer)
    time.sleep(30)

