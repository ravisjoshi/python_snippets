from pulsar import Client, AuthenticationToken

# Create a Pulsar client instance. The instance can be shared across multiple
# producers and consumers
client = Client('pulsar+ssl://gateway.eis.ctl.io:6651/',
                authentication=AuthenticationToken('eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTYxOTQ1OTg0NH0.6BHk-f7Y53yJyah5ypKjAaxFtHcLH8vn51D07TQxSic'))

# Create a producer on the topic. If the topic doesn't exist
# it will be automatically created
producer = client.create_producer('persistent://federal-tenant/federal-namespace/my-topic')

for i in range(10):
    content = 'hello-pulsar-%d' % i
    # Publish a message and wait until it is persisted
    producer.send(bytes(content.encode('utf-8')))
    print('Published message: "%s"' % content)

client.close()
