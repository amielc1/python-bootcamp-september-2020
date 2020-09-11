connection_details = {
    "apple": "red",
    "lettuce": "green",
    "lemon": "yellow",
    "orange": "orange"
}


def check_user_correction(user, password):
    return user in connection_details and connection_details[user] == password


while True:
    username_input = input("Enter Username")
    password_input = input("Enter Password")
    if check_user_correction(username_input, password_input):
        print("---->>Welcome Master")
    print("INTRUDER ALERT")
