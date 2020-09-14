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


"""
Uri's comments:
==============

* This code works, however it always prints "INTRUDER ALERT" which is not
  what expected. It should either print "---->>Welcome Master" or "INTRUDER ALERT".
* while True is causing an endless loop and is not necessary.
* File names, it's better to write in lowercase (like variable names) and then 
  import from the name in lowercase.

"""
