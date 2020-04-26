import websocket, base64, json

header = 'Authorization: BEARER eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTYxOTQ1OTg0NH0.6BHk-f7Y53yJyah5ypKjAaxFtHcLH8vn51D07TQxSic'

TOPIC = 'wss://gateway.eis.ctl.io:8443/pulsar/ws/v2/producer/persistent/public/default/my-topic'

ws = websocket.create_connection(TOPIC, header=header)
# ws = websocket.create_connection(TOPIC, header=['Authorization: BEARER eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTYxOTQ1OTg0NH0.6BHk-f7Y53yJyah5ypKjAaxFtHcLH8vn51D07TQxSic', "x-custom: header"])

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
