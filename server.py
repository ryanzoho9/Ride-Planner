from flask import Flask
from api.routes import api_blueprint

app = Flask(__name__)

app.register_blueprint(api_blueprint, url_prefix='/api')

@app.route('/')
def home():
    return 'Virtual Real Estate Agent Home Page'

if __name__ == '__main__':
    app.run(debug=True)