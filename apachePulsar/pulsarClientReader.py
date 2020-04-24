import pulsar
from pulsar import schema
from pulsar import MessageId

TOPIC_NAME='persistent://joshi-tenant/joshi-namespace/rjoshi-topic'

client = pulsar.Client('pulsar+ssl://gateway.eis.ctl.io:6651')
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
