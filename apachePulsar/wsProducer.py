import websocket, base64, json

# Connect to pulsar via gateway server
TOPIC_gateway = 'wss://dev.gateway.eis.ctl.io:8443/pulsar/ws/v2/producer/persistent/public/default/my-topic'

# Connect to pulsar via gateway server
TOPIC_direct = 'ws://eisgatewaytest2.test.intranet:8080/ws/v2/producer/persistent/public/default/my-topic'

ws = websocket.create_connection(TOPIC_gateway)

# Send one message as JSON
data = json.dumps({
    'payload': 'TestPayload',
    'properties': {'key1': 'Ravi', 'key2': 'Joshi'},
    'context': 5
})

ws.send(data)
response = json.loads(ws.recv())

if response['result'] == 'ok':
    print('Message published successfully')
else:
    print('Failed to publish message:', response)
ws.close()
