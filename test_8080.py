from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return 'Hello World 8080'

@app.route('/edu')
def edu():
    return "8080 - edu"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)