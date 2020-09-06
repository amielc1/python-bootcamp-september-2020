def get_while_empty(list):
    temp_list=[]
    for item in list:
        if item is "":
            return  temp_list[::-1]
        temp_list.append(item)