from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory storage for simplicity
posts = [
    {'id': 1, 'title': 'First Post', 'body': 'This is the first post', 'userId': 1},
    {'id': 2, 'title': 'Second Post', 'body': 'This is the second post', 'userId': 1}
]

# Get all posts
@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

# Get a single post by ID
@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if post:
        return jsonify(post)
    return jsonify({'error': 'Post not found'}), 404

# Create a new post
@app.route('/posts', methods=['POST'])
def create_post():
    new_post = request.get_json()
    new_post['id'] = len(posts) + 1
    posts.append(new_post)
    return jsonify(new_post), 201

# Update an existing post
@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    updated_post = request.get_json()
    post = next((post for post in posts if post['id'] == post_id), None)
    if post:
        post.update(updated_post)
        return jsonify(post)
    return jsonify({'error': 'Post not found'}), 404

# Delete a post
@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    global posts
    posts = [post for post in posts if post['id'] != post_id]
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
