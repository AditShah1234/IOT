import sys

# Import Adafruit IO MQTT client.
from Adafruit_IO import MQTTClient

# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = 'aio_hloW94fCQyIG6ODj5H9LNn4Gw5Eq'

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = 'Adit9497'

# Set to the ID of the feed to subscribe to for updates.
FEED_ID = 'iot.room-temp'
'''
# Define callback functions which will be called when certain events happen.
def connected(client):
    # Connected function will be called when the client is connected to Adafruit IO.
    # This is a good place to subscribe to feed changes.  The client parameter
    # passed to this function is the Adafruit IO MQTT client so you can make
    # calls against it easily.
    print('Connected to Adafruit IO!  Listening for {0} changes...'.format(FEED_ID))
    # Subscribe to changes on a feed named DemoFeed.
    client.subscribe(FEED_ID)



def disconnected(client):
    # Disconnected function will be called when the client disconnects.
    print('Disconnected from Adafruit IO!')
    sys.exit(1)
def subscribe(client, userdata, mid, granted_qos):
    # This method is called when the client subscribes to a new feed.
    print('Subscribed to {0} with QoS {1}'.format(FEED_ID, granted_qos[0]))
def message(client, feed_id, payload):
    # Message function will be called when a subscribed feed has a new value.
    # The feed_id parameter identifies the feed, and the payload parameter has
    # the new value.
    # try_feed =feed_id
    # try_payload = payload
    print('Feed {0} received new value: {1}'.format(feed_id, payload))

'''

# Create an MQTT client instance.
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
if __name__=="__main__":
    # Setup the callback functions defined above.
    client.on_connect    = connected
    client.on_disconnect = disconnected
    client.on_message    = message
    client.on_subscribe  = subscribe

    # Connect to the Adafruit IO server.
    client.connect()

    client.publish(FEED_ID,"21")
    # client.publish(FEED_ID,"e")
    # Start a message loop that blocks forever waiting for MQTT messages to be
    # received.  Note there are other options for running the event loop like doing
    # so in a background thread--see the mqtt_client.py example to learn more.
    client.loop_blocking()
