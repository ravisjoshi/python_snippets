import websocket, base64, json

#TOPIC = 'ws://localhost:8080/ws/v2/reader/persistent/public/default/my-topic'
TOPIC = 'wss://gateway.eis.ctl.io:8443/pulsar/ws/v2/reader/persistent/joshi-tenant/joshi-namespace/rjoshi-topic'

ws = websocket.create_connection(TOPIC)

while True:
    msg = json.loads(ws.recv())
    if not msg: break

    print("Received: {} - payload: {}".format(msg, base64.b64decode(msg['payload'])))

    # Acknowledge successful processing
    ws.send(json.dumps({'messageId' : msg['messageId']}))

ws.close()
