from pulsar import Client, AuthenticationToken

client = Client('pulsar+ssl://gateway.eis.ctl.io:6651/',
                authentication=AuthenticationToken('eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmZWRlcmFsLXVzZXIiLCJleHAiOjE2MTk0NDcxNDB9.5U0ganBuyyEEYyW77KgUxutVXW0AqmQJdygchG1r13w'))
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
