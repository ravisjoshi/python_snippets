from pulsar import Client

# Connect to pulsar via gateway server
client_gateway = Client("pulsar+ssl://eisgatewaytest1.test.intranet:6651/")

# Connect to pulsar via gateway server
client_direct = Client("pulsar://eisgatewaytest2.test.intranet:6650/")

# Set which type of client connection you want to use
client = client_direct

consumer = client.subscribe('persistent://public/default/my-topic', 'my-sub')

while True:
    try:
        # try and receive messages with a timeout of 10 seconds
        msg = consumer.receive(timeout_millis=15000)

        # Do something with the message
        print("Received message '%s'", msg.data())

        # Acknowledge processing of message so that it can be deleted
        consumer.acknowledge(msg)
    except Exception:
        print("No message received in the last 15 seconds")
        break

client.close()
