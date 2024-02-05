from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from db import *
from dotenv import load_dotenv

load_dotenv()

# Init server backend
app = Flask(__name__)

# Apply flask cors
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/bodydata', methods=['POST'])
@cross_origin(origins='*')
def save_body_data():
    data = request.get_json()
    info = data['info']
    measurement = data['measurement']
    image = data['image']

    try:
        insert_data(app, data)
        return jsonify({
            'status': 200,
            'message': 'Data inserted successfully into MongoDB!'
        })
    except Exception as e:
        return jsonify({
            'status': 500,
            'message': f'Something wrong: {e=}, type:{type(e)}'
        })

@app.route('/', methods=['GET'])
def helloworld():
    return jsonify({
        'message': 'Hello World!'
    })

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({
        'status': 404,
        'message': 'Page not found!'
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6868, debug=True)
