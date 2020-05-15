import websocket, base64, json

# Connect to pulsar via gateway server
TOPIC_gateway = 'wss://eisgatewaytest1.test.intranet:8443/pulsar/ws/v2/reader/persistent/public/default/my-topic'

# Connect to pulsar via gateway server
TOPIC_direct = 'ws://eisgatewaytest2.test.intranet:8080/ws/v2/reader/persistent/public/default/my-topic'

ws = websocket.create_connection(TOPIC_direct)

while True:
    msg = json.loads(ws.recv())
    if not msg: break

    print("Received: {} - payload: {}".format(msg, base64.b64decode(msg['payload'])))

    # Acknowledge successful processing
    ws.send(json.dumps({'messageId': msg['messageId']}))

ws.close()
