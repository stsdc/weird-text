"""API"""

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

from decoder import Decoder
from encoder import Encoder

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

encoder = Encoder()
decoder = Decoder()


@app.route('/v1/encode', methods=['POST'])
def encode():
    """Handling the request to encode a text."""
    encoded_text = encoder.encode(request.json['text'])
    return jsonify({'encoded_text': encoded_text})


@app.route('/v1/decode', methods=['POST'])
def decode():
    """Handling the request to decode a text."""
    decoder.word_list = encoder.word_list
    decoded_text = decoder.decode(request.json['encoded_text'])
    return jsonify({'decoded_text': decoded_text})
