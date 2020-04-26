import websocket, base64, json

TOPIC = 'wss://gateway.eis.ctl.io:8443/pulsar/ws/v2/producer/persistent/public/default/my-topic'

ws = websocket.create_connection(TOPIC)

# Send one message as JSON
data = json.dumps({
    'payload': 'TestPayload',
    'properties': {'key1': 'Centurylink', 'key2': 'Federal'},
    'context': 5
})

ws.send(data)
response = json.loads(ws.recv())

if response['result'] == 'ok':
    print('Message published successfully')
else:
    print('Failed to publish message:', response)
ws.close()
