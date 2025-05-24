from flask import Flask, jsonify
from flask_cors import CORS # Import CORS

app = Flask(__name__)
CORS(app) # Enable CORS for all routes, allowing frontend to access it

@app.route('/api/message', methods=['GET'])
def get_message():
    """
    Returns a simple JSON message.
    """
    return jsonify({'message': 'Hello from the Flask Backend Container!'})

if __name__ == '__main__':
    # Run the Flask app, accessible from any IP (0.0.0.0) on port 5000
    # debug=False for production readiness
    app.run(debug=False, host='0.0.0.0', port=5000)