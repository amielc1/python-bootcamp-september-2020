# https://www.tocode.co.il/past_workshops/24
from flask import Flask, request, render_template

app = Flask('Amiel GUI website')


@app.route('/')
def index():
    return render_template('index.html', name='Amiel Cohen')


if __name__ == '__main__':
    app.run()
