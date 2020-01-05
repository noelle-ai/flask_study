from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

# `flask.py`로 호출하면, Flask 자체와 충돌 난다.