from pulsar import Client, AuthenticationToken, MessageId

TOPIC_NAME='persistent://federal-tenant/federal-namespace/my-topic'

client = Client('pulsar+ssl://gateway.eis.ctl.io:6651/',
                authentication=AuthenticationToken('eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTYxOTQ1OTg0NH0.6BHk-f7Y53yJyah5ypKjAaxFtHcLH8vn51D07TQxSic'))

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
