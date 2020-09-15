# https://www.tocode.co.il/past_workshops/24
from flask import Flask, request, render_template

app = Flask('Amiel GUI website')

connection_details = {
    "apple": "red",
    "lettuce": "green",
    "lemon": "yellow",
    "orange": "orange"
}


def check_user_correction(user, password):
    return user in connection_details and connection_details[user] == password


# , methods=['POST', 'GET']
@app.route('/')
def index():
    result = ""
    if 'username' in request.values and 'password' in request.values:
        if check_user_correction(request.values['username'], request.values['password']):
            result = "Welcome Master"
        else:
            result = "INTRUDER ALERT"
    return render_template('index.html', verification_result=result)


@app.route('/anagrams')
def anagrams():
    return "<h1>I need to resolve it.......</h1>"


if __name__ == '__main__':
    app.run()
