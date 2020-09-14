# https://www.tocode.co.il/past_workshops/24
from flask import Flask,request

app = Flask('Amiel website')


@app.route('/')
def index():
    return "Welcome to  my Website1"

@app.route('/hello/<name>')
def hello(name):
    return f"Hello {name}"

@app.route('/hello2')
def hello2():
    name = request.args['name']
    return f"Hello {name}"

if __name__ == '__main__':
    app.run()
