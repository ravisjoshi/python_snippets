import json
from pulsar import Client

# Connect to pulsar via gateway server
client_gateway = Client("pulsar+ssl://eisgatewaytest1.test.intranet:6651/")

# Connect to pulsar via gateway server
client_direct = Client("pulsar://eisgatewaytest2.test.intranet:6650/")

# Set which type of client connection you want to use
client = client_direct

producer = client.create_producer('persistent://public/default/my-topic')

for i in range(10):
    content = 'hello-pulsar-%d' % i
    # Publish a message and wait until it is persisted
    producer.send(bytes(content.encode('utf-8')))
    print('Published message: "%s"' % content)

client.close()
