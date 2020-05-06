from pulsar import Client, AuthenticationToken

# Create a Pulsar client instance. The instance can be shared across multiple
# producers and consumers
client = Client('pulsar+ssl://gateway.ravi.joshi.tld:6651/',
                authentication=AuthenticationToken('exxxxxxxxxxxxxxxxxxxxxxc'))

# Create a producer on the topic. If the topic doesn't exist
# it will be automatically created
producer = client.create_producer('persistent://joshi-tenant/joshi-namespace/my-topic')

for i in range(10):
    content = 'hello-pulsar-%d' % i
    # Publish a message and wait until it is persisted
    producer.send(bytes(content.encode('utf-8')))
    print('Published message: "%s"' % content)

client.close()
