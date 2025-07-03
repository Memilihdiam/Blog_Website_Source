from flask import Flask, render_template

app = Flask(__name__)
Port = 3120

if __name__ == '__main__':
  app.run(debug = False, port = Port)
