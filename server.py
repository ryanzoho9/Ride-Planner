from flask import Flask
from api import api_blueprint
from dotenv import load_dotenv
from flask_socketio import SocketIO
from websockets import register_websocket_handlers
from flask_cors import CORS
import os

load_dotenv()

port_num = os.getenv('PORT')

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(api_blueprint)
socketio = SocketIO(app, async_mode="eventlet")

register_websocket_handlers(socketio)

@app.route('/')
def home():
    return 'Ride Planner'

if __name__ == '__main__':
    socketio.run(app, port=port_num, debug=True)