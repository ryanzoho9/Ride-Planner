from flask_socketio import SocketIO, emit

def register_websocket_handlers(socketio: SocketIO):
    """
    Register all WebSocket event handlers.
    """

    print('REACHED REGISTER FUNCTION')
    # Listen for a user message
    @socketio.on('user_message')
    def handle_user_message(data):
        print(f"Received message: {data}")
        
        # Respond dynamically based on the message
        if data.lower() == "hello":
            emit('response', "Hi there! How can I help you?")
        elif data.lower() == "bye":
            emit('response', "Goodbye! Have a great day!")
        else:
            emit('response', f"You said: {data}")

    # Example for broadcasting
    @socketio.on('broadcast_message')
    def handle_broadcast_message(data):
        print(f"Broadcasting message: {data}")
        emit('response', f"Broadcast: {data}", broadcast=True)

    # Handle WebSocket connections
    @socketio.on('connect')
    def on_connect():
        print("A client connected")

    # Handle WebSocket disconnections
    @socketio.on('disconnect')
    def on_disconnect():
        print("A client disconnected")
