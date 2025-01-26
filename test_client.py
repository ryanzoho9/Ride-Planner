import socketio

# Create a Socket.IO client
sio = socketio.Client()

# Connect to the server
sio.connect('http://127.0.0.1:3002')

# Define event handlers
@sio.on('rsvp_update')
def on_rsvp_update(data):
    print(f"RSVP Update Received: {data}")

@sio.on('error')
def on_error(data):
    print(f"Error: {data}")

# Emit an 'rsvp' event to the server
sio.emit('rsvp', {
    "user_id": "user123",
    "car_go_in_id": "car456"
    })

# Wait for the response
sio.wait()
