import socketio

# Create a Socket.IO client
sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print("Connected to server")

@sio.on('disconnect')
def on_disconnect():
    print("Disconnected from server")

@sio.on('response')
def on_response(data):
    print(f"Response from server: {data}")

# Connect to the server
sio.connect('http://127.0.0.1:3002')

# Send a message
sio.emit('user_message', "SOME OTHER THING??!?!")

# Wait for a response
sio.wait()
