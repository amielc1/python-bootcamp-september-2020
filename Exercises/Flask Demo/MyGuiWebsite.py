# https://www.tocode.co.il/past_workshops/24
from flask import Flask, request, render_template

app = Flask('Amiel GUI website')


@app.route('/', methods=['POST', 'GET'])
def index():
    if 'name' in request.values:
        name = request.values['name']
    else:
        name = "Please enter your name"
    return render_template('index.html', name=name)


if __name__ == '__main__':
    app.run()
