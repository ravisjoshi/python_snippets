import pulsar
from pulsar import schema
from pulsar import MessageId, Client

TOPIC_NAME = 'persistent://public/default/my-topic'

# Connect to pulsar via gateway server
client_gateway = Client("pulsar+ssl://eisgatewaytest1.test.intranet:6651/")

# Connect to pulsar via gateway server
client_direct = Client("pulsar://eisgatewaytest2.test.intranet:6650/")

# Set which type of client connection you want to use
client = client_direct

reader = client.create_reader(topic=TOPIC_NAME, start_message_id=MessageId.earliest)

while True:
    try:
        # try and receive messages with a timeout of 10 seconds
        msg = reader.read_next(timeout_millis=10000)
        print("Received message '{}' id='{}'".format(msg.data(), msg.message_id()))
    except Exception:
        print("No message received in queue!!!")
        break

client.close()
