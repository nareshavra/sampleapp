from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (in a real application, this would come from a database)
users = [
    {"id": 1, "name": "John Doe"},
    {"id": 2, "name": "Jane Smith"},
    {"id": 3, "name": "Bob Johnson"}
]

# Define routes
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({"message": "User not found"}), 404

@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.get_json()
    if not new_user or 'name' not in new_user:
        return jsonify({"message": "Invalid request"}), 400
    new_user['id'] = len(users) + 1
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(debug=True)