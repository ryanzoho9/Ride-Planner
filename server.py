from flask import Flask
from api import api_blueprint
from dotenv import load_dotenv
from flask_socketio import SocketIO
from websockets import register_websocket_handlers
import os

load_dotenv()

port_num = os.getenv('PORT')

app = Flask(__name__)

app.register_blueprint(api_blueprint)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")

register_websocket_handlers(socketio)

@app.route('/')
def home():
    return 'Ride Planner'

if __name__ == '__main__':
    socketio.run(app, port=port_num, debug=True)