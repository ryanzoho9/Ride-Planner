from flask import Flask
from api import api_blueprint
from dotenv import load_dotenv
import os

load_dotenv()

port_num = os.getenv('PORT')

app = Flask(__name__)

app.register_blueprint(api_blueprint)

@app.route('/')
def home():
    return 'Ride Planner'

if __name__ == '__main__':
    app.run(port=port_num, debug=True)