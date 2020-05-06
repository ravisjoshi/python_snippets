import websocket, base64, json

TOPIC = 'wss://gateway.ravi.joshi.tld:8443/pulsar/ws/v2/producer/persistent/public/default/my-topic'

ws = websocket.create_connection(TOPIC, header=header)

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
