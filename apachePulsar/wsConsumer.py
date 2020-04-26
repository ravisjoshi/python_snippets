import websocket, base64, json

TOPIC = 'wss://gateway.eis.ctl.io:8443/pulsar/ws/v2/consumer/persistent/public/default/my-topic/my-sub'

ws = websocket.create_connection(TOPIC)

while True:
    msg = json.loads(ws.recv())
    if not msg: break

    print("Received: {} - payload: {}".format(msg, base64.b64decode(msg['payload'])))

    # Acknowledge successful processing
    ws.send(json.dumps({'messageId': msg['messageId']}))

ws.close()
