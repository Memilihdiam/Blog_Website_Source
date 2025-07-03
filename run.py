from flask import Flask, render_template, jsonify, request, session
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__, template_folder='app/templates')
Port = 3120

client = MongoClient('mongodb://mongodb:27017/')
db = client.blogdb
users_collection = db.users
posts_collection = db.posts

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    user = users_collection.find_one({'username': username})

    if user and check_password_hash(user['password'], password):
      session['username'] = username
      session['id_user'] = str(user['_id'])
      return render_template('index.html')
    else:
      return render_template('login.html', error='Invalid username or password')

@app.route('/test_db')
def test_db():
  return jsonify(list(db.list_collection_names()))

if __name__ == '__main__':
  # host='0.0.0.0' membuat server dapat diakses dari luar container
  app.run(host='0.0.0.0', debug = True, port = Port)
