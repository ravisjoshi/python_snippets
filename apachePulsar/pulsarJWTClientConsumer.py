from pulsar import Client, AuthenticationToken, MessageId

client = Client('pulsar+ssl://gateway.ravi.joshi.tld:6651/',
                authentication=AuthenticationToken('exxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxc'))

consumer = client.subscribe('persistent://joshi-tenant/joshi-namespace/my-topic', 'my-sub')

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
