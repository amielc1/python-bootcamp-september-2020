def get_while_empty(items_list):
    temp_list = []
    for item in items_list:
        if not item:  # if item is "":
            return temp_list[::-1]
        temp_list.append(item)
